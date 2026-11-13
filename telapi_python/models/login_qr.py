from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginQr")


@_attrs_define
class LoginQr:
    """Step `qr`: the account's own QR code, renewed about every 30 s. Scan it in Telegram: Settings → Devices → Link
    Desktop Device.

        Attributes:
            image (str): The QR as a PNG data URL Example: data:image/png;base64,iVBORw0KGgo….
            link (str): The `tg://login?token=…` link the QR holds Example: tg://login?token=AQID….
            expires_at (int): Unix time in seconds when this QR stops working
    """

    image: str = _attrs_field(repr=False)
    link: str = _attrs_field(repr=False)
    expires_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        link = self.link

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "link": link,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image")

        link = d.pop("link")

        expires_at = d.pop("expiresAt")

        login_qr = cls(
            image=image,
            link=link,
            expires_at=expires_at,
        )

        login_qr.additional_properties = d
        return login_qr

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
