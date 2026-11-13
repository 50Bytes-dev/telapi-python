from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginFailure")


@_attrs_define
class LoginFailure:
    """Step `failed`. `reason`: `expired` (timed out, the code expired, or
    five wrong codes or passwords), `cancelled` (a new login or
    `DELETE /session/login`), `rejected` (banned or unregistered number),
    `unavailable` (Telegram refuses the app), `limited` (FLOOD_WAIT on
    login calls; `retryAfterMs`), `failed` (anything else;
    `upstreamCode`), `unsupported` (Telegram asked for a step the gateway
    does not do; `step`). New reasons may come.

        Attributes:
            reason (str):  Example: expired.
            upstream_code (str | Unset):
            retry_after_ms (int | Unset):
            step (str | Unset): `unsupported`: the step Telegram asked for
    """

    reason: str
    upstream_code: str | Unset = UNSET
    retry_after_ms: int | Unset = UNSET
    step: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        upstream_code = self.upstream_code

        retry_after_ms = self.retry_after_ms

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code
        if retry_after_ms is not UNSET:
            field_dict["retryAfterMs"] = retry_after_ms
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        upstream_code = d.pop("upstreamCode", UNSET)

        retry_after_ms = d.pop("retryAfterMs", UNSET)

        step = d.pop("step", UNSET)

        login_failure = cls(
            reason=reason,
            upstream_code=upstream_code,
            retry_after_ms=retry_after_ms,
            step=step,
        )

        login_failure.additional_properties = d
        return login_failure

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
