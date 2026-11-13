from enum import Enum


class EventType(str, Enum):
    ALL = "All"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    LOGGEDOUT = "LoggedOut"
    LOGINUPDATED = "LoginUpdated"
    MESSAGE = "Message"
    MESSAGEEDITED = "MessageEdited"
    MESSAGESDELETED = "MessagesDeleted"
    MESSAGESREAD = "MessagesRead"
    PAUSED = "Paused"
    REACTIONSCHANGED = "ReactionsChanged"
    RESUMED = "Resumed"
    TYPING = "Typing"
    USERSTATUS = "UserStatus"

    def __str__(self) -> str:
        return str(self.value)
