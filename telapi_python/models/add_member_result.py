from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddMemberResult")


@_attrs_define
class AddMemberResult:
    """`status`: `added` (the user is a member now, also when they already were) or `failed` (`code` as in the error
    answers, with `upstreamCode` and `retryAfterMs` when the error has them; `write_forbidden` without `upstreamCode`
    when Telegram reported the user as a missing invitee, their privacy settings); new values may come.

        Attributes:
            user_id (int):
            status (str):  Example: added.
            code (str | Unset):
            upstream_code (str | Unset):
            retry_after_ms (int | Unset): `flood_wait`: in how many milliseconds the call may come again
    """

    user_id: int
    status: str
    code: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    retry_after_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        status = self.status

        code = self.code

        upstream_code = self.upstream_code

        retry_after_ms = self.retry_after_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "status": status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        status = d.pop("status")

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        add_member_result = cls(
            user_id=user_id,
            status=status,
            code=code,
            upstream_code=upstream_code,
            retry_after_ms=retry_after_ms,
        )

        add_member_result.additional_properties = d
        return add_member_result

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
