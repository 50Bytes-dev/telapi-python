from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parse_mode import ParseMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMessageRequest")


@_attrs_define
class EditMessageRequest:
    """
    Attributes:
        text (str): The new text or caption; missing or empty is `400 invalid_input`
        parse_mode (ParseMode | Unset): How `text` is marked up; absent sends it as it is. `html` is
            Telegram's HTML style (`<b>`, `<i>`, `<u>`, `<s>`, `<a href>`,
            `<code>`, `<pre>`, `<blockquote>`, `<tg-spoiler>`). `markdown` is
            CommonMark: `**bold**`, `*italic*`, `~~strike~~`, `||spoiler||`,
            `` `code` ``, fenced code blocks, `[text](url)`, `> quote`; other
            constructs stay plain text. A mention (`tg://user?id=…`) of a user
            this account never saw is `404 peer_not_found`.
        no_webpage (bool | Unset):
    """

    text: str
    parse_mode: ParseMode | Unset = UNSET
    no_webpage: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        parse_mode: str | Unset = UNSET
        if not isinstance(self.parse_mode, Unset):
            parse_mode = self.parse_mode.value

        no_webpage = self.no_webpage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if parse_mode is not UNSET:
            field_dict["parseMode"] = parse_mode
        if no_webpage is not UNSET:
            field_dict["noWebpage"] = no_webpage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        _parse_mode = d.pop("parseMode", UNSET)
        parse_mode: ParseMode | Unset
        if isinstance(_parse_mode, Unset):
            parse_mode = UNSET
        else:
            parse_mode = ParseMode(_parse_mode)

        no_webpage = d.pop("noWebpage", UNSET)

        edit_message_request = cls(
            text=text,
            parse_mode=parse_mode,
            no_webpage=no_webpage,
        )

        edit_message_request.additional_properties = d
        return edit_message_request

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
