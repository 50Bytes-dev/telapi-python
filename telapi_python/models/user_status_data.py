from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserStatusData")


@_attrs_define
class UserStatusData:
    """
    Attributes:
        user_id (int):
        online (bool):
        last_seen_at (int | Unset): Unix time in seconds
    """

    user_id: int
    online: bool
    last_seen_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        online = self.online

        last_seen_at = self.last_seen_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "online": online,
            }
        )
        if last_seen_at is not UNSET:
            field_dict["lastSeenAt"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        online = d.pop("online")

        last_seen_at = d.pop("lastSeenAt", UNSET)

        user_status_data = cls(
            user_id=user_id,
            online=online,
            last_seen_at=last_seen_at,
        )

        user_status_data.additional_properties = d
        return user_status_data

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
