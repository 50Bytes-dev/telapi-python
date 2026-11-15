from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_list_response import ChatListResponse
from ...models.chat_type_filter import ChatTypeFilter
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: list[ChatTypeFilter] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    archived: bool | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params["archived"] = archived

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatListResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ChatListResponse.from_dict(response.json())

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
) -> Response[ChatListResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[ChatTypeFilter] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    archived: bool | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List the chats

     The account's dialogs, most recent first, one page at a time;
    `nextCursor` gives the next page and is absent on the last one.

    Each page is one `messages.getDialogs` call of `limit` dialogs.
    `type` filters the page Telegram gave, so a filtered page may hold
    fewer chats than `limit`, even none, while `nextCursor` goes on:
    follow it until it is absent. Pinned chats come first on the first
    page (give a `limit` of at least the number of pinned chats to see
    them all); later pages leave them out, so none repeats. A chat that
    moves up between two pages (a new message) may appear on both.
    The list ends only when `nextCursor` is absent, which may follow a
    page with no chats; a page shorter than `limit` is not the end
    (Telegram sends short pages in the middle of the list too). Empty
    `limit` or `archived` values count as left out. Cursors of an
    earlier gateway version (`c1.`) are `invalid_input`.

    With `q`, the answer is instead Telegram's search of the account's
    own chats and contacts (`contacts.search`: names, titles and
    usernames, matched as Telegram's search box does; public chats of
    strangers are left out), with their dialog rows, in Telegram's
    order, at most `limit`, in one answer without pages. It searches the
    archive too (each chat says `archived`), so it takes no `cursor`
    and no `archived`. Telegram counts it against the account's lookup
    limits: it is refused while the Telegram user is paused.

    With `ids` (1 to 100 distinct chat ids; it takes no `q`, `cursor`,
    `archived`, `type` or `limit`), the answer is instead those chats,
    as the list shows them, in the order of `ids`, without pages, and
    `missing`, always present: the chats it cannot answer, in the same
    order. A chat the account never saw is missing (`peer_not_found`)
    without a call; the others take one `messages.getPeerDialogs`
    together, never one call per chat. A chat Telegram leaves out of
    its answer is missing (`peer_not_found`); one it returns without a
    dialog (a user never written to) has its counters at zero. When
    Telegram refuses the whole call for one chat it no longer shows the
    account, the chats' objects are read with one call per kind
    (`users.getUsers`, `messages.getChats`, `channels.getChannels`): a
    chat the account left or was banned from comes from its object
    without its dialog row; the others get theirs from a second
    `messages.getPeerDialogs` (or come from their objects when none
    could be set apart or that call is refused too). When Telegram
    refuses a kind's read as a whole for a chat in it (`peer_not_found`
    or `write_forbidden`), its chats are split in halves and each half
    read again, until each refused chat is read alone: that chat is
    missing with its own refusal's `code` and `upstreamCode`, and the
    chats of the halves Telegram answers are answered as usual. At most
    five calls when no kind's read is refused; the halving adds calls
    only on a refusal, at most 1 + 2·k·⌈log₂ n⌉ reads for k refused
    chats among n of a kind and never more than 2n − 1 (one refused
    channel among 100: at most 15; at worst 2 + 199 calls in all). A
    wait, a timeout or any other failure of any call answers the whole
    request, and nothing is retried.

    Args:
        type_ (list[ChatTypeFilter] | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        archived (bool | Unset):
        ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
        archived=archived,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: list[ChatTypeFilter] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    archived: bool | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List the chats

     The account's dialogs, most recent first, one page at a time;
    `nextCursor` gives the next page and is absent on the last one.

    Each page is one `messages.getDialogs` call of `limit` dialogs.
    `type` filters the page Telegram gave, so a filtered page may hold
    fewer chats than `limit`, even none, while `nextCursor` goes on:
    follow it until it is absent. Pinned chats come first on the first
    page (give a `limit` of at least the number of pinned chats to see
    them all); later pages leave them out, so none repeats. A chat that
    moves up between two pages (a new message) may appear on both.
    The list ends only when `nextCursor` is absent, which may follow a
    page with no chats; a page shorter than `limit` is not the end
    (Telegram sends short pages in the middle of the list too). Empty
    `limit` or `archived` values count as left out. Cursors of an
    earlier gateway version (`c1.`) are `invalid_input`.

    With `q`, the answer is instead Telegram's search of the account's
    own chats and contacts (`contacts.search`: names, titles and
    usernames, matched as Telegram's search box does; public chats of
    strangers are left out), with their dialog rows, in Telegram's
    order, at most `limit`, in one answer without pages. It searches the
    archive too (each chat says `archived`), so it takes no `cursor`
    and no `archived`. Telegram counts it against the account's lookup
    limits: it is refused while the Telegram user is paused.

    With `ids` (1 to 100 distinct chat ids; it takes no `q`, `cursor`,
    `archived`, `type` or `limit`), the answer is instead those chats,
    as the list shows them, in the order of `ids`, without pages, and
    `missing`, always present: the chats it cannot answer, in the same
    order. A chat the account never saw is missing (`peer_not_found`)
    without a call; the others take one `messages.getPeerDialogs`
    together, never one call per chat. A chat Telegram leaves out of
    its answer is missing (`peer_not_found`); one it returns without a
    dialog (a user never written to) has its counters at zero. When
    Telegram refuses the whole call for one chat it no longer shows the
    account, the chats' objects are read with one call per kind
    (`users.getUsers`, `messages.getChats`, `channels.getChannels`): a
    chat the account left or was banned from comes from its object
    without its dialog row; the others get theirs from a second
    `messages.getPeerDialogs` (or come from their objects when none
    could be set apart or that call is refused too). When Telegram
    refuses a kind's read as a whole for a chat in it (`peer_not_found`
    or `write_forbidden`), its chats are split in halves and each half
    read again, until each refused chat is read alone: that chat is
    missing with its own refusal's `code` and `upstreamCode`, and the
    chats of the halves Telegram answers are answered as usual. At most
    five calls when no kind's read is refused; the halving adds calls
    only on a refusal, at most 1 + 2·k·⌈log₂ n⌉ reads for k refused
    chats among n of a kind and never more than 2n − 1 (one refused
    channel among 100: at most 15; at worst 2 + 199 calls in all). A
    wait, a timeout or any other failure of any call answers the whole
    request, and nothing is retried.

    Args:
        type_ (list[ChatTypeFilter] | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        archived (bool | Unset):
        ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
        archived=archived,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: list[ChatTypeFilter] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    archived: bool | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
) -> Response[ChatListResponse | ErrorResponse]:
    """List the chats

     The account's dialogs, most recent first, one page at a time;
    `nextCursor` gives the next page and is absent on the last one.

    Each page is one `messages.getDialogs` call of `limit` dialogs.
    `type` filters the page Telegram gave, so a filtered page may hold
    fewer chats than `limit`, even none, while `nextCursor` goes on:
    follow it until it is absent. Pinned chats come first on the first
    page (give a `limit` of at least the number of pinned chats to see
    them all); later pages leave them out, so none repeats. A chat that
    moves up between two pages (a new message) may appear on both.
    The list ends only when `nextCursor` is absent, which may follow a
    page with no chats; a page shorter than `limit` is not the end
    (Telegram sends short pages in the middle of the list too). Empty
    `limit` or `archived` values count as left out. Cursors of an
    earlier gateway version (`c1.`) are `invalid_input`.

    With `q`, the answer is instead Telegram's search of the account's
    own chats and contacts (`contacts.search`: names, titles and
    usernames, matched as Telegram's search box does; public chats of
    strangers are left out), with their dialog rows, in Telegram's
    order, at most `limit`, in one answer without pages. It searches the
    archive too (each chat says `archived`), so it takes no `cursor`
    and no `archived`. Telegram counts it against the account's lookup
    limits: it is refused while the Telegram user is paused.

    With `ids` (1 to 100 distinct chat ids; it takes no `q`, `cursor`,
    `archived`, `type` or `limit`), the answer is instead those chats,
    as the list shows them, in the order of `ids`, without pages, and
    `missing`, always present: the chats it cannot answer, in the same
    order. A chat the account never saw is missing (`peer_not_found`)
    without a call; the others take one `messages.getPeerDialogs`
    together, never one call per chat. A chat Telegram leaves out of
    its answer is missing (`peer_not_found`); one it returns without a
    dialog (a user never written to) has its counters at zero. When
    Telegram refuses the whole call for one chat it no longer shows the
    account, the chats' objects are read with one call per kind
    (`users.getUsers`, `messages.getChats`, `channels.getChannels`): a
    chat the account left or was banned from comes from its object
    without its dialog row; the others get theirs from a second
    `messages.getPeerDialogs` (or come from their objects when none
    could be set apart or that call is refused too). When Telegram
    refuses a kind's read as a whole for a chat in it (`peer_not_found`
    or `write_forbidden`), its chats are split in halves and each half
    read again, until each refused chat is read alone: that chat is
    missing with its own refusal's `code` and `upstreamCode`, and the
    chats of the halves Telegram answers are answered as usual. At most
    five calls when no kind's read is refused; the halving adds calls
    only on a refusal, at most 1 + 2·k·⌈log₂ n⌉ reads for k refused
    chats among n of a kind and never more than 2n − 1 (one refused
    channel among 100: at most 15; at worst 2 + 199 calls in all). A
    wait, a timeout or any other failure of any call answers the whole
    request, and nothing is retried.

    Args:
        type_ (list[ChatTypeFilter] | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        archived (bool | Unset):
        ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        q=q,
        limit=limit,
        cursor=cursor,
        archived=archived,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: list[ChatTypeFilter] | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    archived: bool | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
) -> ChatListResponse | ErrorResponse | None:
    """List the chats

     The account's dialogs, most recent first, one page at a time;
    `nextCursor` gives the next page and is absent on the last one.

    Each page is one `messages.getDialogs` call of `limit` dialogs.
    `type` filters the page Telegram gave, so a filtered page may hold
    fewer chats than `limit`, even none, while `nextCursor` goes on:
    follow it until it is absent. Pinned chats come first on the first
    page (give a `limit` of at least the number of pinned chats to see
    them all); later pages leave them out, so none repeats. A chat that
    moves up between two pages (a new message) may appear on both.
    The list ends only when `nextCursor` is absent, which may follow a
    page with no chats; a page shorter than `limit` is not the end
    (Telegram sends short pages in the middle of the list too). Empty
    `limit` or `archived` values count as left out. Cursors of an
    earlier gateway version (`c1.`) are `invalid_input`.

    With `q`, the answer is instead Telegram's search of the account's
    own chats and contacts (`contacts.search`: names, titles and
    usernames, matched as Telegram's search box does; public chats of
    strangers are left out), with their dialog rows, in Telegram's
    order, at most `limit`, in one answer without pages. It searches the
    archive too (each chat says `archived`), so it takes no `cursor`
    and no `archived`. Telegram counts it against the account's lookup
    limits: it is refused while the Telegram user is paused.

    With `ids` (1 to 100 distinct chat ids; it takes no `q`, `cursor`,
    `archived`, `type` or `limit`), the answer is instead those chats,
    as the list shows them, in the order of `ids`, without pages, and
    `missing`, always present: the chats it cannot answer, in the same
    order. A chat the account never saw is missing (`peer_not_found`)
    without a call; the others take one `messages.getPeerDialogs`
    together, never one call per chat. A chat Telegram leaves out of
    its answer is missing (`peer_not_found`); one it returns without a
    dialog (a user never written to) has its counters at zero. When
    Telegram refuses the whole call for one chat it no longer shows the
    account, the chats' objects are read with one call per kind
    (`users.getUsers`, `messages.getChats`, `channels.getChannels`): a
    chat the account left or was banned from comes from its object
    without its dialog row; the others get theirs from a second
    `messages.getPeerDialogs` (or come from their objects when none
    could be set apart or that call is refused too). When Telegram
    refuses a kind's read as a whole for a chat in it (`peer_not_found`
    or `write_forbidden`), its chats are split in halves and each half
    read again, until each refused chat is read alone: that chat is
    missing with its own refusal's `code` and `upstreamCode`, and the
    chats of the halves Telegram answers are answered as usual. At most
    five calls when no kind's read is refused; the halving adds calls
    only on a refusal, at most 1 + 2·k·⌈log₂ n⌉ reads for k refused
    chats among n of a kind and never more than 2n − 1 (one refused
    channel among 100: at most 15; at worst 2 + 199 calls in all). A
    wait, a timeout or any other failure of any call answers the whole
    request, and nothing is retried.

    Args:
        type_ (list[ChatTypeFilter] | Unset):
        q (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        archived (bool | Unset):
        ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            q=q,
            limit=limit,
            cursor=cursor,
            archived=archived,
            ids=ids,
        )
    ).parsed
