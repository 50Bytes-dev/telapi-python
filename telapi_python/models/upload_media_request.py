from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_upload_type import MediaUploadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadMediaRequest")


@_attrs_define
class UploadMediaRequest:
    """Exactly one of `url` and `data`

    Attributes:
        type_ (MediaUploadType): `photo` is prepared and sent as a photo; the others go up as documents with their
            attributes
        url (str | Unset): http(s) URL the gateway fetches Example: https://example.com/photo.jpg.
        data (str | Unset): The file as base64 or a base64 data URL
        file_name (str | Unset): The file name to show (not for `photo`); the fetched file's name when absent
        mime_type (str | Unset): The MIME type (not for `photo`); the data URL's or the fetched file's own when
            specific, else detected from the content and the name
        duration (int | Unset): Seconds (`video`, `audio`, `voice`, `animation`); Telegram shows it and does not read it
            from the file
        width (int | Unset): Pixels (`video`, `animation`)
        height (int | Unset): Pixels (`video`, `animation`)
    """

    type_: MediaUploadType
    url: str | Unset = UNSET
    data: str | Unset = UNSET
    file_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    duration: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        url = self.url

        data = self.data

        file_name = self.file_name

        mime_type = self.mime_type

        duration = self.duration

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MediaUploadType(d.pop("type"))

        url = d.pop("url", UNSET)

        data = d.pop("data", UNSET)

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        duration = d.pop("duration", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        upload_media_request = cls(
            type_=type_,
            url=url,
            data=data,
            file_name=file_name,
            mime_type=mime_type,
            duration=duration,
            width=width,
            height=height,
        )

        upload_media_request.additional_properties = d
        return upload_media_request

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
