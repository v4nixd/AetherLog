from rich import print
from time import strftime

from models import AetherConfig
from levels import LogLevel

class AetherLogger:
    def __init__(self, config: AetherConfig) -> None:
        """
        Parameters
        ----------
        config : AetherConfig
            The configuration object for this instance
        """
        self.config = config

    def _get_time(self) -> str:
        return strftime("%H:%M:%S")
    
    def _stylize(self, level: LogLevel, text: str) -> str:
        return f"[{level.value[1]}]{text}[/{level.value[1]}]"

    def _format(self, content: str, level: LogLevel, stylized: bool) -> str:
        level_name = self._stylize(level, level.name) if stylized else level.name
        level_name += " " * (len(LogLevel.SUCCESS.name) - len(level.name))
        time = self._get_time()
        content = self._stylize(level, content) if stylized else content

        return self.config.template.format(level=level_name, time=time, content=content)

    def debug(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.DEBUG, stylized))

    def info(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.INFO, stylized))

    def success(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.SUCCESS, stylized))

    def warn(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.WARN, stylized))

    def error(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.ERROR, stylized))

    def fatal(self, content: str, stylized: bool = False) -> None:
        print(self._format(content, LogLevel.FATAL, stylized))

if __name__=="__main__": #testing
    logger = AetherLogger(AetherConfig())
    logger.debug("Debug message", True)
    logger.info("Information message", True)
    logger.success("Success message", True)
    logger.warn("Warning message", True)
    logger.error("Error message", True)
    logger.fatal("FATAL MESSAGE", True)