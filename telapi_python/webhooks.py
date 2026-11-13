"""Verifying and parsing the gateway's webhook deliveries.

Hand-written, not generated: generate.sh keeps this module across a regeneration.

A delivery is a JSON POST with the headers ``X-Telapi-Event`` (the type), ``X-Telapi-Delivery`` (the event id, the
same on every retry), ``X-Telapi-Timestamp`` (Unix seconds of this attempt) and ``X-Telapi-Signature`` (``sha256=``
and the hex HMAC-SHA256 of ``timestamp + "." + body`` under the account's webhook secret). The secret is used as the
string the gateway showed, not decoded. Each retry is signed anew with its own timestamp, so a retry of an old event
still verifies; dedupe by the event id.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from collections.abc import Mapping
from typing import Any

from .models import (
    ConnectedEvent,
    DisconnectedEvent,
    LoggedOutEvent,
    LoginUpdatedEvent,
    MessageEditedEvent,
    MessageEvent,
    MessagesDeletedEvent,
    MessagesReadEvent,
    PausedEvent,
    ReactionsChangedEvent,
    ResumedEvent,
    TypingEvent,
    UserStatusEvent,
)

EVENT_HEADER = "X-Telapi-Event"
DELIVERY_HEADER = "X-Telapi-Delivery"
TIMESTAMP_HEADER = "X-Telapi-Timestamp"
SIGNATURE_HEADER = "X-Telapi-Signature"

# How old a delivery's timestamp may be, in seconds, before it is taken for a replay.
DEFAULT_MAX_AGE = 300

WebhookEvent = (
    LoginUpdatedEvent
    | ConnectedEvent
    | DisconnectedEvent
    | LoggedOutEvent
    | PausedEvent
    | ResumedEvent
    | MessageEvent
    | MessageEditedEvent
    | MessagesDeletedEvent
    | MessagesReadEvent
    | TypingEvent
    | UserStatusEvent
    | ReactionsChangedEvent
)

# The model of each event type, in the order of the gateway's EventType.
EVENT_MODELS: dict[str, type[WebhookEvent]] = {
    "LoginUpdated": LoginUpdatedEvent,
    "Connected": ConnectedEvent,
    "Disconnected": DisconnectedEvent,
    "LoggedOut": LoggedOutEvent,
    "Paused": PausedEvent,
    "Resumed": ResumedEvent,
    "Message": MessageEvent,
    "MessageEdited": MessageEditedEvent,
    "MessagesDeleted": MessagesDeletedEvent,
    "MessagesRead": MessagesReadEvent,
    "Typing": TypingEvent,
    "UserStatus": UserStatusEvent,
    "ReactionsChanged": ReactionsChangedEvent,
}


class InvalidSignature(Exception):
    """The delivery's signature or timestamp does not hold: do not trust its body."""


class UnknownEvent(ValueError):
    """The body is an event of a type this package does not know."""


def sign(secret: str, timestamp: str, body: bytes) -> str:
    """The ``X-Telapi-Signature`` of ``body`` sent at ``timestamp``: ``sha256=<hex HMAC-SHA256>``."""
    mac = hmac.new(secret.encode(), timestamp.encode() + b"." + body, hashlib.sha256)
    return "sha256=" + mac.hexdigest()


def verify_signature(
    secret: str,
    timestamp: str,
    signature: str,
    body: bytes,
    *,
    max_age: float = DEFAULT_MAX_AGE,
    now: float | None = None,
) -> bool:
    """Whether ``signature`` is the gateway's for ``body`` at ``timestamp`` and the timestamp is at most ``max_age``
    seconds from ``now`` (the current time by default).

    ``body`` must be the raw bytes as received, before any JSON parsing. The comparison is in constant time.
    """
    try:
        sent = int(timestamp)
    except (TypeError, ValueError):
        return False
    if now is None:
        now = time.time()
    if abs(now - sent) > max_age:
        return False
    return hmac.compare_digest(sign(secret, timestamp, body).encode(), signature.encode())


def _header(headers: Mapping[str, str], name: str) -> str | None:
    value = headers.get(name)
    if value is not None:
        return value
    lowered = name.lower()
    for key, value in headers.items():
        if key.lower() == lowered:
            return value
    return None


def verify(
    secret: str,
    headers: Mapping[str, str],
    body: bytes,
    *,
    max_age: float = DEFAULT_MAX_AGE,
    now: float | None = None,
) -> bool:
    """:func:`verify_signature` with the timestamp and signature taken from a delivery's headers (any case)."""
    timestamp = _header(headers, TIMESTAMP_HEADER)
    signature = _header(headers, SIGNATURE_HEADER)
    if timestamp is None or signature is None:
        return False
    return verify_signature(secret, timestamp, signature, body, max_age=max_age, now=now)


def parse_event(body: bytes | str | Mapping[str, Any]) -> WebhookEvent:
    """The event model of a delivery's body, picked by its ``type``.

    Raises :class:`UnknownEvent` for a type this package does not know (the gateway may add types), and
    ``ValueError`` or ``KeyError`` for a body that is not an event.
    """
    if isinstance(body, (bytes, str)):
        body = json.loads(body)
    if not isinstance(body, Mapping):
        raise ValueError("a webhook body is a JSON object")
    kind = body.get("type")
    model = EVENT_MODELS.get(kind) if isinstance(kind, str) else None
    if model is None:
        raise UnknownEvent(f"unknown event type {kind!r}")
    return model.from_dict(body)


def verify_and_parse(
    secret: str,
    headers: Mapping[str, str],
    body: bytes,
    *,
    max_age: float = DEFAULT_MAX_AGE,
    now: float | None = None,
) -> WebhookEvent:
    """Verifies a delivery (:func:`verify`) and parses its event (:func:`parse_event`).

    Raises :class:`InvalidSignature` when the signature or the timestamp does not hold.
    """
    if not verify(secret, headers, body, max_age=max_age, now=now):
        raise InvalidSignature("the webhook signature or timestamp does not hold")
    return parse_event(body)


__all__ = [
    "DEFAULT_MAX_AGE",
    "DELIVERY_HEADER",
    "EVENT_HEADER",
    "EVENT_MODELS",
    "SIGNATURE_HEADER",
    "TIMESTAMP_HEADER",
    "InvalidSignature",
    "UnknownEvent",
    "WebhookEvent",
    "parse_event",
    "sign",
    "verify",
    "verify_and_parse",
    "verify_signature",
]
