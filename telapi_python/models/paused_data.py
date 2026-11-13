from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pause import Pause


T = TypeVar("T", bound="PausedData")


@_attrs_define
class PausedData:
    """
    Attributes:
        pause (Pause): The pause of the Telegram user. `reason`: `spam` (PEER_FLOOD,
            USER_RESTRICTED), `flood` (a long FLOOD_WAIT, or the third on sends
            within 10 minutes), `frozen` (FROZEN_*: only Telegram's appeal lifts
            it); new reasons may come. Lifted only by `POST /session/resume`.
    """

    pause: Pause
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pause = self.pause.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pause": pause,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pause import Pause

        d = dict(src_dict)
        pause = Pause.from_dict(d.pop("pause"))

        paused_data = cls(
            pause=pause,
        )

        paused_data.additional_properties = d
        return paused_data

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
