from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """A member. `role`: `creator`, `admin`, `member`, `restricted`, `left`, `banned`; new values may come.

    Attributes:
        user_id (int):
        name (str):
        bot (bool):
        role (str):  Example: member.
        username (str | Unset):
    """

    user_id: int
    name: str
    bot: bool
    role: str
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        name = self.name

        bot = self.bot

        role = self.role

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "name": name,
                "bot": bot,
                "role": role,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        name = d.pop("name")

        bot = d.pop("bot")

        role = d.pop("role")

        username = d.pop("username", UNSET)

        member = cls(
            user_id=user_id,
            name=name,
            bot=bot,
            role=role,
            username=username,
        )

        member.additional_properties = d
        return member

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
