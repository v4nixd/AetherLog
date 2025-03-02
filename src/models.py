class AetherConfig:
    """Config object for AetherLogger

    Parameters
    ----------
    template : str, optional
        Template for logger output
    """
    def __init__(
            self,
            template: str | None = "{level} | {time} | {content}"
    ) -> None:
        self.template = template