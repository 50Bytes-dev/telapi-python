from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat import Chat


T = TypeVar("T", bound="ChatListResponse")


@_attrs_define
class ChatListResponse:
    """
    Attributes:
        success (bool):
        chats (list[Chat]):
        next_cursor (str | Unset): The cursor of the next page; absent on the last
    """

    success: bool
    chats: list[Chat]
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chats = []
        for chats_item_data in self.chats:
            chats_item = chats_item_data.to_dict()
            chats.append(chats_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chats": chats,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat import Chat

        d = dict(src_dict)
        success = d.pop("success")

        chats = []
        _chats = d.pop("chats")
        for chats_item_data in _chats:
            chats_item = Chat.from_dict(chats_item_data)

            chats.append(chats_item)

        next_cursor = d.pop("nextCursor", UNSET)

        chat_list_response = cls(
            success=success,
            chats=chats,
            next_cursor=next_cursor,
        )

        chat_list_response.additional_properties = d
        return chat_list_response

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
