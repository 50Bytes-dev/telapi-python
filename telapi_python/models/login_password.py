from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginPassword")


@_attrs_define
class LoginPassword:
    """Step `password`: two-step verification is on.

    Attributes:
        hint (str): The hint the owner set ("" = none)
        has_recovery (bool): A recovery email is set
    """

    hint: str
    has_recovery: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hint = self.hint

        has_recovery = self.has_recovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hint": hint,
                "hasRecovery": has_recovery,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hint = d.pop("hint")

        has_recovery = d.pop("hasRecovery")

        login_password = cls(
            hint=hint,
            has_recovery=has_recovery,
        )

        login_password.additional_properties = d
        return login_password

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
