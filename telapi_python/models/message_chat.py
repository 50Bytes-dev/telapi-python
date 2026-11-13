from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MessageChat")


@_attrs_define
class MessageChat:
    """The chat of a message. `type`: `user`, `bot`, `group`, `channel`; new values may come. `title` is empty when the
    account has not seen the chat since the gateway started: Telegram sends most private and basic group messages
    without their users and chats.

        Attributes:
            chat_id (int):
            type_ (str):  Example: user.
            title (str):
    """

    chat_id: int
    type_: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = d.pop("type")

        title = d.pop("title")

        message_chat = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
        )

        message_chat.additional_properties = d
        return message_chat

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
