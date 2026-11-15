from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monoforum_thread import MonoforumThread
    from ..models.topic import Topic


T = TypeVar("T", bound="TopicListResponse")


@_attrs_define
class TopicListResponse:
    """`topics` and `orderByCreateDate` for a forum; `threads` for a monoforum.

    Attributes:
        success (bool):
        topics (list[Topic] | Unset): A forum's topics, in Telegram's order
        order_by_create_date (bool | Unset): A forum's topics are ordered by creation rather than by last message
        threads (list[MonoforumThread] | Unset): A monoforum's threads, most recent first
        next_cursor (str | Unset): The cursor of the next page; absent on the last
    """

    success: bool
    topics: list[Topic] | Unset = UNSET
    order_by_create_date: bool | Unset = UNSET
    threads: list[MonoforumThread] | Unset = UNSET
    next_cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        order_by_create_date = self.order_by_create_date

        threads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threads, Unset):
            threads = []
            for threads_item_data in self.threads:
                threads_item = threads_item_data.to_dict()
                threads.append(threads_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if topics is not UNSET:
            field_dict["topics"] = topics
        if order_by_create_date is not UNSET:
            field_dict["orderByCreateDate"] = order_by_create_date
        if threads is not UNSET:
            field_dict["threads"] = threads
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monoforum_thread import MonoforumThread
        from ..models.topic import Topic

        d = dict(src_dict)
        success = d.pop("success")

        _topics = d.pop("topics", UNSET)
        topics: list[Topic] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = Topic.from_dict(topics_item_data)

                topics.append(topics_item)

        order_by_create_date = d.pop("orderByCreateDate", UNSET)

        _threads = d.pop("threads", UNSET)
        threads: list[MonoforumThread] | Unset = UNSET
        if _threads is not UNSET:
            threads = []
            for threads_item_data in _threads:
                threads_item = MonoforumThread.from_dict(threads_item_data)

                threads.append(threads_item)

        next_cursor = d.pop("nextCursor", UNSET)

        topic_list_response = cls(
            success=success,
            topics=topics,
            order_by_create_date=order_by_create_date,
            threads=threads,
            next_cursor=next_cursor,
        )

        topic_list_response.additional_properties = d
        return topic_list_response

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
