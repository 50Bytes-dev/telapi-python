from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_member_result import AddMemberResult


T = TypeVar("T", bound="AddMembersResponse")


@_attrs_define
class AddMembersResponse:
    """
    Attributes:
        success (bool):
        results (list[AddMemberResult]):
    """

    success: bool
    results: list[AddMemberResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_member_result import AddMemberResult

        d = dict(src_dict)
        success = d.pop("success")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AddMemberResult.from_dict(results_item_data)

            results.append(results_item)

        add_members_response = cls(
            success=success,
            results=results,
        )

        add_members_response.additional_properties = d
        return add_members_response

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
