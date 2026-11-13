from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_chat_type import NewChatType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChatRequest")


@_attrs_define
class CreateChatRequest:
    """
    Attributes:
        type_ (NewChatType): `group` creates a supergroup, `channel` a broadcast channel
        title (str):
        about (str | Unset):
        user_ids (list[int] | Unset): Users to invite at once, each once
    """

    type_: NewChatType
    title: str
    about: str | Unset = UNSET
    user_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        title = self.title

        about = self.about

        user_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
            }
        )
        if about is not UNSET:
            field_dict["about"] = about
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = NewChatType(d.pop("type"))

        title = d.pop("title")

        about = d.pop("about", UNSET)

        user_ids = cast(list[int], d.pop("userIds", UNSET))

        create_chat_request = cls(
            type_=type_,
            title=title,
            about=about,
            user_ids=user_ids,
        )

        create_chat_request.additional_properties = d
        return create_chat_request

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
