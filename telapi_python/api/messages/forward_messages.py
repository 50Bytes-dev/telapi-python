from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.forward_messages_request import ForwardMessagesRequest
from ...models.send_message_response import SendMessageResponse
from ...types import Response


def _get_kwargs(
    chat_id: int,
    *,
    body: ForwardMessagesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chats/{chat_id}/forward".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SendMessageResponse | None:
    if response.status_code == 200:
        response_200 = SendMessageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse.from_dict(response.json())

        return response_410

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if response.status_code >= 400:
        # telapi-python: every error of the gateway is the ErrorResponse envelope, also on a status the schema does
        # not list for this call.
        try:
            error_body = response.json()
        except ValueError:
            error_body = None
        if (
            isinstance(error_body, dict)
            and error_body.get("success") is False
            and isinstance(error_body.get("code"), str)
        ):
            return ErrorResponse.from_dict(error_body)

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SendMessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    body: ForwardMessagesRequest,
) -> Response[ErrorResponse | SendMessageResponse]:
    """Forward messages

     Forwards 1 to 100 messages of `fromChatId` into this chat
    with one `messages.forwardMessages` call. For Telegram's antispam
    it is a send: a `FLOOD_WAIT` is `429 flood_wait` with
    `retryAfterMs` and holds every send of the Telegram user, and the
    stop signals pause it, exactly as on `POST /messages`. Either chat
    may be the account's own id (Saved Messages). `ref` makes it safe
    to repeat as on `POST /messages` (one `random_id` per message,
    fixed by the `ref`); with `scheduleDate` the copies go into the
    scheduled queue and their ids are ids there. `messageIds` lists the
    new messages in the order of the request's ids, and is empty when
    Telegram's answer did not pair each of them (for example when one
    of the source messages no longer exists).

    Args:
        chat_id (int):
        body (ForwardMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SendMessageResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    body: ForwardMessagesRequest,
) -> ErrorResponse | SendMessageResponse | None:
    """Forward messages

     Forwards 1 to 100 messages of `fromChatId` into this chat
    with one `messages.forwardMessages` call. For Telegram's antispam
    it is a send: a `FLOOD_WAIT` is `429 flood_wait` with
    `retryAfterMs` and holds every send of the Telegram user, and the
    stop signals pause it, exactly as on `POST /messages`. Either chat
    may be the account's own id (Saved Messages). `ref` makes it safe
    to repeat as on `POST /messages` (one `random_id` per message,
    fixed by the `ref`); with `scheduleDate` the copies go into the
    scheduled queue and their ids are ids there. `messageIds` lists the
    new messages in the order of the request's ids, and is empty when
    Telegram's answer did not pair each of them (for example when one
    of the source messages no longer exists).

    Args:
        chat_id (int):
        body (ForwardMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SendMessageResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    body: ForwardMessagesRequest,
) -> Response[ErrorResponse | SendMessageResponse]:
    """Forward messages

     Forwards 1 to 100 messages of `fromChatId` into this chat
    with one `messages.forwardMessages` call. For Telegram's antispam
    it is a send: a `FLOOD_WAIT` is `429 flood_wait` with
    `retryAfterMs` and holds every send of the Telegram user, and the
    stop signals pause it, exactly as on `POST /messages`. Either chat
    may be the account's own id (Saved Messages). `ref` makes it safe
    to repeat as on `POST /messages` (one `random_id` per message,
    fixed by the `ref`); with `scheduleDate` the copies go into the
    scheduled queue and their ids are ids there. `messageIds` lists the
    new messages in the order of the request's ids, and is empty when
    Telegram's answer did not pair each of them (for example when one
    of the source messages no longer exists).

    Args:
        chat_id (int):
        body (ForwardMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SendMessageResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    body: ForwardMessagesRequest,
) -> ErrorResponse | SendMessageResponse | None:
    """Forward messages

     Forwards 1 to 100 messages of `fromChatId` into this chat
    with one `messages.forwardMessages` call. For Telegram's antispam
    it is a send: a `FLOOD_WAIT` is `429 flood_wait` with
    `retryAfterMs` and holds every send of the Telegram user, and the
    stop signals pause it, exactly as on `POST /messages`. Either chat
    may be the account's own id (Saved Messages). `ref` makes it safe
    to repeat as on `POST /messages` (one `random_id` per message,
    fixed by the `ref`); with `scheduleDate` the copies go into the
    scheduled queue and their ids are ids there. `messageIds` lists the
    new messages in the order of the request's ids, and is empty when
    Telegram's answer did not pair each of them (for example when one
    of the source messages no longer exists).

    Args:
        chat_id (int):
        body (ForwardMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SendMessageResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed
