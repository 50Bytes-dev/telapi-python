from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.lookup_users_request import LookupUsersRequest
from ...models.lookup_users_response import LookupUsersResponse
from ...types import Response


def _get_kwargs(
    *,
    body: LookupUsersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/lookup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | LookupUsersResponse | None:
    if response.status_code == 200:
        response_200 = LookupUsersResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorResponse.from_dict(response.json())

        return response_413

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

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
) -> Response[ErrorResponse | LookupUsersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupUsersRequest,
) -> Response[ErrorResponse | LookupUsersResponse]:
    """Find users by phone or username

     Looks each phone number and username up, on its own. A phone lookup
    is kept per Telegram user (found 90 days, not found 30 days), so a
    repeat does not call Telegram. Phone numbers come first, then
    usernames. A lookup that failed answers in its own result:
    `invalid_target` for what is no phone number or username,
    `flood_wait` with `retryAfterMs` once Telegram asked to wait (the
    rest are then held without a call), and otherwise the code a single
    call would answer. The whole request has one budget (240 s, under
    the server's write timeout): lookups it leaves no time for answer
    `timeout` without a call and may be asked again. A paused Telegram
    user gets `409 paused` for the whole request, before any lookup.

    Args:
        body (LookupUsersRequest): At least one phone number or username

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LookupUsersResponse]
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
    body: LookupUsersRequest,
) -> ErrorResponse | LookupUsersResponse | None:
    """Find users by phone or username

     Looks each phone number and username up, on its own. A phone lookup
    is kept per Telegram user (found 90 days, not found 30 days), so a
    repeat does not call Telegram. Phone numbers come first, then
    usernames. A lookup that failed answers in its own result:
    `invalid_target` for what is no phone number or username,
    `flood_wait` with `retryAfterMs` once Telegram asked to wait (the
    rest are then held without a call), and otherwise the code a single
    call would answer. The whole request has one budget (240 s, under
    the server's write timeout): lookups it leaves no time for answer
    `timeout` without a call and may be asked again. A paused Telegram
    user gets `409 paused` for the whole request, before any lookup.

    Args:
        body (LookupUsersRequest): At least one phone number or username

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LookupUsersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupUsersRequest,
) -> Response[ErrorResponse | LookupUsersResponse]:
    """Find users by phone or username

     Looks each phone number and username up, on its own. A phone lookup
    is kept per Telegram user (found 90 days, not found 30 days), so a
    repeat does not call Telegram. Phone numbers come first, then
    usernames. A lookup that failed answers in its own result:
    `invalid_target` for what is no phone number or username,
    `flood_wait` with `retryAfterMs` once Telegram asked to wait (the
    rest are then held without a call), and otherwise the code a single
    call would answer. The whole request has one budget (240 s, under
    the server's write timeout): lookups it leaves no time for answer
    `timeout` without a call and may be asked again. A paused Telegram
    user gets `409 paused` for the whole request, before any lookup.

    Args:
        body (LookupUsersRequest): At least one phone number or username

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | LookupUsersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LookupUsersRequest,
) -> ErrorResponse | LookupUsersResponse | None:
    """Find users by phone or username

     Looks each phone number and username up, on its own. A phone lookup
    is kept per Telegram user (found 90 days, not found 30 days), so a
    repeat does not call Telegram. Phone numbers come first, then
    usernames. A lookup that failed answers in its own result:
    `invalid_target` for what is no phone number or username,
    `flood_wait` with `retryAfterMs` once Telegram asked to wait (the
    rest are then held without a call), and otherwise the code a single
    call would answer. The whole request has one budget (240 s, under
    the server's write timeout): lookups it leaves no time for answer
    `timeout` without a call and may be asked again. A paused Telegram
    user gets `409 paused` for the whole request, before any lookup.

    Args:
        body (LookupUsersRequest): At least one phone number or username

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | LookupUsersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
