from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.member import Member


T = TypeVar("T", bound="MemberListResponse")


@_attrs_define
class MemberListResponse:
    """
    Attributes:
        success (bool):
        members (list[Member]):
        total (int): Members in all, as Telegram counts them
    """

    success: bool
    members: list[Member]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "members": members,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member import Member

        d = dict(src_dict)
        success = d.pop("success")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = Member.from_dict(members_item_data)

            members.append(members_item)

        total = d.pop("total")

        member_list_response = cls(
            success=success,
            members=members,
            total=total,
        )

        member_list_response.additional_properties = d
        return member_list_response

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
