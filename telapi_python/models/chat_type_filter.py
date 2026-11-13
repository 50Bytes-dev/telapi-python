from enum import Enum


class ChatTypeFilter(str, Enum):
    BOT = "bot"
    CHANNEL = "channel"
    GROUP = "group"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
