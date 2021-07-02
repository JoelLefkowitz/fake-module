import importlib
import sys

from types import ModuleType, TracebackType
from typing import Optional, Type, Any
from .exceptions import MissingModule


class FakeModule:
    name: str

    def __init__(self, name: str) -> None:
        if name not in sys.modules:
            raise MissingModule(name)

        self.name = name

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        setattr(self.module, name, value)

    def __enter__(self) -> "FakeModule":
        self.purge()
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self.restore()

    @property
    def module(self) -> ModuleType:
        return sys.modules[self.name]

    def purge(self) -> None:
        unchanged = [
            "__file__",
            "__loader__",
            "__package__",
            "__path__",
            "__spec__",
        ]

        for key in set(self.module.__dict__) - set(unchanged):
            delattr(self.module, key)

    def restore(self) -> None:
        importlib.reload(self.module)
