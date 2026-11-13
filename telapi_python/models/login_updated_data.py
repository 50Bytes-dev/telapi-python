from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.login import Login


T = TypeVar("T", bound="LoginUpdatedData")


@_attrs_define
class LoginUpdatedData:
    """
    Attributes:
        login (Login): The login into Telegram. `step`: `none` (no login ran), `qr` (scan
            `qr`), `code` (send the code), `password` (send the cloud password),
            `done` (`tgUser`; `Connected` follows), `failed` (`failure`). New
            steps may come.
    """

    login: Login
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login = self.login.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login import Login

        d = dict(src_dict)
        login = Login.from_dict(d.pop("login"))

        login_updated_data = cls(
            login=login,
        )

        login_updated_data.additional_properties = d
        return login_updated_data

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
