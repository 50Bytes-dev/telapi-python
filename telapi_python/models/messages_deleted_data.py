from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagesDeletedData")


@_attrs_define
class MessagesDeletedData:
    """
    Attributes:
        message_ids (list[int]):
        chat_id (int | Unset): The supergroup or channel of the messages; absent for private chats and basic groups,
            whose messages share one id sequence per account and whose deletions Telegram sends without the chat
    """

    message_ids: list[int]
    chat_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_ids = self.message_ids

        chat_id = self.chat_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageIds": message_ids,
            }
        )
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_ids = cast(list[int], d.pop("messageIds"))

        chat_id = d.pop("chatId", UNSET)

        messages_deleted_data = cls(
            message_ids=message_ids,
            chat_id=chat_id,
        )

        messages_deleted_data.additional_properties = d
        return messages_deleted_data

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
