from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MissingChat")


@_attrs_define
class MissingChat:
    """A chat of `GET /chats?ids=` that the answer does not have

    Attributes:
        chat_id (int): The chat id as given
        code (str): Why, as an error code: `peer_not_found` (never seen by the account, or left out of Telegram's
            answer), or the refusal Telegram gave for the read of this chat alone; new values may come
        upstream_code (str | Unset): Telegram's error, when Telegram gave one
    """

    chat_id: int
    code: str
    upstream_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        code = self.code

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "code": code,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        code = d.pop("code")

        upstream_code = d.pop("upstreamCode", UNSET)

        missing_chat = cls(
            chat_id=chat_id,
            code=code,
            upstream_code=upstream_code,
        )

        missing_chat.additional_properties = d
        return missing_chat

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
