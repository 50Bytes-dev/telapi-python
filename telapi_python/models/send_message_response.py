from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageResponse")


@_attrs_define
class SendMessageResponse:
    """
    Attributes:
        success (bool):
        chat_id (int):
        message_ids (list[int]): Every message of the send (one per album item); empty when Telegram's answer did not
            carry the ids
        duplicate (bool): Telegram already had this send (the same `ref` went out before, or this request's first
            attempt did); the ids are that send's when known
        message_id (int | Unset): The id of the (first) message; absent when Telegram's answer did not carry the ids
    """

    success: bool
    chat_id: int
    message_ids: list[int]
    duplicate: bool
    message_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chat_id = self.chat_id

        message_ids = self.message_ids

        duplicate = self.duplicate

        message_id = self.message_id

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        chat_id = d.pop("chatId")

        message_ids = cast(list[int], d.pop("messageIds"))

        duplicate = d.pop("duplicate")

        message_id = d.pop("messageId", UNSET)

        send_message_response = cls(
            success=success,
            chat_id=chat_id,
            message_ids=message_ids,
            duplicate=duplicate,
            message_id=message_id,
        )

        send_message_response.additional_properties = d
        return send_message_response

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
