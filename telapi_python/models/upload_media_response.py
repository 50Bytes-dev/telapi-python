from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadMediaResponse")


@_attrs_define
class UploadMediaResponse:
    """
    Attributes:
        success (bool):
        attachment (str): The handle for `POST /messages` (`tgm1.…`), valid in any chat of the same Telegram user
            Example: tgm1.AAECAwQ.
        type_ (str):  Example: photo.
        size (int): Bytes uploaded
        file_name (str | Unset):
        mime_type (str | Unset):
        width (int | Unset):
        height (int | Unset):
        duration (int | Unset): Seconds
    """

    success: bool
    attachment: str
    type_: str
    size: int
    file_name: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        attachment = self.attachment

        type_ = self.type_

        size = self.size

        file_name = self.file_name

        mime_type = self.mime_type

        width = self.width

        height = self.height

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "attachment": attachment,
                "type": type_,
                "size": size,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
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
        success = d.pop("success")

        attachment = d.pop("attachment")

        type_ = d.pop("type")

        size = d.pop("size")

        file_name = d.pop("fileName", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        duration = d.pop("duration", UNSET)

        upload_media_response = cls(
            success=success,
            attachment=attachment,
            type_=type_,
            size=size,
            file_name=file_name,
            mime_type=mime_type,
            width=width,
            height=height,
            duration=duration,
        )

        upload_media_response.additional_properties = d
        return upload_media_response

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
