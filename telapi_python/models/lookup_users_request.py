from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookupUsersRequest")


@_attrs_define
class LookupUsersRequest:
    """At least one phone number or username

    Attributes:
        phones (list[str] | Unset):  Example: ['79001234567'].
        usernames (list[str] | Unset):  Example: ['anna_p'].
    """

    phones: list[str] | Unset = UNSET
    usernames: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phones: list[str] | Unset = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones

        usernames: list[str] | Unset = UNSET
        if not isinstance(self.usernames, Unset):
            usernames = self.usernames

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phones is not UNSET:
            field_dict["phones"] = phones
        if usernames is not UNSET:
            field_dict["usernames"] = usernames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phones = cast(list[str], d.pop("phones", UNSET))

        usernames = cast(list[str], d.pop("usernames", UNSET))

        lookup_users_request = cls(
            phones=phones,
            usernames=usernames,
        )

        lookup_users_request.additional_properties = d
        return lookup_users_request

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
