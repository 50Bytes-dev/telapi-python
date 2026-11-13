from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reaction")


@_attrs_define
class Reaction:
    """
    Attributes:
        reaction (str): The emoji itself, `custom:<documentId>` for a custom emoji (the form a reaction is set with), or
            `paid` for the paid star reaction Example: 👍.
        count (int):
        chosen (bool | Unset): This account chose it; absent when Telegram sent the counts without the account's own
            choice, as it does in large chats
    """

    reaction: str
    count: int
    chosen: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reaction = self.reaction

        count = self.count

        chosen = self.chosen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reaction": reaction,
                "count": count,
            }
        )
        if chosen is not UNSET:
            field_dict["chosen"] = chosen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction = d.pop("reaction")

        count = d.pop("count")

        chosen = d.pop("chosen", UNSET)

        reaction = cls(
            reaction=reaction,
            count=count,
            chosen=chosen,
        )

        reaction.additional_properties = d
        return reaction

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
