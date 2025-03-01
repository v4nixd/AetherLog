from time import strftime

from models import AetherConfig
from levels import LogLevel

class AetherLogger:
    """
    Parameters
    ----------
    config : AetherConfig
        The configuration object for this instance
    """

    def __init__(self, config: AetherConfig):
        """
        :param: config The configuration object for this instance
        """
        self.config = config

    def _get_time(self):
        return strftime("%H:%M:%S")

    def log(self, content: str, level: LogLevel):
        level_name = level.name + " " * (len(LogLevel.SUCCESS.name) - len(level.name))
        time = self._get_time()
        print(self.config.template.format(level=level_name, time=time, content=content))

if __name__=="__main__":
    logger = AetherLogger(AetherConfig())
    logger.log("hello, world!", LogLevel.INFO)
    logger.log("hi", LogLevel.SUCCESS)