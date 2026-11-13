from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invite_link_request import CreateInviteLinkRequest
from ...models.error_response import ErrorResponse
from ...models.invite_link_response import InviteLinkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chat_id: int,
    *,
    body: CreateInviteLinkRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chats/{chat_id}/invite-link".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | InviteLinkResponse | None:
    if response.status_code == 200:
        response_200 = InviteLinkResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | InviteLinkResponse]:
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
    body: CreateInviteLinkRequest | Unset = UNSET,
) -> Response[ErrorResponse | InviteLinkResponse]:
    """Create an invite link

     A new invite link of a group or channel (`messages.exportChatInvite`); a private chat is
    `invalid_input`. The body may be left out for a link without limits.

    Args:
        chat_id (int):
        body (CreateInviteLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InviteLinkResponse]
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
    body: CreateInviteLinkRequest | Unset = UNSET,
) -> ErrorResponse | InviteLinkResponse | None:
    """Create an invite link

     A new invite link of a group or channel (`messages.exportChatInvite`); a private chat is
    `invalid_input`. The body may be left out for a link without limits.

    Args:
        chat_id (int):
        body (CreateInviteLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InviteLinkResponse
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
    body: CreateInviteLinkRequest | Unset = UNSET,
) -> Response[ErrorResponse | InviteLinkResponse]:
    """Create an invite link

     A new invite link of a group or channel (`messages.exportChatInvite`); a private chat is
    `invalid_input`. The body may be left out for a link without limits.

    Args:
        chat_id (int):
        body (CreateInviteLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | InviteLinkResponse]
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
    body: CreateInviteLinkRequest | Unset = UNSET,
) -> ErrorResponse | InviteLinkResponse | None:
    """Create an invite link

     A new invite link of a group or channel (`messages.exportChatInvite`); a private chat is
    `invalid_input`. The body may be left out for a link without limits.

    Args:
        chat_id (int):
        body (CreateInviteLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | InviteLinkResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed
