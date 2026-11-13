from enum import Enum


class NewChatType(str, Enum):
    CHANNEL = "channel"
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
