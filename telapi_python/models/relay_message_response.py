from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelayMessageResponse")


@_attrs_define
class RelayMessageResponse:
    """
    Attributes:
        success (bool):
        chat_id (int):
        message_ids (list[int]): Every message of the send (one per album item); empty when Telegram's answer did not
            carry the ids
        duplicate (bool): Telegram already had this send (the same `ref` went out before, or this request's first
            attempt did); the ids are that send's when known
        message_id (int | Unset): The id of the (first) message; absent when Telegram's answer did not carry the ids
        saved_messages_left (list[int] | Unset): The ids of the copy in Saved Messages when deleting it failed; absent
            when it was deleted
    """

    success: bool
    chat_id: int
    message_ids: list[int]
    duplicate: bool
    message_id: int | Unset = UNSET
    saved_messages_left: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat_id = self.chat_id

        message_ids = self.message_ids

        duplicate = self.duplicate

        message_id = self.message_id

        saved_messages_left: list[int] | Unset = UNSET
        if not isinstance(self.saved_messages_left, Unset):
            saved_messages_left = self.saved_messages_left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chatId": chat_id,
                "messageIds": message_ids,
                "duplicate": duplicate,
            }
        )
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if saved_messages_left is not UNSET:
            field_dict["savedMessagesLeft"] = saved_messages_left

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        chat_id = d.pop("chatId")

        message_ids = cast(list[int], d.pop("messageIds"))

        duplicate = d.pop("duplicate")

        message_id = d.pop("messageId", UNSET)

        saved_messages_left = cast(list[int], d.pop("savedMessagesLeft", UNSET))

        relay_message_response = cls(
            success=success,
            chat_id=chat_id,
            message_ids=message_ids,
            duplicate=duplicate,
            message_id=message_id,
            saved_messages_left=saved_messages_left,
        )

        relay_message_response.additional_properties = d
        return relay_message_response

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
