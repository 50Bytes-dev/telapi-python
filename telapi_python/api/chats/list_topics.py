from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.topic_list_response import TopicListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chat_id: int,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats/{chat_id}/topics".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TopicListResponse | None:
    if response.status_code == 200:
        response_200 = TopicListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | TopicListResponse]:
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ErrorResponse | TopicListResponse]:
    """List the topics

     The topics of a forum supergroup (`messages.getForumTopics`), or the
    threads of a channel's direct messages, one per user who wrote
    (`messages.getSavedDialogs` of the monoforum, for the channel's
    admins). A forum answers `topics` and `orderByCreateDate`; a
    monoforum answers `threads`. Any other chat is `400 invalid_input`:
    a user, bot or basic group without a call, a supergroup or channel
    that is neither as the account last saw it. Topics of a private chat
    with a bot (bot forums) are not supported.

    One page is one Telegram call of `limit` items; `nextCursor` gives
    the next page and is absent on the last one. Follow it until it is
    absent: a page may hold fewer items than `limit`, even none. Pinned
    topics (General among them, when pinned) come first on the first
    page, out of the date order. The forum orders the rest by last
    message, or by creation when `orderByCreateDate` is true; the
    cursor goes on from the page's oldest unpinned topic, so pinned
    topics do not move it, and it only moves on: a topic a later page
    gives again never moves it back, and a later page with no topic
    past it ends the list, as does reaching the number of topics
    Telegram counted on the first page. Deleted topics are left out. A
    cursor is opaque (`t1.…`) and belongs to its chat; give the same
    `q` with it.

    A chat the account never saw is `404 peer_not_found` without a call.
    A channel it saw only in someone's message, or not since a restart,
    is read first (`channels.getChannels`). A read: it goes on while the
    Telegram user is paused.

    Args:
        chat_id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TopicListResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        limit=limit,
        cursor=cursor,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ErrorResponse | TopicListResponse | None:
    """List the topics

     The topics of a forum supergroup (`messages.getForumTopics`), or the
    threads of a channel's direct messages, one per user who wrote
    (`messages.getSavedDialogs` of the monoforum, for the channel's
    admins). A forum answers `topics` and `orderByCreateDate`; a
    monoforum answers `threads`. Any other chat is `400 invalid_input`:
    a user, bot or basic group without a call, a supergroup or channel
    that is neither as the account last saw it. Topics of a private chat
    with a bot (bot forums) are not supported.

    One page is one Telegram call of `limit` items; `nextCursor` gives
    the next page and is absent on the last one. Follow it until it is
    absent: a page may hold fewer items than `limit`, even none. Pinned
    topics (General among them, when pinned) come first on the first
    page, out of the date order. The forum orders the rest by last
    message, or by creation when `orderByCreateDate` is true; the
    cursor goes on from the page's oldest unpinned topic, so pinned
    topics do not move it, and it only moves on: a topic a later page
    gives again never moves it back, and a later page with no topic
    past it ends the list, as does reaching the number of topics
    Telegram counted on the first page. Deleted topics are left out. A
    cursor is opaque (`t1.…`) and belongs to its chat; give the same
    `q` with it.

    A chat the account never saw is `404 peer_not_found` without a call.
    A channel it saw only in someone's message, or not since a restart,
    is read first (`channels.getChannels`). A read: it goes on while the
    Telegram user is paused.

    Args:
        chat_id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TopicListResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        limit=limit,
        cursor=cursor,
        q=q,
    ).parsed


async def asyncio_detailed(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[ErrorResponse | TopicListResponse]:
    """List the topics

     The topics of a forum supergroup (`messages.getForumTopics`), or the
    threads of a channel's direct messages, one per user who wrote
    (`messages.getSavedDialogs` of the monoforum, for the channel's
    admins). A forum answers `topics` and `orderByCreateDate`; a
    monoforum answers `threads`. Any other chat is `400 invalid_input`:
    a user, bot or basic group without a call, a supergroup or channel
    that is neither as the account last saw it. Topics of a private chat
    with a bot (bot forums) are not supported.

    One page is one Telegram call of `limit` items; `nextCursor` gives
    the next page and is absent on the last one. Follow it until it is
    absent: a page may hold fewer items than `limit`, even none. Pinned
    topics (General among them, when pinned) come first on the first
    page, out of the date order. The forum orders the rest by last
    message, or by creation when `orderByCreateDate` is true; the
    cursor goes on from the page's oldest unpinned topic, so pinned
    topics do not move it, and it only moves on: a topic a later page
    gives again never moves it back, and a later page with no topic
    past it ends the list, as does reaching the number of topics
    Telegram counted on the first page. Deleted topics are left out. A
    cursor is opaque (`t1.…`) and belongs to its chat; give the same
    `q` with it.

    A chat the account never saw is `404 peer_not_found` without a call.
    A channel it saw only in someone's message, or not since a restart,
    is read first (`channels.getChannels`). A read: it goes on while the
    Telegram user is paused.

    Args:
        chat_id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TopicListResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        limit=limit,
        cursor=cursor,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> ErrorResponse | TopicListResponse | None:
    """List the topics

     The topics of a forum supergroup (`messages.getForumTopics`), or the
    threads of a channel's direct messages, one per user who wrote
    (`messages.getSavedDialogs` of the monoforum, for the channel's
    admins). A forum answers `topics` and `orderByCreateDate`; a
    monoforum answers `threads`. Any other chat is `400 invalid_input`:
    a user, bot or basic group without a call, a supergroup or channel
    that is neither as the account last saw it. Topics of a private chat
    with a bot (bot forums) are not supported.

    One page is one Telegram call of `limit` items; `nextCursor` gives
    the next page and is absent on the last one. Follow it until it is
    absent: a page may hold fewer items than `limit`, even none. Pinned
    topics (General among them, when pinned) come first on the first
    page, out of the date order. The forum orders the rest by last
    message, or by creation when `orderByCreateDate` is true; the
    cursor goes on from the page's oldest unpinned topic, so pinned
    topics do not move it, and it only moves on: a topic a later page
    gives again never moves it back, and a later page with no topic
    past it ends the list, as does reaching the number of topics
    Telegram counted on the first page. Deleted topics are left out. A
    cursor is opaque (`t1.…`) and belongs to its chat; give the same
    `q` with it.

    A chat the account never saw is `404 peer_not_found` without a call.
    A channel it saw only in someone's message, or not since a restart,
    is read first (`channels.getChannels`). A read: it goes on while the
    Telegram user is paused.

    Args:
        chat_id (int):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        q (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TopicListResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            limit=limit,
            cursor=cursor,
            q=q,
        )
    ).parsed
