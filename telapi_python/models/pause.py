from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pause")


@_attrs_define
class Pause:
    """The pause of the Telegram user. `reason`: `spam` (PEER_FLOOD,
    USER_RESTRICTED), `flood` (a long FLOOD_WAIT, or the third on sends
    within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
    it); new reasons may come. Lifted only by `POST /session/resume`.

        Attributes:
            reason (str):  Example: spam.
            upstream_code (str): The Telegram error that paused it Example: PEER_FLOOD.
            since (int): Unix time in seconds Example: 1794500000.
            until (int | Unset): `flood`: Unix time in seconds when Telegram's wait ends. The pause still lasts until a
                resume. Example: 1794503600.
    """

    reason: str
    upstream_code: str
    since: int
    until: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        upstream_code = self.upstream_code

        since = self.since

        until = self.until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "upstreamCode": upstream_code,
                "since": since,
            }
        )
        if until is not UNSET:
            field_dict["until"] = until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        upstream_code = d.pop("upstreamCode")

        since = d.pop("since")

        until = d.pop("until", UNSET)

        pause = cls(
            reason=reason,
            upstream_code=upstream_code,
            since=since,
            until=until,
        )

        pause.additional_properties = d
        return pause

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
