from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message import Message


T = TypeVar("T", bound="HistoryResponse")


@_attrs_define
class HistoryResponse:
    """
    Attributes:
        success (bool):
        messages (list[Message]):
        next_offset_id (int | Unset): The `offsetId` of the older page; absent when Telegram tells this page reaches the
            start of the chat
    """

    success: bool
    messages: list[Message]
    next_offset_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        next_offset_id = self.next_offset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "messages": messages,
            }
        )
        if next_offset_id is not UNSET:
            field_dict["nextOffsetId"] = next_offset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message import Message

        d = dict(src_dict)
        success = d.pop("success")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        next_offset_id = d.pop("nextOffsetId", UNSET)

        history_response = cls(
            success=success,
            messages=messages,
            next_offset_id=next_offset_id,
        )

        history_response.additional_properties = d
        return history_response

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
