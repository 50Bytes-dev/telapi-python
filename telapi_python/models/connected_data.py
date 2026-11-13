from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tg_user import TgUser


T = TypeVar("T", bound="ConnectedData")


@_attrs_define
class ConnectedData:
    """
    Attributes:
        tg_user (TgUser): The Telegram user the account is logged into
        reconnect (bool): The connection came back after an outage
    """

    tg_user: TgUser
    reconnect: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tg_user = self.tg_user.to_dict()

        reconnect = self.reconnect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tgUser": tg_user,
                "reconnect": reconnect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tg_user import TgUser

        d = dict(src_dict)
        tg_user = TgUser.from_dict(d.pop("tgUser"))

        reconnect = d.pop("reconnect")

        connected_data = cls(
            tg_user=tg_user,
            reconnect=reconnect,
        )

        connected_data.additional_properties = d
        return connected_data

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
