from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.relay_message_request import RelayMessageRequest
from ...models.relay_message_response import RelayMessageResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RelayMessageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/relay",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RelayMessageResponse | None:
    if response.status_code == 200:
        response_200 = RelayMessageResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | RelayMessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RelayMessageRequest,
) -> Response[ErrorResponse | RelayMessageResponse]:
    r"""Send a message through Saved Messages (for bulk posting)

     **The method to use for posting many messages (catalogs, product
    feeds) into a group or channel.** It sends one message, like
    `POST /messages`, in three steps: the message goes into the
    account's Saved Messages, is forwarded from there into the chat
    without its author (no \"Forwarded from\" header; photos, captions
    and albums stay as they are), and its copy in Saved Messages is
    deleted. On a fresh account plain sends into one chat drew
    `FLOOD_WAIT` at 100 to 300 posts an hour; relayed sends held 1000
    an hour, evenly paced, with no wait. Telegram documents neither.

    The gateway adds no pacing: the caller spaces the messages. A
    `FLOOD_WAIT` on any step is answered at once as `429` with
    `retryAfterMs`, and the stop signals pause the user, as for
    `POST /messages`. Address the chat by `chatId`, `phone` or
    `username`; the account's own Saved Messages is no target.
    `replyTo`, `noWebpage` and `scheduleDate` are not taken: a forward
    cannot carry them (a link preview of the text is kept).

    The `ref` fixes the forward's `random_id`s: a repeat whose ids are
    known is answered without a call, and any other repeat makes a new
    copy whose forward Telegram drops if it already has it
    (`duplicate: true`). The copy is deleted whatever the forward did;
    when deleting it fails (or a pause stops it), the answer, success
    or error, names it in `savedMessagesLeft`. The copy causes no
    webhook event: neither its `Message` nor its `MessagesDeleted`.

    Args:
        body (RelayMessageRequest): Exactly one of `chatId`, `phone` and `username`; `text`,
            `attachments` or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RelayMessageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RelayMessageRequest,
) -> ErrorResponse | RelayMessageResponse | None:
    r"""Send a message through Saved Messages (for bulk posting)

     **The method to use for posting many messages (catalogs, product
    feeds) into a group or channel.** It sends one message, like
    `POST /messages`, in three steps: the message goes into the
    account's Saved Messages, is forwarded from there into the chat
    without its author (no \"Forwarded from\" header; photos, captions
    and albums stay as they are), and its copy in Saved Messages is
    deleted. On a fresh account plain sends into one chat drew
    `FLOOD_WAIT` at 100 to 300 posts an hour; relayed sends held 1000
    an hour, evenly paced, with no wait. Telegram documents neither.

    The gateway adds no pacing: the caller spaces the messages. A
    `FLOOD_WAIT` on any step is answered at once as `429` with
    `retryAfterMs`, and the stop signals pause the user, as for
    `POST /messages`. Address the chat by `chatId`, `phone` or
    `username`; the account's own Saved Messages is no target.
    `replyTo`, `noWebpage` and `scheduleDate` are not taken: a forward
    cannot carry them (a link preview of the text is kept).

    The `ref` fixes the forward's `random_id`s: a repeat whose ids are
    known is answered without a call, and any other repeat makes a new
    copy whose forward Telegram drops if it already has it
    (`duplicate: true`). The copy is deleted whatever the forward did;
    when deleting it fails (or a pause stops it), the answer, success
    or error, names it in `savedMessagesLeft`. The copy causes no
    webhook event: neither its `Message` nor its `MessagesDeleted`.

    Args:
        body (RelayMessageRequest): Exactly one of `chatId`, `phone` and `username`; `text`,
            `attachments` or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RelayMessageResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RelayMessageRequest,
) -> Response[ErrorResponse | RelayMessageResponse]:
    r"""Send a message through Saved Messages (for bulk posting)

     **The method to use for posting many messages (catalogs, product
    feeds) into a group or channel.** It sends one message, like
    `POST /messages`, in three steps: the message goes into the
    account's Saved Messages, is forwarded from there into the chat
    without its author (no \"Forwarded from\" header; photos, captions
    and albums stay as they are), and its copy in Saved Messages is
    deleted. On a fresh account plain sends into one chat drew
    `FLOOD_WAIT` at 100 to 300 posts an hour; relayed sends held 1000
    an hour, evenly paced, with no wait. Telegram documents neither.

    The gateway adds no pacing: the caller spaces the messages. A
    `FLOOD_WAIT` on any step is answered at once as `429` with
    `retryAfterMs`, and the stop signals pause the user, as for
    `POST /messages`. Address the chat by `chatId`, `phone` or
    `username`; the account's own Saved Messages is no target.
    `replyTo`, `noWebpage` and `scheduleDate` are not taken: a forward
    cannot carry them (a link preview of the text is kept).

    The `ref` fixes the forward's `random_id`s: a repeat whose ids are
    known is answered without a call, and any other repeat makes a new
    copy whose forward Telegram drops if it already has it
    (`duplicate: true`). The copy is deleted whatever the forward did;
    when deleting it fails (or a pause stops it), the answer, success
    or error, names it in `savedMessagesLeft`. The copy causes no
    webhook event: neither its `Message` nor its `MessagesDeleted`.

    Args:
        body (RelayMessageRequest): Exactly one of `chatId`, `phone` and `username`; `text`,
            `attachments` or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RelayMessageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RelayMessageRequest,
) -> ErrorResponse | RelayMessageResponse | None:
    r"""Send a message through Saved Messages (for bulk posting)

     **The method to use for posting many messages (catalogs, product
    feeds) into a group or channel.** It sends one message, like
    `POST /messages`, in three steps: the message goes into the
    account's Saved Messages, is forwarded from there into the chat
    without its author (no \"Forwarded from\" header; photos, captions
    and albums stay as they are), and its copy in Saved Messages is
    deleted. On a fresh account plain sends into one chat drew
    `FLOOD_WAIT` at 100 to 300 posts an hour; relayed sends held 1000
    an hour, evenly paced, with no wait. Telegram documents neither.

    The gateway adds no pacing: the caller spaces the messages. A
    `FLOOD_WAIT` on any step is answered at once as `429` with
    `retryAfterMs`, and the stop signals pause the user, as for
    `POST /messages`. Address the chat by `chatId`, `phone` or
    `username`; the account's own Saved Messages is no target.
    `replyTo`, `noWebpage` and `scheduleDate` are not taken: a forward
    cannot carry them (a link preview of the text is kept).

    The `ref` fixes the forward's `random_id`s: a repeat whose ids are
    known is answered without a call, and any other repeat makes a new
    copy whose forward Telegram drops if it already has it
    (`duplicate: true`). The copy is deleted whatever the forward did;
    when deleting it fails (or a pause stops it), the answer, success
    or error, names it in `savedMessagesLeft`. The copy causes no
    webhook event: neither its `Message` nor its `MessagesDeleted`.

    Args:
        body (RelayMessageRequest): Exactly one of `chatId`, `phone` and `username`; `text`,
            `attachments` or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RelayMessageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
