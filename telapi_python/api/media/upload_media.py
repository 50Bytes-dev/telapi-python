from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.upload_media_form import UploadMediaForm
from ...models.upload_media_request import UploadMediaRequest
from ...models.upload_media_response import UploadMediaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadMediaForm | UploadMediaRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/media",
    }

    if isinstance(body, UploadMediaForm):
        _kwargs["files"] = body.to_multipart()

    if isinstance(body, UploadMediaRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UploadMediaResponse | None:
    if response.status_code == 200:
        response_200 = UploadMediaResponse.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse.from_dict(response.json())

        return response_502

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
) -> Response[ErrorResponse | UploadMediaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadMediaForm | UploadMediaRequest | Unset = UNSET,
) -> Response[ErrorResponse | UploadMediaResponse]:
    """Upload a file for messages

     Uploads a file to Telegram once and answers an `attachment` handle
    for `POST /messages`, valid in any chat of the same Telegram user.
    Send it as multipart (`file` and the fields) or as JSON with either
    `url` (fetched by the gateway; internal addresses are refused) or
    `data` (base64 or a base64 data URL). A `photo` (at most
    `TELAPI_PHOTO_MAX_BYTES`) is made anew as a JPEG (at most 2560 px,
    EXIF orientation applied, at most 25 megapixels, sides differing at
    most 20 times); the other types go up as documents (at most
    `TELAPI_MEDIA_MAX_BYTES`) with the attributes of their type. A field
    that does not apply to the type (a photo's `fileName`, a document's
    `duration`) is refused, never ignored. The handle is sealed by the
    gateway: an altered handle, or one of another Telegram user, is
    refused by `POST /messages`.

    Args:
        body (UploadMediaForm):
        body (UploadMediaRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UploadMediaResponse]
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
    body: UploadMediaForm | UploadMediaRequest | Unset = UNSET,
) -> ErrorResponse | UploadMediaResponse | None:
    """Upload a file for messages

     Uploads a file to Telegram once and answers an `attachment` handle
    for `POST /messages`, valid in any chat of the same Telegram user.
    Send it as multipart (`file` and the fields) or as JSON with either
    `url` (fetched by the gateway; internal addresses are refused) or
    `data` (base64 or a base64 data URL). A `photo` (at most
    `TELAPI_PHOTO_MAX_BYTES`) is made anew as a JPEG (at most 2560 px,
    EXIF orientation applied, at most 25 megapixels, sides differing at
    most 20 times); the other types go up as documents (at most
    `TELAPI_MEDIA_MAX_BYTES`) with the attributes of their type. A field
    that does not apply to the type (a photo's `fileName`, a document's
    `duration`) is refused, never ignored. The handle is sealed by the
    gateway: an altered handle, or one of another Telegram user, is
    refused by `POST /messages`.

    Args:
        body (UploadMediaForm):
        body (UploadMediaRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UploadMediaResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadMediaForm | UploadMediaRequest | Unset = UNSET,
) -> Response[ErrorResponse | UploadMediaResponse]:
    """Upload a file for messages

     Uploads a file to Telegram once and answers an `attachment` handle
    for `POST /messages`, valid in any chat of the same Telegram user.
    Send it as multipart (`file` and the fields) or as JSON with either
    `url` (fetched by the gateway; internal addresses are refused) or
    `data` (base64 or a base64 data URL). A `photo` (at most
    `TELAPI_PHOTO_MAX_BYTES`) is made anew as a JPEG (at most 2560 px,
    EXIF orientation applied, at most 25 megapixels, sides differing at
    most 20 times); the other types go up as documents (at most
    `TELAPI_MEDIA_MAX_BYTES`) with the attributes of their type. A field
    that does not apply to the type (a photo's `fileName`, a document's
    `duration`) is refused, never ignored. The handle is sealed by the
    gateway: an altered handle, or one of another Telegram user, is
    refused by `POST /messages`.

    Args:
        body (UploadMediaForm):
        body (UploadMediaRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UploadMediaResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UploadMediaForm | UploadMediaRequest | Unset = UNSET,
) -> ErrorResponse | UploadMediaResponse | None:
    """Upload a file for messages

     Uploads a file to Telegram once and answers an `attachment` handle
    for `POST /messages`, valid in any chat of the same Telegram user.
    Send it as multipart (`file` and the fields) or as JSON with either
    `url` (fetched by the gateway; internal addresses are refused) or
    `data` (base64 or a base64 data URL). A `photo` (at most
    `TELAPI_PHOTO_MAX_BYTES`) is made anew as a JPEG (at most 2560 px,
    EXIF orientation applied, at most 25 megapixels, sides differing at
    most 20 times); the other types go up as documents (at most
    `TELAPI_MEDIA_MAX_BYTES`) with the attributes of their type. A field
    that does not apply to the type (a photo's `fileName`, a document's
    `duration`) is refused, never ignored. The handle is sealed by the
    gateway: an altered handle, or one of another Telegram user, is
    refused by `POST /messages`.

    Args:
        body (UploadMediaForm):
        body (UploadMediaRequest): Exactly one of `url` and `data`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UploadMediaResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
