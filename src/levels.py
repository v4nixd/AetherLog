from enum import Enum

class LogLevel(Enum):
    DEBUG = (0, "blue")
    INFO = (1, "blue")
    SUCCESS = (2, "green")
    WARN = (3, "yellow")
    ERROR = (4, "red")
    FATAL = (5, "red")

    @property
    def MAX_LENGTH(self):
        return len(LogLevel.SUCCESS.name)