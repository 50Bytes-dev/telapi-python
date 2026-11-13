from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.session_response import SessionResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/session",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SessionResponse | None:
    if response.status_code == 200:
        response_200 = SessionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

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
) -> Response[ErrorResponse | SessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SessionResponse]:
    """The account's Telegram session

     Whether the account is logged in and connected, its Telegram user,
    the login while one runs (or the failed last one) and the pause.
    Once `TELAPI_LIVENESS_INTERVAL` (±20 %) has passed since the client
    connected or the login was last checked, the login is checked with
    Telegram first (`users.getUsers`, waiting at most about 5 s); a login
    Telegram confirms ended is erased and `LoggedOut` follows. The
    login's QR is left out here: it is in `GET /session/login`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SessionResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SessionResponse | None:
    """The account's Telegram session

     Whether the account is logged in and connected, its Telegram user,
    the login while one runs (or the failed last one) and the pause.
    Once `TELAPI_LIVENESS_INTERVAL` (±20 %) has passed since the client
    connected or the login was last checked, the login is checked with
    Telegram first (`users.getUsers`, waiting at most about 5 s); a login
    Telegram confirms ended is erased and `LoggedOut` follows. The
    login's QR is left out here: it is in `GET /session/login`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SessionResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | SessionResponse]:
    """The account's Telegram session

     Whether the account is logged in and connected, its Telegram user,
    the login while one runs (or the failed last one) and the pause.
    Once `TELAPI_LIVENESS_INTERVAL` (±20 %) has passed since the client
    connected or the login was last checked, the login is checked with
    Telegram first (`users.getUsers`, waiting at most about 5 s); a login
    Telegram confirms ended is erased and `LoggedOut` follows. The
    login's QR is left out here: it is in `GET /session/login`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SessionResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | SessionResponse | None:
    """The account's Telegram session

     Whether the account is logged in and connected, its Telegram user,
    the login while one runs (or the failed last one) and the pause.
    Once `TELAPI_LIVENESS_INTERVAL` (±20 %) has passed since the client
    connected or the login was last checked, the login is checked with
    Telegram first (`users.getUsers`, waiting at most about 5 s); a login
    Telegram confirms ended is erased and `LoggedOut` follows. The
    login's QR is left out here: it is in `GET /session/login`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SessionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
