import hashlib
import hmac
import json

import pytest

from telapi_python.models import (
    LoggedOutEvent,
    LoginUpdatedEvent,
    MessageEvent,
    MessagesDeletedEvent,
    PausedEvent,
)
from telapi_python.types import UNSET
from telapi_python.webhooks import (
    EVENT_MODELS,
    InvalidSignature,
    UnknownEvent,
    parse_event,
    sign,
    verify,
    verify_and_parse,
    verify_signature,
)

SECRET = "5f" * 32  # used as the string the gateway showed, not decoded
NOW = 1794500000.0


def envelope(event_type: str, data: dict) -> dict:
    return {
        "id": "0b8e9c1e-3f4a-4c6b-9a57-2f1d8e7c6b5a",
        "type": event_type,
        "accountId": "6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f",
        "accountName": "sales-1",
        "timestamp": 1794500000,
        "data": data,
    }


def delivery(event: dict, timestamp: str = "1794500000") -> tuple[dict, bytes]:
    body = json.dumps(event).encode()
    headers = {
        "X-Telapi-Event": event["type"],
        "X-Telapi-Delivery": event["id"],
        "X-Telapi-Timestamp": timestamp,
        "X-Telapi-Signature": sign(SECRET, timestamp, body),
    }
    return headers, body


MESSAGE = envelope(
    "Message",
    {
        "message": {
            "messageId": 42,
            "chatId": -1001234567890,
            "senderId": 777000,
            "out": False,
            "date": 1794500000,
            "text": "Есть в наличии?",
            "forwarded": False,
        },
        "chat": {"chatId": -1001234567890, "type": "supergroup", "title": "Покупатели"},
        "sender": {"userId": 777000, "name": "Анна"},
    },
)


def test_the_signature_is_the_hmac_of_timestamp_dot_body_under_the_secret_string():
    body = b'{"id":"x"}'
    expected = hmac.new(SECRET.encode(), b"1794500000." + body, hashlib.sha256).hexdigest()
    assert sign(SECRET, "1794500000", body) == "sha256=" + expected


def test_a_delivery_verifies_and_parses_into_its_model():
    headers, body = delivery(MESSAGE)
    event = verify_and_parse(SECRET, headers, body, now=NOW)

    assert isinstance(event, MessageEvent)
    assert event.data.message.message_id == 42
    assert event.data.chat.title == "Покупатели"
    assert event.data.sender.name == "Анна"


def test_a_message_in_a_forum_topic_or_a_channels_direct_messages_carries_where_it_is():
    in_topic = json.loads(json.dumps(MESSAGE))
    in_topic["data"]["message"]["topicId"] = 42
    event = parse_event(in_topic)
    assert event.data.message.topic_id == 42
    assert event.data.message.monoforum_peer_id is UNSET

    in_thread = json.loads(json.dumps(MESSAGE))
    in_thread["data"]["message"]["monoforumPeerId"] = 777000
    event = parse_event(in_thread)
    assert event.data.message.monoforum_peer_id == 777000
    assert event.data.message.topic_id is UNSET

    assert parse_event(MESSAGE).data.message.topic_id is UNSET


def test_headers_are_found_in_any_case():
    headers, body = delivery(MESSAGE)
    lowered = {k.lower(): v for k, v in headers.items()}
    assert verify(SECRET, lowered, body, now=NOW)


@pytest.mark.parametrize(
    "change",
    [
        lambda h, b: (h, b + b" "),  # the body changed
        lambda h, b: ({**h, "X-Telapi-Signature": "sha256=" + "0" * 64}, b),  # another signature
        lambda h, b: ({**h, "X-Telapi-Timestamp": "1794500001"}, b),  # the timestamp changed
        lambda h, b: ({k: v for k, v in h.items() if k != "X-Telapi-Signature"}, b),  # no signature
        lambda h, b: ({**h, "X-Telapi-Timestamp": "soon"}, b),  # not a number
    ],
)
def test_a_tampered_delivery_does_not_verify(change):
    headers, body = change(*delivery(MESSAGE))
    assert not verify(SECRET, headers, body, now=NOW)
    with pytest.raises(InvalidSignature):
        verify_and_parse(SECRET, headers, body, now=NOW)


def test_another_secret_does_not_verify():
    headers, body = delivery(MESSAGE)
    assert not verify("6a" * 32, headers, body, now=NOW)


def test_a_stale_or_future_timestamp_does_not_verify():
    headers, body = delivery(MESSAGE)
    assert verify(SECRET, headers, body, now=NOW + 300)
    assert not verify(SECRET, headers, body, now=NOW + 301)
    assert not verify(SECRET, headers, body, now=NOW - 301)
    assert verify(SECRET, headers, body, now=NOW + 3600, max_age=3600)


def test_verify_signature_takes_the_parts_directly():
    body = b"{}"
    assert verify_signature(SECRET, "1794500000", sign(SECRET, "1794500000", body), body, now=NOW)


def test_every_event_type_of_the_gateway_has_a_model():
    assert list(EVENT_MODELS) == [
        "LoginUpdated",
        "Connected",
        "Disconnected",
        "LoggedOut",
        "Paused",
        "Resumed",
        "Message",
        "MessageEdited",
        "MessagesDeleted",
        "MessagesRead",
        "Typing",
        "UserStatus",
        "ReactionsChanged",
    ]


def test_a_login_update_carries_the_qr_and_keeps_it_out_of_repr():
    event = parse_event(
        envelope(
            "LoginUpdated",
            {
                "login": {
                    "step": "qr",
                    "method": "qr",
                    "qr": {
                        "image": "data:image/png;base64,iVBORw0KGgo",
                        "link": "tg://login?token=AQIDBAUGBwg",
                        "expiresAt": 1794500030,
                    },
                }
            },
        )
    )

    assert isinstance(event, LoginUpdatedEvent)
    assert event.data.login.qr.link == "tg://login?token=AQIDBAUGBwg"
    assert "AQIDBAUGBwg" not in repr(event)


def test_other_events_parse_from_bytes_str_and_dicts():
    logged_out = envelope("LoggedOut", {"reason": "revoked"})
    paused = envelope("Paused", {"pause": {"reason": "flood", "upstreamCode": "FLOOD_WAIT_220", "since": 1794500000}})
    deleted = envelope("MessagesDeleted", {"chatId": -1001234567890, "messageIds": [41, 42]})

    assert isinstance(parse_event(json.dumps(logged_out).encode()), LoggedOutEvent)
    assert parse_event(json.dumps(logged_out)).data.reason == "revoked"
    assert isinstance(parse_event(paused), PausedEvent)
    assert parse_event(paused).data.pause.upstream_code == "FLOOD_WAIT_220"
    assert parse_event(deleted).data.message_ids == [41, 42]
    assert isinstance(parse_event(deleted), MessagesDeletedEvent)


def test_an_unknown_type_is_refused_by_name():
    with pytest.raises(UnknownEvent):
        parse_event(envelope("SomethingNew", {}))
    with pytest.raises(ValueError):
        parse_event(b"[]")


def test_a_model_refuses_a_body_of_another_type():
    with pytest.raises(ValueError):
        MessageEvent.from_dict(envelope("Paused", {"pause": {"reason": "flood", "upstreamCode": "", "since": 1}}))
