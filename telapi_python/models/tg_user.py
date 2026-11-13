from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TgUser")


@_attrs_define
class TgUser:
    """The Telegram user the account is logged into

    Attributes:
        id (int):  Example: 123456789.
        first_name (str):  Example: Anna.
        last_name (str):  Example: Petrova.
        name (str): First and last name together Example: Anna Petrova.
        premium (bool):
        username (str | Unset):  Example: anna_p.
        phone (str | Unset): Digits with the country code Example: 79001234567.
    """

    id: int
    first_name: str
    last_name: str
    name: str
    premium: bool
    username: str | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        name = self.name

        premium = self.premium

        username = self.username

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firstName": first_name,
                "lastName": last_name,
                "name": name,
                "premium": premium,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        name = d.pop("name")

        premium = d.pop("premium")

        username = d.pop("username", UNSET)

        phone = d.pop("phone", UNSET)

        tg_user = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            name=name,
            premium=premium,
            username=username,
            phone=phone,
        )

        tg_user.additional_properties = d
        return tg_user

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
