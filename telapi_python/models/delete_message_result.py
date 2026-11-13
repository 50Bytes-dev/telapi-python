from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteMessageResult")


@_attrs_define
class DeleteMessageResult:
    """`status`: `deleted`, `not_found`, `forbidden`, `too_old`; new values may come.

    Attributes:
        message_id (int):
        status (str):  Example: deleted.
        upstream_code (str | Unset):
    """

    message_id: int
    status: str
    upstream_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        status = self.status

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "status": status,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        status = d.pop("status")

        upstream_code = d.pop("upstreamCode", UNSET)

        delete_message_result = cls(
            message_id=message_id,
            status=status,
            upstream_code=upstream_code,
        )

        delete_message_result.additional_properties = d
        return delete_message_result

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
