from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TypingData")


@_attrs_define
class TypingData:
    """
    Attributes:
        chat_id (int):
        user_id (int):
        action (str): `typing`, `cancel`, `record_video`, `upload_video`, `record_audio`, `upload_audio`,
            `upload_photo`, `upload_document`, `record_round`, `upload_round`, `choose_location`, `choose_contact`,
            `choose_sticker`, `play_game`, `import_history`, or `other` for an action Telegram added later; new values may
            come. Voice activity in a group call and animated emoji interactions are not sent, nor is an action of a user
            who writes as a channel. Example: typing.
    """

    chat_id: int
    user_id: int
    action: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        user_id = self.user_id

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "userId": user_id,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        user_id = d.pop("userId")

        action = d.pop("action")

        typing_data = cls(
            chat_id=chat_id,
            user_id=user_id,
            action=action,
        )

        typing_data.additional_properties = d
        return typing_data

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
