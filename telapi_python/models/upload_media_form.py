from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.media_upload_type import MediaUploadType
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadMediaForm")


@_attrs_define
class UploadMediaForm:
    """
    Attributes:
        file (File):
        type_ (MediaUploadType): `photo` is prepared and sent as a photo; the others go up as documents with their
            attributes
        file_name (str | Unset): The file name to show; the part's file name when absent (not for `photo`)
        mime_type (str | Unset): The MIME type (not for `photo`); the part's own when specific, else detected from the
            content and the name
        duration (int | Unset): Seconds (`video`, `audio`, `voice`, `animation`); Telegram shows it and does not read it
            from the file
        width (int | Unset): Pixels (`video`, `animation`)
        height (int | Unset): Pixels (`video`, `animation`)
    """

    file: File
    type_: MediaUploadType
    file_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    duration: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        type_ = self.type_.value

        file_name = self.file_name

        mime_type = self.mime_type

        duration = self.duration

        width = self.width

        height = self.height

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "type": type_,
            }
        )
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("type", (None, str(self.type_.value).encode(), "text/plain")))

        if not isinstance(self.file_name, Unset):
            files.append(("fileName", (None, str(self.file_name).encode(), "text/plain")))

        if not isinstance(self.mime_type, Unset):
            files.append(("mimeType", (None, str(self.mime_type).encode(), "text/plain")))

        if not isinstance(self.duration, Unset):
            files.append(("duration", (None, str(self.duration).encode(), "text/plain")))

        if not isinstance(self.width, Unset):
            files.append(("width", (None, str(self.width).encode(), "text/plain")))

        if not isinstance(self.height, Unset):
            files.append(("height", (None, str(self.height).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        type_ = MediaUploadType(d.pop("type"))

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        duration = d.pop("duration", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        upload_media_form = cls(
            file=file,
            type_=type_,
            file_name=file_name,
            mime_type=mime_type,
            duration=duration,
            width=width,
            height=height,
        )

        upload_media_form.additional_properties = d
        return upload_media_form

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
