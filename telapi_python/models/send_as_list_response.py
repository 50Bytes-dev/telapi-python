from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.send_as_peer import SendAsPeer


T = TypeVar("T", bound="SendAsListResponse")


@_attrs_define
class SendAsListResponse:
    """
    Attributes:
        success (bool):
        peers (list[SendAsPeer]):
    """

    success: bool
    peers: list[SendAsPeer]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()
            peers.append(peers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "peers": peers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_as_peer import SendAsPeer

        d = dict(src_dict)
        success = d.pop("success")

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = SendAsPeer.from_dict(peers_item_data)

            peers.append(peers_item)

        send_as_list_response = cls(
            success=success,
            peers=peers,
        )

        send_as_list_response.additional_properties = d
        return send_as_list_response

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
