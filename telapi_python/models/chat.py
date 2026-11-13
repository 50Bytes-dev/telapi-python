from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Chat")


@_attrs_define
class Chat:
    """A chat. `type`: `user`, `bot`, `group` (basic group or supergroup),
    `channel` (broadcast channel); new values may come. `about`,
    `blocked`, `linkedChatId` and `slowmodeSeconds` come only with the
    full view (`GET /chats/{chatId}`, `PATCH /chats/{chatId}`).

    `canWrite` is what Telegram's objects show, not a promise: left,
    removed, deactivated or migrated → `chat_closed`; a broadcast channel
    without the right to post → `not_admin`; a group whose rights (for
    all or for the account) ban sending, the account no admin →
    `restricted`; a deleted account → `deleted_user`; a user the account
    blocked → `blocked` (full view only); a user who takes messages only
    from contacts and Premium users, while the account has no Premium,
    is no mutual contact and has had no message from them →
    `premium_required`.

        Attributes:
            chat_id (int):  Example: -1001234567890.
            type_ (str):  Example: group.
            title (str): The title, or the name of a user or bot Example: Team.
            can_write (bool): The account may send messages here, as far as Telegram's objects show
            unread_count (int):
            pinned (bool):
            muted (bool): Notifications are off now (muted until a time still ahead)
            archived (bool): The chat is in the archive folder
            username (str | Unset):
            user_id (int | Unset): `user` and `bot`: the user id
            members_count (int | Unset): Members of a group or channel, when Telegram tells it
            cant_write_reason (str | Unset): When `canWrite` is false: `chat_closed`, `not_admin`, `restricted`,
                `deleted_user`, `blocked`, `premium_required`; new values may come
            last_message (Message | Unset): A message
            about (str | Unset): The description of a group or channel, the bio of a user
            blocked (bool | Unset): `user` and `bot`, full view: the account blocked this user
            linked_chat_id (int | Unset): The discussion group of a channel, or the channel of a discussion group
            slowmode_seconds (int | Unset):
    """

    chat_id: int
    type_: str
    title: str
    can_write: bool
    unread_count: int
    pinned: bool
    muted: bool
    archived: bool
    username: str | Unset = UNSET
    user_id: int | Unset = UNSET
    members_count: int | Unset = UNSET
    cant_write_reason: str | Unset = UNSET
    last_message: Message | Unset = UNSET
    about: str | Unset = UNSET
    blocked: bool | Unset = UNSET
    linked_chat_id: int | Unset = UNSET
    slowmode_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_

        title = self.title

        can_write = self.can_write

        unread_count = self.unread_count

        pinned = self.pinned

        muted = self.muted

        archived = self.archived

        username = self.username

        user_id = self.user_id

        members_count = self.members_count

        cant_write_reason = self.cant_write_reason

        last_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        about = self.about

        blocked = self.blocked

        linked_chat_id = self.linked_chat_id

        slowmode_seconds = self.slowmode_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
                "canWrite": can_write,
                "unreadCount": unread_count,
                "pinned": pinned,
                "muted": muted,
                "archived": archived,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if cant_write_reason is not UNSET:
            field_dict["cantWriteReason"] = cant_write_reason
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if about is not UNSET:
            field_dict["about"] = about
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if linked_chat_id is not UNSET:
            field_dict["linkedChatId"] = linked_chat_id
        if slowmode_seconds is not UNSET:
            field_dict["slowmodeSeconds"] = slowmode_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = d.pop("type")

        title = d.pop("title")

        can_write = d.pop("canWrite")

        unread_count = d.pop("unreadCount")

        pinned = d.pop("pinned")

        muted = d.pop("muted")

        archived = d.pop("archived")

        username = d.pop("username", UNSET)

        user_id = d.pop("userId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        cant_write_reason = d.pop("cantWriteReason", UNSET)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Message | Unset
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = Message.from_dict(_last_message)

        about = d.pop("about", UNSET)

        blocked = d.pop("blocked", UNSET)

        linked_chat_id = d.pop("linkedChatId", UNSET)

        slowmode_seconds = d.pop("slowmodeSeconds", UNSET)

        chat = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
            can_write=can_write,
            unread_count=unread_count,
            pinned=pinned,
            muted=muted,
            archived=archived,
            username=username,
            user_id=user_id,
            members_count=members_count,
            cant_write_reason=cant_write_reason,
            last_message=last_message,
            about=about,
            blocked=blocked,
            linked_chat_id=linked_chat_id,
            slowmode_seconds=slowmode_seconds,
        )

        chat.additional_properties = d
        return chat

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
