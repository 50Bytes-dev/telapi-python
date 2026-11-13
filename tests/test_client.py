import json
from uuid import UUID

import httpx
import pytest

from telapi_python import AuthenticatedClient, Client
from telapi_python.api.admin import create_account, rotate_account_token
from telapi_python.api.chats import list_chats
from telapi_python.api.health import get_health
from telapi_python.api.login import start_qr_login, submit_login_code, submit_login_password
from telapi_python.api.media import upload_media
from telapi_python.api.messages import forward_messages, relay_message, send_message
from telapi_python.api.session import connect
from telapi_python.api.webhook import rotate_webhook_secret
from telapi_python.models import (
    AccountTokenResponse,
    ChatTypeFilter,
    CreateAccountRequest,
    CreateAccountResponse,
    ErrorResponse,
    EventType,
    ForwardMessagesRequest,
    HealthResponse,
    LoginResponse,
    MediaUploadType,
    RelayMessageRequest,
    RelayMessageResponse,
    SendMessageRequest,
    SendMessageResponse,
    SubmitLoginCodeRequest,
    SubmitLoginPasswordRequest,
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
    assert request.url.params["limit"] == "50"


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


@pytest.mark.parametrize("status", [400, 401, 403, 404, 409, 413, 422, 429, 500, 502, 503, 504])
def test_every_error_status_of_a_send_is_an_error_response(status):
    rec = Recorder(status, {"success": False, "code": "some_code", "error": "text"})
    res = send_message.sync(client=account_client(rec), body=SendMessageRequest(chat_id=1, text="x"))

    assert isinstance(res, ErrorResponse)
    assert res.code == "some_code"
