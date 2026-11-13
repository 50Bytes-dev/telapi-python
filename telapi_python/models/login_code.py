from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginCode")


@_attrs_define
class LoginCode:
    """Step `code`: how Telegram sent the code.

    Attributes:
        type_ (str): `app` (the Telegram app of the account), `sms`, `sms_word`, `sms_phrase`, `call`, `flash_call`,
            `missed_call`, `email`, `fragment`; "" when Telegram names a type the gateway does not know; new values may
            come. `sms_word` and `sms_phrase` have `length` 0. Example: app.
        length (int): Digits in the code Example: 5.
        timeout (int | Unset): Seconds before the next code may be asked
    """

    type_: str
    length: int
    timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        length = self.length

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "length": length,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        length = d.pop("length")

        timeout = d.pop("timeout", UNSET)

        login_code = cls(
            type_=type_,
            length=length,
            timeout=timeout,
        )

        login_code.additional_properties = d
        return login_code

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
