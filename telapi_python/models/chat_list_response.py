from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat import Chat
    from ..models.missing_chat import MissingChat


T = TypeVar("T", bound="ChatListResponse")


@_attrs_define
class ChatListResponse:
    """
    Attributes:
        success (bool):
        chats (list[Chat]):
        next_cursor (str | Unset): The cursor of the next page; absent on the last
        missing (list[MissingChat] | Unset): With `ids` only, and then always present (empty when every chat was found)
    """

    success: bool
    chats: list[Chat]
    next_cursor: str | Unset = UNSET
    missing: list[MissingChat] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        chats = []
        for chats_item_data in self.chats:
            chats_item = chats_item_data.to_dict()
            chats.append(chats_item)

        next_cursor = self.next_cursor

        missing: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = []
            for missing_item_data in self.missing:
                missing_item = missing_item_data.to_dict()
                missing.append(missing_item)

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
        if missing is not UNSET:
            field_dict["missing"] = missing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat import Chat
        from ..models.missing_chat import MissingChat

        d = dict(src_dict)
        success = d.pop("success")

        chats = []
        _chats = d.pop("chats")
        for chats_item_data in _chats:
            chats_item = Chat.from_dict(chats_item_data)

            chats.append(chats_item)

        next_cursor = d.pop("nextCursor", UNSET)

        _missing = d.pop("missing", UNSET)
        missing: list[MissingChat] | Unset = UNSET
        if _missing is not UNSET:
            missing = []
            for missing_item_data in _missing:
                missing_item = MissingChat.from_dict(missing_item_data)

                missing.append(missing_item)

        chat_list_response = cls(
            success=success,
            chats=chats,
            next_cursor=next_cursor,
            missing=missing,
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
