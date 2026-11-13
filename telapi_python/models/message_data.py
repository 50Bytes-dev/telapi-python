from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message
    from ..models.message_chat import MessageChat
    from ..models.message_sender import MessageSender


T = TypeVar("T", bound="MessageData")


@_attrs_define
class MessageData:
    """
    Attributes:
        message (Message): A message
        chat (MessageChat): The chat of a message. `type`: `user`, `bot`, `group`, `channel`; new values may come.
            `title` is empty when the account has not seen the chat since the gateway started: Telegram sends most private
            and basic group messages without their users and chats.
        sender (MessageSender | Unset): The user who sent a message; `name` is empty when the account has not seen the
            user since the gateway started (see `MessageChat`)
    """

    message: Message
    chat: MessageChat
    sender: MessageSender | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message.to_dict()

        chat = self.chat.to_dict()

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "chat": chat,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message
        from ..models.message_chat import MessageChat
        from ..models.message_sender import MessageSender

        d = dict(src_dict)
        message = Message.from_dict(d.pop("message"))

        chat = MessageChat.from_dict(d.pop("chat"))

        _sender = d.pop("sender", UNSET)
        sender: MessageSender | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = MessageSender.from_dict(_sender)

        message_data = cls(
            message=message,
            chat=chat,
            sender=sender,
        )

        message_data.additional_properties = d
        return message_data

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
