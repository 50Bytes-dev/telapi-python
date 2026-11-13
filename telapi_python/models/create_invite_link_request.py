from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInviteLinkRequest")


@_attrs_define
class CreateInviteLinkRequest:
    """
    Attributes:
        expire_at (int | Unset): Unix time in seconds when the link stops working; left out or 0, never
        usage_limit (int | Unset): How many may join by it; left out or 0, no limit
    """

    expire_at: int | Unset = UNSET
    usage_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expire_at = self.expire_at

        usage_limit = self.usage_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expire_at is not UNSET:
            field_dict["expireAt"] = expire_at
        if usage_limit is not UNSET:
            field_dict["usageLimit"] = usage_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expire_at = d.pop("expireAt", UNSET)

        usage_limit = d.pop("usageLimit", UNSET)

        create_invite_link_request = cls(
            expire_at=expire_at,
            usage_limit=usage_limit,
        )

        create_invite_link_request.additional_properties = d
        return create_invite_link_request

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
