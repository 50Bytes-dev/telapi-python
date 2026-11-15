from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendAsPeer")


@_attrs_define
class SendAsPeer:
    """A chat the account may send as. `type`: `user` (the account itself), `group`, `channel`; new values may come.

    Attributes:
        chat_id (int):  Example: -1001234567890.
        type_ (str):  Example: channel.
        title (str): The title, or the account's name
        premium_required (bool): Only a Premium account may send as this chat
        username (str | Unset):
    """

    chat_id: int
    type_: str
    title: str
    premium_required: bool
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_

        title = self.title

        premium_required = self.premium_required

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
                "premiumRequired": premium_required,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = d.pop("type")

        title = d.pop("title")

        premium_required = d.pop("premiumRequired")

        username = d.pop("username", UNSET)

        send_as_peer = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
            premium_required=premium_required,
            username=username,
        )

        send_as_peer.additional_properties = d
        return send_as_peer

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
