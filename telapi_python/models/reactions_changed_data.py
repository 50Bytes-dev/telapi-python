from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reaction import Reaction


T = TypeVar("T", bound="ReactionsChangedData")


@_attrs_define
class ReactionsChangedData:
    """
    Attributes:
        chat_id (int):
        message_id (int):
        reactions (list[Reaction]):
    """

    chat_id: int
    message_id: int
    reactions: list[Reaction]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_id = self.message_id

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "messageId": message_id,
                "reactions": reactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reaction import Reaction

        d = dict(src_dict)
        chat_id = d.pop("chatId")

        message_id = d.pop("messageId")

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = Reaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        reactions_changed_data = cls(
            chat_id=chat_id,
            message_id=message_id,
            reactions=reactions,
        )

        reactions_changed_data.additional_properties = d
        return reactions_changed_data

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
