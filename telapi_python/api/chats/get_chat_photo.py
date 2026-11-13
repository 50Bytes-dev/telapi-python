from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    chat_id: int,
    *,
    big: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["big"] = big

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats/{chat_id}/photo".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorResponse | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[ErrorResponse | File]:
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
    big: bool | Unset = False,
) -> Response[ErrorResponse | File]:
    """The chat's photo

     The current photo of the chat (a user's or bot's profile photo for
    a private chat) as a JPEG. The chat is read for its photo
    (`users.getUsers`, `messages.getChats` or `channels.getChannels`),
    then the photo is downloaded (`upload.getFile`) and answered whole;
    over `TELAPI_MEDIA_MAX_BYTES` it is `422 media_too_large`.

    Args:
        chat_id (int):
        big (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        big=big,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    big: bool | Unset = False,
) -> ErrorResponse | File | None:
    """The chat's photo

     The current photo of the chat (a user's or bot's profile photo for
    a private chat) as a JPEG. The chat is read for its photo
    (`users.getUsers`, `messages.getChats` or `channels.getChannels`),
    then the photo is downloaded (`upload.getFile`) and answered whole;
    over `TELAPI_MEDIA_MAX_BYTES` it is `422 media_too_large`.

    Args:
        chat_id (int):
        big (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        big=big,
    ).parsed


async def asyncio_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    big: bool | Unset = False,
) -> Response[ErrorResponse | File]:
    """The chat's photo

     The current photo of the chat (a user's or bot's profile photo for
    a private chat) as a JPEG. The chat is read for its photo
    (`users.getUsers`, `messages.getChats` or `channels.getChannels`),
    then the photo is downloaded (`upload.getFile`) and answered whole;
    over `TELAPI_MEDIA_MAX_BYTES` it is `422 media_too_large`.

    Args:
        chat_id (int):
        big (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | File]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        big=big,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    big: bool | Unset = False,
) -> ErrorResponse | File | None:
    """The chat's photo

     The current photo of the chat (a user's or bot's profile photo for
    a private chat) as a JPEG. The chat is read for its photo
    (`users.getUsers`, `messages.getChats` or `channels.getChannels`),
    then the photo is downloaded (`upload.getFile`) and answered whole;
    over `TELAPI_MEDIA_MAX_BYTES` it is `422 media_too_large`.

    Args:
        chat_id (int):
        big (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | File
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            big=big,
        )
    ).parsed
