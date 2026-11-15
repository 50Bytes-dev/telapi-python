from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """A topic of a forum supergroup. `topicId` is the id of the message
    that opened it and the value a send's `topicId` takes; General is
    `1`.

    `canWrite` is what Telegram's objects show, not a promise: the
    account may write to the forum at all (the chat's own `canWrite`),
    and the topic is open, or the account opened it, or it is the
    forum's creator or an admin who manages topics.

        Attributes:
            topic_id (int):  Example: 1.
            title (str):  Example: General.
            date (int): Unix seconds when the topic was opened
            icon_color (int): The RGB color of the fallback icon
            closed (bool): Only the topic's author, the creator and admins who manage topics may post
            pinned (bool):
            hidden (bool): General only, hidden from the topic list of the apps
            my (bool): The account opened the topic
            unread_count (int):
            can_write (bool): The account may send to this topic, as far as Telegram's objects show
            from_id (int | Unset): The chat id of whoever opened the topic (a user, or a chat for an anonymous admin)
            icon_emoji_id (str | Unset): The custom emoji of the icon, **as a decimal string**
            last_message (Message | Unset): A message
    """

    topic_id: int
    title: str
    date: int
    icon_color: int
    closed: bool
    pinned: bool
    hidden: bool
    my: bool
    unread_count: int
    can_write: bool
    from_id: int | Unset = UNSET
    icon_emoji_id: str | Unset = UNSET
    last_message: Message | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic_id = self.topic_id

        title = self.title

        date = self.date

        icon_color = self.icon_color

        closed = self.closed

        pinned = self.pinned

        hidden = self.hidden

        my = self.my

        unread_count = self.unread_count

        can_write = self.can_write

        from_id = self.from_id

        icon_emoji_id = self.icon_emoji_id

        last_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topicId": topic_id,
                "title": title,
                "date": date,
                "iconColor": icon_color,
                "closed": closed,
                "pinned": pinned,
                "hidden": hidden,
                "my": my,
                "unreadCount": unread_count,
                "canWrite": can_write,
            }
        )
        if from_id is not UNSET:
            field_dict["fromId"] = from_id
        if icon_emoji_id is not UNSET:
            field_dict["iconEmojiId"] = icon_emoji_id
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        topic_id = d.pop("topicId")

        title = d.pop("title")

        date = d.pop("date")

        icon_color = d.pop("iconColor")

        closed = d.pop("closed")

        pinned = d.pop("pinned")

        hidden = d.pop("hidden")

        my = d.pop("my")

        unread_count = d.pop("unreadCount")

        can_write = d.pop("canWrite")

        from_id = d.pop("fromId", UNSET)

        icon_emoji_id = d.pop("iconEmojiId", UNSET)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Message | Unset
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = Message.from_dict(_last_message)

        topic = cls(
            topic_id=topic_id,
            title=title,
            date=date,
            icon_color=icon_color,
            closed=closed,
            pinned=pinned,
            hidden=hidden,
            my=my,
            unread_count=unread_count,
            can_write=can_write,
            from_id=from_id,
            icon_emoji_id=icon_emoji_id,
            last_message=last_message,
        )

        topic.additional_properties = d
        return topic

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
