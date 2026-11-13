from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="LookupResult")


@_attrs_define
class LookupResult:
    """One phone number or username. Not found (no Telegram account, hidden
    by its owner's privacy, or a username of a channel or group) is
    `found` false without `code`; a lookup that failed carries `code`,
    and `upstreamCode` and `retryAfterMs` where they apply.

        Attributes:
            query (str): The phone number or username as given
            found (bool):
            user (User | Unset): A Telegram user
            code (str | Unset):  Example: flood_wait.
            upstream_code (str | Unset): Telegram's error type, e.g. `FLOOD_WAIT`
            retry_after_ms (int | Unset):
    """

    query: str
    found: bool
    user: User | Unset = UNSET
    code: str | Unset = UNSET
    upstream_code: str | Unset = UNSET
    retry_after_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        found = self.found

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        code = self.code

        upstream_code = self.upstream_code

        retry_after_ms = self.retry_after_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "found": found,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if code is not UNSET:
            field_dict["code"] = code
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User

        d = dict(src_dict)
        query = d.pop("query")

        found = d.pop("found")

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        code = d.pop("code", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        lookup_result = cls(
            query=query,
            found=found,
            user=user,
            code=code,
            upstream_code=upstream_code,
            retry_after_ms=retry_after_ms,
        )

        lookup_result.additional_properties = d
        return lookup_result

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
