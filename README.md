# telapi-python
A client library for accessing [telapi](https://github.com/50Bytes-dev/telapi), the HTTP gateway for **Telegram user
accounts** (real people's accounts, not bots): it logs into an account by QR code (with the cloud password) or by
phone number and code, keeps the session, sends text, photos, albums, documents, audio and video, edits and deletes
messages, reads history, lists and manages chats and their members, forum topics and a channel's direct messages,
looks up users, and reports what happens in the account as signed webhooks. This package follows telapi's version
(1.2.1).

The package is generated from the gateway's OpenAPI schema (`static/api/spec.yml` in telapi; the gateway serves it at
`/api/spec.yml`, with the Swagger UI at `/api/`). The full contract, with every code and when it comes, is
[`API.md`](https://github.com/50Bytes-dev/telapi/blob/main/API.md). The webhook helpers in `telapi_python.webhooks`
are written by hand.

## Clients
Both tokens go as `Authorization: Bearer <token>`, the default of `AuthenticatedClient`:

```python
import httpx

from telapi_python import AuthenticatedClient, Client

# /admin/*: the admin token (TELAPI_ADMIN_TOKEN)
admin = AuthenticatedClient(base_url="http://localhost:5559", token="<admin token>")

# everything else: the account token from create_account
account = AuthenticatedClient(base_url="http://localhost:5559", token="<account token>", timeout=httpx.Timeout(30.0))

# /health takes no token
public = Client(base_url="http://localhost:5559")
```

One Telegram call takes up to about 10 s and a send with attachments up to 20 s, so httpx's default timeout of 5 s
is too short for the account client. An upload (`api.media.upload_media`) and a download take up to 120 s, and
`add_members` and `lookup_users` up to 240 s: give their client a longer timeout.

## Calls
Every operation is a module under `telapi_python.api.<tag>` with four functions: `sync`, `sync_detailed`, `asyncio`
and `asyncio_detailed`. `sync` returns the parsed body, which for an error is an `ErrorResponse`; `sync_detailed`
returns a `Response` with `status_code` and `parsed`. An error envelope is parsed into `ErrorResponse` on any status
from 400, also on one the schema does not list for that call.

| Module | Call |
|---|---|
| `api.health.get_health` | `GET /health` |
| `api.admin.list_accounts` | `GET /admin/accounts` |
| `api.admin.create_account` | `POST /admin/accounts` |
| `api.admin.get_account` | `GET /admin/accounts/{account_id}` |
| `api.admin.update_account` | `PATCH /admin/accounts/{account_id}` |
| `api.admin.delete_account` | `DELETE /admin/accounts/{account_id}` |
| `api.admin.rotate_account_token` | `POST /admin/accounts/{account_id}/token` |
| `api.session.get_session` | `GET /session` |
| `api.session.connect` | `POST /session/connect` |
| `api.session.disconnect` | `POST /session/disconnect` |
| `api.session.logout` | `POST /session/logout` |
| `api.session.resume` | `POST /session/resume` |
| `api.login.get_login` | `GET /session/login` |
| `api.login.cancel_login` | `DELETE /session/login` |
| `api.login.start_qr_login` | `POST /session/login/qr` |
| `api.login.start_phone_login` | `POST /session/login/phone` |
| `api.login.submit_login_code` | `POST /session/login/code` |
| `api.login.submit_login_password` | `POST /session/login/password` |
| `api.webhook.get_webhook` | `GET /webhook` |
| `api.webhook.set_webhook` | `PUT /webhook` |
| `api.webhook.delete_webhook` | `DELETE /webhook` |
| `api.webhook.rotate_webhook_secret` | `POST /webhook/secret` |
| `api.media.upload_media` | `POST /media` |
| `api.messages.send_message` | `POST /messages` |
| `api.messages.relay_message` | `POST /messages/relay` |
| `api.messages.forward_messages` | `POST /chats/{chat_id}/forward` |
| `api.messages.edit_message` | `PATCH /chats/{chat_id}/messages/{message_id}` |
| `api.messages.delete_messages` | `POST /chats/{chat_id}/messages/delete` |
| `api.chats.list_chats` | `GET /chats` |
| `api.chats.create_chat` | `POST /chats` |
| `api.chats.join_chat` | `POST /chats/join` |
| `api.chats.get_chat` | `GET /chats/{chat_id}` |
| `api.chats.update_chat` | `PATCH /chats/{chat_id}` |
| `api.chats.leave_chat` | `POST /chats/{chat_id}/leave` |
| `api.chats.get_chat_photo` | `GET /chats/{chat_id}/photo` |
| `api.chats.create_invite_link` | `POST /chats/{chat_id}/invite-link` |
| `api.chats.list_members` | `GET /chats/{chat_id}/members` |
| `api.chats.add_members` | `POST /chats/{chat_id}/members` |
| `api.chats.remove_member` | `DELETE /chats/{chat_id}/members/{user_id}` |
| `api.chats.set_member_role` | `PUT /chats/{chat_id}/members/{user_id}/role` |
| `api.chats.list_topics` | `GET /chats/{chat_id}/topics` |
| `api.chats.list_send_as` | `GET /chats/{chat_id}/send-as` |
| `api.chats.get_history` | `GET /chats/{chat_id}/messages` |
| `api.chats.download_media` | `GET /chats/{chat_id}/messages/{message_id}/media` |
| `api.chats.mark_read` | `POST /chats/{chat_id}/read` |
| `api.chats.send_typing` | `POST /chats/{chat_id}/typing` |
| `api.chats.set_reaction` | `PUT /chats/{chat_id}/messages/{message_id}/reaction` |
| `api.users.get_user` | `GET /users/{user_id}` |
| `api.users.lookup_users` | `POST /users/lookup` |
| `api.users.list_contacts` | `GET /contacts` |

Fields the gateway leaves out are `UNSET` (`from telapi_python.types import UNSET`), which is falsy. Errors carry a
machine `code` (`flood_wait`, `paused`, `not_connected`, `timeout`, …); branch on it, never on `error`. New codes,
login steps, chat types and reasons may come: they are plain strings, not enums.

### Create an account

```python
from telapi_python.api.admin import create_account
from telapi_python.models import CreateAccountRequest, EventType

created = create_account.sync(
    client=admin,
    body=CreateAccountRequest(
        name="sales-1",
        webhook_url="https://shop.example/telegram/events",
        events=[EventType.ALL],
    ),
)
store_secret(created.account.id, created.token, created.webhook_secret)  # your code: both are shown only here
```

The token and the webhook secret are left out of the models' `repr`, and so are the login code, the cloud password
and the login QR (its `tg://login` link holds the login token). Store them like passwords.

### Log in by QR, with the cloud password

```python
from telapi_python.api.login import get_login, start_qr_login, submit_login_password
from telapi_python.models import ErrorResponse, SubmitLoginPasswordRequest

res = start_qr_login.sync(client=account)
if isinstance(res, ErrorResponse):
    raise RuntimeError(f"{res.code}: {res.error}")  # already_logged_in, wrong_login_step, login_unavailable, ...

login = res.login
show_qr(login.qr.image)  # your code: a PNG data URL; scan it in Telegram → Settings → Devices → Link Desktop Device

# The QR renews about every 30 s: follow the LoginUpdated webhook, or poll
login = get_login.sync(client=account).login
if login.step == "password":
    print("hint:", login.password.hint)
    submit_login_password.sync(client=account, body=SubmitLoginPasswordRequest(password=ask_password()))
elif login.step == "done":
    print("logged in as", login.tg_user.name)
elif login.step == "failed":
    print("login failed:", login.failure.reason)
```

By phone instead: `api.login.start_phone_login` with `StartPhoneLoginRequest(phone="+79001234567")`, then
`submit_login_code` with `SubmitLoginCodeRequest(code=...)`, and the password if the step asks for it.

### Upload and send

```python
from telapi_python.api.media import upload_media
from telapi_python.api.messages import send_message
from telapi_python.models import ErrorResponse, MediaUploadType, SendMessageRequest, UploadMediaRequest

# Once per Telegram user: the handle works in any of its chats
photo = upload_media.sync(
    client=account, body=UploadMediaRequest(type_=MediaUploadType.PHOTO, url="https://example.com/photo.jpg")
)

res = send_message.sync(
    client=account,
    body=SendMessageRequest(
        chat_id=-1001234567890,  # Bot API style: -100… a supergroup or channel, -id a basic group, id a user
        text="Платье, 1200 ₽",
        attachments=[photo.attachment],  # up to 10 photos make an album
        ref="product-1042",  # your idempotency key: a repeat never sends twice
    ),
)
if isinstance(res, ErrorResponse):
    if res.code == "flood_wait":
        hold_all_sends(res.retry_after_ms)  # your code: Telegram asked this account to wait
    elif res.code == "paused":
        stop_export(res.pause.reason)  # a person resumes it with api.session.resume
    elif res.code == "timeout":
        ...  # the effect is unknown: send again with the same ref
    elif res.code == "attachment_rejected":
        ...  # upload the items of res.rejected_attachments again
else:
    print("sent:", res.message_ids, "duplicate:", res.duplicate)
```

A file goes as multipart with `UploadMediaForm(file=File(payload=..., file_name="photo.jpg"), type_=...)`.

### Posting many messages: `relay_message`

For catalogs, product feeds and any run of posts into one group or channel, use
`relay_message`, not `send_message`. It posts one message through the account's Saved Messages
(sent there, forwarded into the chat without the "Forwarded from" header, the copy deleted),
which held 1000 posts an hour where plain sends drew `FLOOD_WAIT` at 100–300. The gateway does
not pace anything: space the posts yourself and stop for `retry_after_ms` on `flood_wait`.

```python
from telapi_python.api.messages import relay_message
from telapi_python.models import ErrorResponse, RelayMessageRequest

res = relay_message.sync(
    client=account,
    body=RelayMessageRequest(
        chat_id=-1001234567890,
        text="Платье, 1200 ₽",
        attachments=[photo.attachment],  # up to 10 make an album
        ref="product-1042",  # a repeat never posts twice
    ),
)
if isinstance(res, ErrorResponse):
    ...  # the same codes as send_message
elif res.saved_messages_left:
    ...  # the copy could not be deleted from Saved Messages: delete it later
```

### Forward

```python
from telapi_python.api.messages import forward_messages
from telapi_python.models import ForwardMessagesRequest

res = forward_messages.sync(
    -1001234567890,  # into this chat
    client=account,
    body=ForwardMessagesRequest(
        from_chat_id=me.id,  # the account's own id is its Saved Messages
        message_ids=[501, 502, 503],  # 1 to 100, one call
        drop_author=True,  # as the account's own posts, without "Forwarded from"
        ref="batch-17",
    ),
)
```

For Telegram's antispam a forward is a send: the same `flood_wait` and `paused` answers apply.
Address a person by `phone` or `username` instead of `chat_id` until the account has seen the chat.

### Topics, send-as and paid messages

`send_message`, `relay_message` and `forward_messages` take the same target options: `topic_id` (a forum topic, 1 is
General), `monoforum_peer_id` (for a channel's admin: the user's thread in the channel's direct messages), `send_as`
(a chat from `list_send_as`, or the account's own id) and `allow_paid_stars` (the most Telegram Stars the call may
spend on a recipient that charges for messages; absent never pays).

```python
from telapi_python.api.chats import list_send_as, list_topics
from telapi_python.api.messages import send_message
from telapi_python.models import ErrorResponse, SendMessageRequest
from telapi_python.types import UNSET

cursor = UNSET
while True:  # follow next_cursor until it is absent: a page may hold fewer items than limit, even none
    page = list_topics.sync(-1001234567890, client=account, cursor=cursor)
    for topic in page.topics or []:  # a forum answers topics; a channel's direct messages answer threads
        print(topic.topic_id, topic.title, "closed" if topic.closed else "")
    if page.next_cursor is UNSET:
        break
    cursor = page.next_cursor

senders = list_send_as.sync(-1001234567890, client=account).peers  # [] where Telegram has no send-as

res = send_message.sync(
    client=account,
    body=SendMessageRequest(
        chat_id=-1001234567890,
        topic_id=42,
        send_as=senders[0].chat_id,
        text="Hi",
        allow_paid_stars=30,
    ),
)
if isinstance(res, ErrorResponse):
    if res.code == "payment_required":
        ...  # res.required_stars (Telegram's figure) for res.message_count messages: raise allow_paid_stars
    elif res.code == "chat_migrated":
        ...  # the basic group became the supergroup res.migrated_to_chat_id: send there
    elif res.code in ("topic_closed", "topic_invalid", "topic_deleted"):
        ...
```

Messages carry `topic_id` and `monoforum_peer_id`, in history and in the `Message` webhook alike. A `Chat` tells
where these apply: `forum`, `monoforum`, `send_paid_messages_stars`, `slowmode_enabled`, `join_to_send`,
`default_banned_rights` and `banned_rights` (`ChatBannedRights`), and `migrated_to_chat_id`; boolean traits are
`UNSET` unless true. `can_write` with `cant_write_reason` (`migrated`, `chat_closed`, `join_required`, `not_admin`,
`restricted`, …) is what Telegram's objects show, not a promise.

### Chats and history

```python
from telapi_python.api.chats import get_history, list_chats
from telapi_python.models import ChatTypeFilter
from telapi_python.types import UNSET

cursor = UNSET
while True:
    page = list_chats.sync(client=account, type_=[ChatTypeFilter.GROUP, ChatTypeFilter.CHANNEL], cursor=cursor)
    for chat in page.chats:
        print(chat.chat_id, chat.type_, chat.title)
    if page.next_cursor is UNSET:
        break
    cursor = page.next_cursor

# Known chats by id, without pages: those it cannot answer come in page.missing with their code
page = list_chats.sync(client=account, ids=[-1001234567890, 777000])
for missing in page.missing:
    print("missing:", missing.chat_id, missing.code)

history = get_history.sync(-1001234567890, client=account, limit=50)
for m in history.messages:
    print(m.message_id, m.date, m.text)
```

### Webhooks

```python
from telapi_python.models import LoginUpdatedEvent, LoggedOutEvent, MessageEvent, PausedEvent
from telapi_python.webhooks import InvalidSignature, UnknownEvent, verify_and_parse

def handle(headers, raw_body: bytes):  # the raw bytes, before any JSON parsing
    try:
        event = verify_and_parse(webhook_secret, headers, raw_body)
    except InvalidSignature:
        return 401
    except UnknownEvent:
        return 200  # a newer gateway's event: accept and skip
    if seen_before(event.id):  # retries carry the same id
        return 200
    if isinstance(event, MessageEvent):
        print(event.data.chat.title, event.data.message.text, "own" if event.data.message.out else "")
    elif isinstance(event, LoginUpdatedEvent):
        print("login step:", event.data.login.step)
    elif isinstance(event, PausedEvent):
        print("paused:", event.data.pause.reason, event.data.pause.upstream_code)
    elif isinstance(event, LoggedOutEvent):
        print("logged out:", event.data.reason)
    return 200
```

`verify_and_parse` checks `X-Telapi-Signature` (`sha256=` and the HMAC-SHA256 of `timestamp + "." + body` under the
webhook secret, used as the string the gateway showed) and refuses a timestamp more than 5 minutes off
(`max_age=`). `sign`, `verify`, `verify_signature` and `parse_event` are there for the parts.

### Async

```python
from telapi_python.api.session import get_session

async with account as client:
    session = await get_session.asyncio(client=client)
```

## Advanced customizations

`verify_ssl`, `timeout`, `headers`, `httpx_args` and the rest are on the generated `Client` and
`AuthenticatedClient`, see their docstrings. You can also customize the underlying `httpx.Client` or
`httpx.AsyncClient`:

```python
from telapi_python import AuthenticatedClient


def log_response(response):
    request = response.request
    print(f"{request.method} {request.url} - Status {response.status_code}")


account = AuthenticatedClient(
    base_url="http://localhost:5559",
    token="<account token>",
    httpx_args={"event_hooks": {"response": [log_response]}},
)
```

## Regenerate client
After a change of `../telapi/static/api/spec.yml`:

```shell
uv sync --no-install-project
./generate.sh
uv run pytest
```

`generate.sh` runs `openapi-python-client` from the dev group, moves the generated `telapi_client` package to
`telapi_python` and keeps the hand-written `webhooks.py`. The generator is pinned below 0.29: 0.29 writes code that
needs Python 3.11 (`typing.Self`), and the package supports 3.10.

The templates override the generator's in three places:

- `templates/client.py.jinja`: `token` and the headers (which carry the token once a request is made) are left out
  of the clients' `repr`.
- `templates/model.py.jinja`: the fields that carry a secret are left out of the models' `repr`: `token` and
  `webhook_secret` of `CreateAccountResponse`, `AccountTokenResponse` and `WebhookSecretResponse`, `code` of
  `SubmitLoginCodeRequest`, `password` of `SubmitLoginPasswordRequest`, and `image` and `link` of `LoginQr`.
- `templates/endpoint_module.py.jinja`: in `upload_media`, which takes two bodies, the multipart body gets no
  hand-set `Content-Type` (httpx adds its boundary) and `Unset` is imported; and a call that answers
  `ErrorResponse` parses the error envelope on any status from 400.

When the generator is upgraded, copy its new templates and redo these changes.
