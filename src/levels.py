from enum import Enum

class LogLevel(Enum):
    DEBUG = (0, "bold blue")
    INFO = (1, "bold blue")
    SUCCESS = (2, "bold green")
    WARN = (3, "bold yellow")
    ERROR = (4, "bold red")
    FATAL = (5, "bold white on red")