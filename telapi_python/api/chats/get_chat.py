from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_response import ChatResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    chat_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats/{chat_id}".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

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
) -> Response[ChatResponse | ErrorResponse]:
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
) -> Response[ChatResponse | ErrorResponse]:
    """Get a chat

     The chat's dialog row (`messages.getPeerDialogs`) with its full
    information (`users.getFullUser`, `messages.getFullChat` or
    `channels.getFullChannel`): `about`, `membersCount`, `linkedChatId`,
    `slowmodeSeconds`, `slowmodeNextSendDate`, `migratedFromChatId`,
    `defaultSendAs`, `boostsApplied` and `boostsUnrestrict` for a group
    or channel; `blocked`, `noforwards`, `noforwardsByMe` and
    `noforwardsByPeer` for a user or bot. In the full view
    `sendPaidMessagesStars` is what this account pays, and `canWrite`
    counts the account's boosts. A user the account has no dialog with
    has the row's counters at zero. A chat id the account never saw is
    `404 peer_not_found` without a call.

    Args:
        chat_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: int,
    *,
    client: AuthenticatedClient,
) -> ChatResponse | ErrorResponse | None:
    """Get a chat

     The chat's dialog row (`messages.getPeerDialogs`) with its full
    information (`users.getFullUser`, `messages.getFullChat` or
    `channels.getFullChannel`): `about`, `membersCount`, `linkedChatId`,
    `slowmodeSeconds`, `slowmodeNextSendDate`, `migratedFromChatId`,
    `defaultSendAs`, `boostsApplied` and `boostsUnrestrict` for a group
    or channel; `blocked`, `noforwards`, `noforwardsByMe` and
    `noforwardsByPeer` for a user or bot. In the full view
    `sendPaidMessagesStars` is what this account pays, and `canWrite`
    counts the account's boosts. A user the account has no dialog with
    has the row's counters at zero. A chat id the account never saw is
    `404 peer_not_found` without a call.

    Args:
        chat_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatResponse | ErrorResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ChatResponse | ErrorResponse]:
    """Get a chat

     The chat's dialog row (`messages.getPeerDialogs`) with its full
    information (`users.getFullUser`, `messages.getFullChat` or
    `channels.getFullChannel`): `about`, `membersCount`, `linkedChatId`,
    `slowmodeSeconds`, `slowmodeNextSendDate`, `migratedFromChatId`,
    `defaultSendAs`, `boostsApplied` and `boostsUnrestrict` for a group
    or channel; `blocked`, `noforwards`, `noforwardsByMe` and
    `noforwardsByPeer` for a user or bot. In the full view
    `sendPaidMessagesStars` is what this account pays, and `canWrite`
    counts the account's boosts. A user the account has no dialog with
    has the row's counters at zero. A chat id the account never saw is
    `404 peer_not_found` without a call.

    Args:
        chat_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: int,
    *,
    client: AuthenticatedClient,
) -> ChatResponse | ErrorResponse | None:
    """Get a chat

     The chat's dialog row (`messages.getPeerDialogs`) with its full
    information (`users.getFullUser`, `messages.getFullChat` or
    `channels.getFullChannel`): `about`, `membersCount`, `linkedChatId`,
    `slowmodeSeconds`, `slowmodeNextSendDate`, `migratedFromChatId`,
    `defaultSendAs`, `boostsApplied` and `boostsUnrestrict` for a group
    or channel; `blocked`, `noforwards`, `noforwardsByMe` and
    `noforwardsByPeer` for a user or bot. In the full view
    `sendPaidMessagesStars` is what this account pays, and `canWrite`
    counts the account's boosts. A user the account has no dialog with
    has the row's counters at zero. A chat id the account never saw is
    `404 peer_not_found` without a call.

    Args:
        chat_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
        )
    ).parsed
