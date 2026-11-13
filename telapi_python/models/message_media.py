from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageMedia")


@_attrs_define
class MessageMedia:
    """The media of a message. `type`: `photo`, `video`, `audio`, `voice`, `document`, `sticker`, `animation`, `contact`,
    `location`, `poll`, `webpage`, `other`; new values may come.

        Attributes:
            type_ (str):  Example: photo.
            file_name (str | Unset):
            mime_type (str | Unset):
            size (int | Unset): Bytes
            width (int | Unset):
            height (int | Unset):
            duration (int | Unset): Seconds
    """

    type_: str
    file_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    size: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        file_name = self.file_name

        mime_type = self.mime_type

        size = self.size

        width = self.width

        height = self.height

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if size is not UNSET:
            field_dict["size"] = size
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        size = d.pop("size", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        duration = d.pop("duration", UNSET)

        message_media = cls(
            type_=type_,
            file_name=file_name,
            mime_type=mime_type,
            size=size,
            width=width,
            height=height,
            duration=duration,
        )

        message_media.additional_properties = d
        return message_media

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
