from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_type import EventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountRequest")


@_attrs_define
class UpdateAccountRequest:
    """Every given field replaces the stored one

    Attributes:
        name (str | Unset): 1 to 128 bytes after trimming spaces
        webhook_url (str | Unset):
        events (list[EventType] | Unset):
        proxy (str | Unset): "" = none of its own (`TELAPI_DEFAULT_PROXY` when the gateway sets one, direct otherwise);
            a change restarts the Telegram client
    """

    name: str | Unset = UNSET
    webhook_url: str | Unset = UNSET
    events: list[EventType] | Unset = UNSET
    proxy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        webhook_url = self.webhook_url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        proxy = self.proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if events is not UNSET:
            field_dict["events"] = events
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        _events = d.pop("events", UNSET)
        events: list[EventType] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = EventType(events_item_data)

                events.append(events_item)

        proxy = d.pop("proxy", UNSET)

        update_account_request = cls(
            name=name,
            webhook_url=webhook_url,
            events=events,
            proxy=proxy,
        )

        update_account_request.additional_properties = d
        return update_account_request

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
