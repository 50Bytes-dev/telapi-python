import json
from uuid import UUID

import httpx
import pytest

from telapi_python import AuthenticatedClient, Client
from telapi_python.api.admin import create_account, rotate_account_token
from telapi_python.api.chats import get_chat, get_history, list_chats, list_send_as, list_topics
from telapi_python.api.health import get_health
from telapi_python.api.login import start_qr_login, submit_login_code, submit_login_password
from telapi_python.api.media import upload_media
from telapi_python.api.messages import forward_messages, relay_message, send_message
from telapi_python.api.session import connect
from telapi_python.api.webhook import rotate_webhook_secret
from telapi_python.models import (
    AccountTokenResponse,
    ChatBannedRights,
    ChatListResponse,
    ChatResponse,
    ChatTypeFilter,
    CreateAccountRequest,
    CreateAccountResponse,
    ErrorResponse,
    EventType,
    ForwardMessagesRequest,
    HealthResponse,
    LoginResponse,
    MediaUploadType,
    MissingChat,
    MonoforumThread,
    RelayMessageRequest,
    RelayMessageResponse,
    SendAsListResponse,
    SendAsPeer,
    SendMessageRequest,
    SendMessageResponse,
    SubmitLoginCodeRequest,
    SubmitLoginPasswordRequest,
    Topic,
    TopicListResponse,
    UploadMediaForm,
    UploadMediaRequest,
    UploadMediaResponse,
    WebhookSecretResponse,
)
from telapi_python.types import UNSET, File

BASE_URL = "http://telapi.test"


class Recorder:
    """A MockTransport handler that answers one status and body and keeps the requests it got."""

    def __init__(self, status: int, body: dict):
        self.status = status
        self.body = body
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        return httpx.Response(self.status, json=self.body)


def account_client(recorder: Recorder, token: str = "account-token") -> AuthenticatedClient:
    return AuthenticatedClient(base_url=BASE_URL, token=token, httpx_args={"transport": httpx.MockTransport(recorder)})


ACCOUNT = {
    "id": "6f1c2d4e-8a7b-4c3d-9e2f-1a2b3c4d5e6f",
    "name": "sales-1",
    "webhookUrl": "",
    "events": ["All"],
    "proxy": "",
    "usesDefaultProxy": True,
    "loggedIn": False,
    "connected": False,
    "createdAt": 1794500000,
}


def test_a_send_parses_its_answer_and_sends_only_the_given_fields():
    rec = Recorder(
        200, {"success": True, "chatId": -1001234567890, "messageIds": [42], "messageId": 42, "duplicate": False}
    )
    res = send_message.sync(
        client=account_client(rec),
        body=SendMessageRequest(chat_id=-1001234567890, text="Hello!", attachments=["tgm1.abc"], ref="order-1042"),
    )

    assert isinstance(res, SendMessageResponse)
    assert res.message_ids == [42]
    assert res.message_id == 42
    assert res.duplicate is False
    request = rec.requests[0]
    assert request.url.path == "/messages"
    assert json.loads(request.content) == {
        "chatId": -1001234567890,
        "text": "Hello!",
        "attachments": ["tgm1.abc"],
        "ref": "order-1042",
    }


def test_a_forward_goes_to_the_path_chat_with_only_the_given_fields():
    rec = Recorder(
        200, {"success": True, "chatId": -1001234567890, "messageIds": [501, 502], "messageId": 501, "duplicate": False}
    )
    res = forward_messages.sync(
        -1001234567890,
        client=account_client(rec),
        body=ForwardMessagesRequest(from_chat_id=777, message_ids=[10, 11], drop_author=True, ref="batch-1"),
    )

    assert isinstance(res, SendMessageResponse)
    assert res.message_ids == [501, 502]
    request = rec.requests[0]
    assert request.method == "POST"
    assert request.url.path == "/chats/-1001234567890/forward"
    assert json.loads(request.content) == {
        "fromChatId": 777,
        "messageIds": [10, 11],
        "dropAuthor": True,
        "ref": "batch-1",
    }


def test_a_relayed_send_parses_its_answer_and_the_copy_left_in_saved_messages():
    rec = Recorder(
        200,
        {
            "success": True,
            "chatId": -1001234567890,
            "messageIds": [5089],
            "messageId": 5089,
            "duplicate": False,
            "savedMessagesLeft": [6626],
        },
    )
    res = relay_message.sync(
        client=account_client(rec),
        body=RelayMessageRequest(chat_id=-1001234567890, text="Платье", attachments=["tgm1.abc"], ref="product-1042"),
    )

    assert isinstance(res, RelayMessageResponse)
    assert res.message_ids == [5089]
    assert res.saved_messages_left == [6626]
    request = rec.requests[0]
    assert request.url.path == "/messages/relay"
    assert json.loads(request.content) == {
        "chatId": -1001234567890,
        "text": "Платье",
        "attachments": ["tgm1.abc"],
        "ref": "product-1042",
    }


def test_the_target_options_go_under_their_names_on_every_kind_of_send():
    ok = {"success": True, "chatId": -1001234567890, "messageIds": [7], "messageId": 7, "duplicate": False}
    rec = Recorder(200, ok)
    client = account_client(rec)
    send_message.sync(
        client=client,
        body=SendMessageRequest(
            chat_id=-1001234567890, text="Hi", topic_id=42, send_as=-1009876543210, allow_paid_stars=30
        ),
    )
    relay_message.sync(
        client=client, body=RelayMessageRequest(chat_id=-1001234567890, text="Hi", monoforum_peer_id=777000)
    )
    forward_messages.sync(
        -1001234567890,
        client=client,
        body=ForwardMessagesRequest(from_chat_id=777, message_ids=[10], topic_id=1, allow_paid_stars=0),
    )

    assert json.loads(rec.requests[0].content) == {
        "chatId": -1001234567890,
        "text": "Hi",
        "topicId": 42,
        "sendAs": -1009876543210,
        "allowPaidStars": 30,
    }
    assert json.loads(rec.requests[1].content) == {"chatId": -1001234567890, "text": "Hi", "monoforumPeerId": 777000}
    assert json.loads(rec.requests[2].content) == {
        "fromChatId": 777,
        "messageIds": [10],
        "topicId": 1,
        "allowPaidStars": 0,
    }


def test_a_paid_recipient_answers_the_stars_and_the_messages_of_the_call():
    rec = Recorder(
        402,
        {
            "success": False,
            "code": "payment_required",
            "error": "the recipient charges Telegram Stars",
            "upstreamCode": "ALLOW_PAYMENT_REQUIRED",
            "requiredStars": 25,
            "messageCount": 3,
        },
    )
    res = send_message.sync_detailed(
        client=account_client(rec), body=SendMessageRequest(chat_id=1, attachments=["tgm1.a", "tgm1.b", "tgm1.c"])
    )

    assert res.status_code == 402
    assert isinstance(res.parsed, ErrorResponse)
    assert res.parsed.code == "payment_required"
    assert res.parsed.required_stars == 25
    assert res.parsed.message_count == 3
    assert res.parsed.migrated_to_chat_id is UNSET


def test_a_migrated_group_answers_its_supergroup():
    rec = Recorder(
        410,
        {
            "success": False,
            "code": "chat_migrated",
            "error": "the group became a supergroup",
            "migratedToChatId": -1001234567890,
        },
    )
    res = forward_messages.sync(
        -4012345, client=account_client(rec), body=ForwardMessagesRequest(from_chat_id=777, message_ids=[10])
    )

    assert isinstance(res, ErrorResponse)
    assert res.code == "chat_migrated"
    assert res.migrated_to_chat_id == -1001234567890


TOPIC_MESSAGE = {
    "messageId": 120,
    "chatId": -1001234567890,
    "senderId": 777000,
    "out": False,
    "date": 1794500000,
    "text": "В теме",
    "forwarded": False,
    "topicId": 42,
}


def test_the_topics_of_a_forum_come_in_pages():
    rec = Recorder(
        200,
        {
            "success": True,
            "topics": [
                {
                    "topicId": 42,
                    "title": "Заказы",
                    "date": 1794400000,
                    "iconColor": 7322096,
                    "closed": False,
                    "pinned": True,
                    "hidden": False,
                    "my": False,
                    "unreadCount": 2,
                    "canWrite": True,
                    "fromId": 777000,
                    "lastMessage": TOPIC_MESSAGE,
                }
            ],
            "orderByCreateDate": False,
            "nextCursor": "t1.abc",
        },
    )
    res = list_topics.sync(-1001234567890, client=account_client(rec), limit=20, cursor="t1.prev", q="Зак")

    assert isinstance(res, TopicListResponse)
    assert isinstance(res.topics[0], Topic)
    assert res.topics[0].topic_id == 42
    assert res.topics[0].last_message.topic_id == 42
    assert res.topics[0].icon_emoji_id is UNSET
    assert res.threads is UNSET
    assert res.next_cursor == "t1.abc"
    request = rec.requests[0]
    assert request.url.path == "/chats/-1001234567890/topics"
    assert dict(request.url.params) == {"limit": "20", "cursor": "t1.prev", "q": "Зак"}


def test_a_channels_direct_messages_answer_threads():
    rec = Recorder(
        200,
        {
            "success": True,
            "threads": [
                {
                    "monoforumPeerId": 777000,
                    "title": "Анна",
                    "unreadCount": 1,
                    "lastMessage": {
                        **{k: v for k, v in TOPIC_MESSAGE.items() if k != "topicId"},
                        "chatId": -1001234567891,
                        "monoforumPeerId": 777000,
                    },
                }
            ],
        },
    )
    res = list_topics.sync(-1001234567891, client=account_client(rec))

    assert isinstance(res, TopicListResponse)
    assert res.topics is UNSET
    assert isinstance(res.threads[0], MonoforumThread)
    assert res.threads[0].monoforum_peer_id == 777000
    assert res.threads[0].last_message.monoforum_peer_id == 777000
    assert res.threads[0].last_message.topic_id is UNSET
    assert res.next_cursor is UNSET
    assert dict(rec.requests[0].url.params) == {}


def test_the_senders_a_chat_takes_parse_with_their_premium_mark():
    rec = Recorder(
        200,
        {
            "success": True,
            "peers": [
                {"chatId": 123456, "type": "user", "title": "Max", "premiumRequired": False},
                {
                    "chatId": -1009876543210,
                    "type": "channel",
                    "title": "Магазин",
                    "username": "shop",
                    "premiumRequired": True,
                },
            ],
        },
    )
    res = list_send_as.sync(-1001234567890, client=account_client(rec))

    assert isinstance(res, SendAsListResponse)
    assert all(isinstance(p, SendAsPeer) for p in res.peers)
    assert [p.chat_id for p in res.peers] == [123456, -1009876543210]
    assert res.peers[1].premium_required is True
    assert res.peers[0].username is UNSET
    assert rec.requests[0].url.path == "/chats/-1001234567890/send-as"


def test_chats_by_id_go_as_repeated_ids_and_answer_the_missing_ones():
    rec = Recorder(
        200,
        {
            "success": True,
            "chats": [
                {
                    "chatId": -1001234567890,
                    "type": "group",
                    "title": "Покупатели",
                    "canWrite": True,
                    "unreadCount": 0,
                    "pinned": False,
                    "muted": False,
                    "archived": False,
                }
            ],
            "missing": [
                {"chatId": 42, "code": "peer_not_found"},
                {"chatId": -1001111111111, "code": "write_forbidden", "upstreamCode": "CHANNEL_PRIVATE"},
            ],
        },
    )
    res = list_chats.sync(client=account_client(rec), ids=[-1001234567890, 42, -1001111111111])

    assert isinstance(res, ChatListResponse)
    assert res.chats[0].chat_id == -1001234567890
    assert all(isinstance(m, MissingChat) for m in res.missing)
    assert [m.code for m in res.missing] == ["peer_not_found", "write_forbidden"]
    assert res.missing[0].upstream_code is UNSET
    assert res.missing[1].upstream_code == "CHANNEL_PRIVATE"
    params = rec.requests[0].url.params
    assert params.get_list("ids") == ["-1001234567890", "42", "-1001111111111"]


# The 1.2.0 schema gave limit and archived defaults, so every list_chats call sent limit=50&archived=false, and
# the gateway refuses both next to ids or q: a call sends only the params its caller sets.
@pytest.mark.parametrize(
    "kwargs, params",
    [
        ({}, []),
        ({"ids": [-1001234567890, 42]}, [("ids", "-1001234567890"), ("ids", "42")]),
        ({"q": "Покуп"}, [("q", "Покуп")]),
        ({"limit": 20, "archived": True}, [("limit", "20"), ("archived", "true")]),
        ({"archived": False}, [("archived", "false")]),
    ],
)
def test_list_chats_sends_only_the_params_its_caller_sets(kwargs, params):
    rec = Recorder(200, {"success": True, "chats": []})
    res = list_chats.sync(client=account_client(rec), **kwargs)

    assert isinstance(res, ChatListResponse)
    assert rec.requests[0].url.path == "/chats"
    assert rec.requests[0].url.params.multi_items() == params


def test_history_sends_a_limit_only_when_its_caller_sets_one():
    rec = Recorder(200, {"success": True, "messages": []})
    get_history.sync(-1001234567890, client=account_client(rec))
    get_history.sync(-1001234567890, client=account_client(rec), limit=20, offset_id=501)

    assert rec.requests[0].url.path == "/chats/-1001234567890/messages"
    # offsetId keeps its schema default, 0 (from the newest), which the gateway takes with any other param.
    assert dict(rec.requests[0].url.params) == {"offsetId": "0"}
    assert dict(rec.requests[1].url.params) == {"limit": "20", "offsetId": "501"}


RIGHTS = {
    name: False
    for name in (
        "viewMessages sendMessages sendMedia sendStickers sendGifs sendGames sendInline embedLinks sendPolls "
        "changeInfo inviteUsers pinMessages manageTopics sendPhotos sendVideos sendRoundvideos sendAudios "
        "sendVoices sendDocs sendPlain sendReactions editRank manageLinkedPeers"
    ).split()
}


def test_a_chats_traits_and_rights_parse_and_absent_traits_are_unset():
    rec = Recorder(
        200,
        {
            "success": True,
            "chat": {
                "chatId": -1001234567890,
                "type": "group",
                "title": "Форум",
                "canWrite": False,
                "cantWriteReason": "restricted",
                "unreadCount": 0,
                "pinned": False,
                "muted": False,
                "archived": False,
                "forum": True,
                "slowmodeEnabled": True,
                "sendPaidMessagesStars": 10,
                "defaultBannedRights": {**RIGHTS, "sendMessages": True},
                "bannedRights": {**RIGHTS, "sendPhotos": True, "untilDate": 1794600000},
                "slowmodeSeconds": 30,
                "slowmodeNextSendDate": 1794500030,
                "defaultSendAs": -1009876543210,
                "boostsApplied": 1,
                "boostsUnrestrict": 4,
            },
        },
    )
    res = get_chat.sync(-1001234567890, client=account_client(rec))

    assert isinstance(res, ChatResponse)
    chat = res.chat
    assert chat.forum is True
    assert chat.monoforum is UNSET
    assert chat.cant_write_reason == "restricted"
    assert chat.send_paid_messages_stars == 10
    assert isinstance(chat.default_banned_rights, ChatBannedRights)
    assert chat.default_banned_rights.send_messages is True
    assert chat.default_banned_rights.until_date is UNSET
    assert chat.banned_rights.send_photos is True
    assert chat.banned_rights.until_date == 1794600000
    assert chat.default_send_as == -1009876543210
    assert chat.boosts_unrestrict == 4
    assert chat.to_dict()["bannedRights"]["untilDate"] == 1794600000


def test_a_flood_wait_comes_with_retry_after_ms():
    rec = Recorder(
        429,
        {
            "success": False,
            "code": "flood_wait",
            "error": "Telegram asked to wait",
            "retryAfterMs": 37000,
            "upstreamCode": "FLOOD_WAIT_37",
        },
    )
    res = send_message.sync_detailed(client=account_client(rec), body=SendMessageRequest(username="durov", text="Hi"))

    assert res.status_code == 429
    assert isinstance(res.parsed, ErrorResponse)
    assert res.parsed.code == "flood_wait"
    assert res.parsed.retry_after_ms == 37000
    assert res.parsed.upstream_code == "FLOOD_WAIT_37"


def test_a_paused_user_comes_with_its_pause():
    rec = Recorder(
        409,
        {
            "success": False,
            "code": "paused",
            "error": "The Telegram user is paused",
            "pause": {"reason": "flood", "upstreamCode": "FLOOD_WAIT_220", "since": 1794500000, "until": 1794500220},
        },
    )
    res = send_message.sync(client=account_client(rec), body=SendMessageRequest(chat_id=1, text="x"))

    assert isinstance(res, ErrorResponse)
    assert res.pause.reason == "flood"
    assert res.pause.until == 1794500220
    assert res.retry_after_ms is UNSET


def test_rejected_attachments_come_with_their_indexes():
    rec = Recorder(
        422,
        {
            "success": False,
            "code": "attachment_rejected",
            "error": "Telegram refused an attachment",
            "upstreamCode": "MEDIA_EMPTY",
            "rejectedAttachments": [0, 2],
        },
    )
    res = send_message.sync(
        client=account_client(rec), body=SendMessageRequest(chat_id=1, attachments=["tgm1.a", "tgm1.b", "tgm1.c"])
    )

    assert isinstance(res, ErrorResponse)
    assert res.rejected_attachments == [0, 2]


def test_an_error_envelope_on_a_status_the_schema_does_not_list_still_parses():
    rec = Recorder(418, {"success": False, "code": "some_new_code", "error": "text"})
    res = connect.sync(client=account_client(rec))

    assert isinstance(res, ErrorResponse)
    assert res.code == "some_new_code"


def test_a_body_that_is_not_an_envelope_on_an_unlisted_status_is_none():
    rec = Recorder(418, {"teapot": True})
    assert connect.sync(client=account_client(rec)) is None


def test_the_account_token_goes_as_a_bearer_token():
    rec = Recorder(200, {"success": True, "chats": []})
    page = list_chats.sync(
        client=account_client(rec, token="0123abcd"), type_=[ChatTypeFilter.GROUP, ChatTypeFilter.CHANNEL]
    )

    assert page.chats == []
    assert page.next_cursor is UNSET
    request = rec.requests[0]
    assert request.headers["Authorization"] == "Bearer 0123abcd"
    assert request.url.params.get_list("type") == ["group", "channel"]
    assert "limit" not in request.url.params
    assert "archived" not in request.url.params


def test_the_admin_token_goes_as_a_bearer_token_and_the_new_secrets_stay_out_of_repr():
    rec = Recorder(200, {"success": True, "account": ACCOUNT, "token": "a" * 64, "webhookSecret": "b" * 64})
    admin = AuthenticatedClient(
        base_url=BASE_URL, token="admin-token", httpx_args={"transport": httpx.MockTransport(rec)}
    )
    res = create_account.sync(client=admin, body=CreateAccountRequest(name="sales-1", events=[EventType.ALL]))

    assert rec.requests[0].headers["Authorization"] == "Bearer admin-token"
    assert isinstance(res, CreateAccountResponse)
    assert res.token == "a" * 64
    assert res.webhook_secret == "b" * 64
    assert res.account.events == ["All"]
    assert res.account.proxy == ""
    assert res.account.uses_default_proxy is True
    assert "a" * 64 not in repr(res)
    assert "b" * 64 not in repr(res)


def test_a_rotated_token_and_secret_stay_out_of_repr():
    rec = Recorder(200, {"success": True, "token": "c" * 64})
    res = rotate_account_token.sync(UUID(ACCOUNT["id"]), client=account_client(rec, token="admin-token"))
    assert isinstance(res, AccountTokenResponse)
    assert "c" * 64 not in repr(res)

    rec = Recorder(200, {"success": True, "webhookSecret": "d" * 64})
    res = rotate_webhook_secret.sync(client=account_client(rec))
    assert isinstance(res, WebhookSecretResponse)
    assert "d" * 64 not in repr(res)


def test_the_login_code_and_password_stay_out_of_repr_but_go_to_the_gateway():
    code = SubmitLoginCodeRequest(code="91827")
    password = SubmitLoginPasswordRequest(password="correct horse battery staple")
    assert "91827" not in repr(code)
    assert "correct horse" not in repr(password)

    rec = Recorder(
        200, {"success": True, "login": {"step": "password", "password": {"hint": "", "hasRecovery": False}}}
    )
    submit_login_code.sync(client=account_client(rec), body=code)
    submit_login_password.sync(client=account_client(rec), body=password)
    assert json.loads(rec.requests[0].content) == {"code": "91827"}
    assert json.loads(rec.requests[1].content) == {"password": "correct horse battery staple"}


def test_a_qr_login_answers_the_qr_and_keeps_its_link_out_of_repr():
    rec = Recorder(
        200,
        {
            "success": True,
            "login": {
                "step": "qr",
                "method": "qr",
                "startedAt": 1794500000,
                "expiresAt": 1794500300,
                "qr": {
                    "image": "data:image/png;base64,iVBORw0KGgo",
                    "link": "tg://login?token=AQIDBAUGBwg",
                    "expiresAt": 1794500030,
                },
            },
        },
    )
    res = start_qr_login.sync(client=account_client(rec))

    assert isinstance(res, LoginResponse)
    assert res.login.step == "qr"
    assert res.login.qr.link == "tg://login?token=AQIDBAUGBwg"
    assert res.login.failure is UNSET
    assert "AQIDBAUGBwg" not in repr(res)
    assert "iVBORw0KGgo" not in repr(res)


def test_a_client_leaves_its_token_out_of_repr_also_after_a_request():
    rec = Recorder(200, {"success": True, "chats": []})
    client = account_client(rec, token="secret-account-token")
    list_chats.sync(client=client)

    assert "secret-account-token" not in repr(client)


def test_health_takes_no_token_and_parses_the_degraded_answer():
    rec = Recorder(
        503,
        {
            "success": False,
            "status": "degraded",
            "version": "1.0.0",
            "uptimeSeconds": 12,
            "db": False,
            "accounts": 0,
            "connected": 0,
            "goroutines": 8,
            "memAllocMb": 3,
            "code": "db_unavailable",
            "error": "the database does not answer",
        },
    )
    public = Client(base_url=BASE_URL, httpx_args={"transport": httpx.MockTransport(rec)})
    res = get_health.sync(client=public)

    assert "Authorization" not in rec.requests[0].headers
    assert isinstance(res, HealthResponse)
    assert res.status == "degraded"
    assert res.db is False


def test_a_multipart_upload_lets_httpx_set_its_boundary():
    rec = Recorder(200, {"success": True, "attachment": "tgm1.eyJwIjoi", "type": "photo", "size": 183402})
    res = upload_media.sync(
        client=account_client(rec),
        body=UploadMediaForm(
            file=File(payload=b"\xff\xd8\xff", file_name="photo.jpg", mime_type="image/jpeg"),
            type_=MediaUploadType.PHOTO,
        ),
    )

    assert isinstance(res, UploadMediaResponse)
    assert res.attachment == "tgm1.eyJwIjoi"
    request = rec.requests[0]
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert b'name="file"; filename="photo.jpg"' in request.content
    assert b'name="type"' in request.content and b"photo" in request.content


def test_a_json_upload_is_sent_as_json():
    rec = Recorder(422, {"success": False, "code": "fetch_failed", "error": "the url could not be fetched"})
    res = upload_media.sync(
        client=account_client(rec),
        body=UploadMediaRequest(type_=MediaUploadType.PHOTO, url="https://example.com/photo.jpg"),
    )

    assert isinstance(res, ErrorResponse)
    assert res.code == "fetch_failed"
    assert rec.requests[0].headers["Content-Type"] == "application/json"
    assert json.loads(rec.requests[0].content) == {"type": "photo", "url": "https://example.com/photo.jpg"}


@pytest.mark.parametrize("status", [400, 401, 402, 403, 404, 409, 410, 413, 422, 429, 500, 502, 503, 504])
def test_every_error_status_of_a_send_is_an_error_response(status):
    rec = Recorder(status, {"success": False, "code": "some_code", "error": "text"})
    res = send_message.sync(client=account_client(rec), body=SendMessageRequest(chat_id=1, text="x"))

    assert isinstance(res, ErrorResponse)
    assert res.code == "some_code"
