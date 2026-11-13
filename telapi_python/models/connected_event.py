from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connected_data import ConnectedData


T = TypeVar("T", bound="ConnectedEvent")


@_attrs_define
class ConnectedEvent:
    """The login is connected (after a login, a connect, the start of the gateway, or an outage).

    Attributes:
        id (UUID): The event id, the same on every retry
        type_ (Literal['Connected']):
        account_id (UUID):
        account_name (str):
        timestamp (int): Unix time in seconds of the event
        data (ConnectedData):
    """

    id: UUID
    type_: Literal["Connected"]
    account_id: UUID
    account_name: str
    timestamp: int
    data: ConnectedData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        account_id = str(self.account_id)

        account_name = self.account_name

        timestamp = self.timestamp

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "accountId": account_id,
                "accountName": account_name,
                "timestamp": timestamp,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_data import ConnectedData

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = cast(Literal["Connected"], d.pop("type"))
        if type_ != "Connected":
            raise ValueError(f"type must match const 'Connected', got '{type_}'")

        account_id = UUID(d.pop("accountId"))

        account_name = d.pop("accountName")

        timestamp = d.pop("timestamp")

        data = ConnectedData.from_dict(d.pop("data"))

        connected_event = cls(
            id=id,
            type_=type_,
            account_id=account_id,
            account_name=account_name,
            timestamp=timestamp,
            data=data,
        )

        connected_event.additional_properties = d
        return connected_event

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
