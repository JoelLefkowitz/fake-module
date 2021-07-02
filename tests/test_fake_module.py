# pylint: disable=comparison-with-callable
import colorsys

import pytest

from src.fake_module import FakeModule, MissingModule


def test_faked_attributes() -> None:
    fake = FakeModule("colorsys")
    fake.purge()

    setattr(fake, "rgb_to_hls", 1)
    assert colorsys.rgb_to_hls == 1  # type: ignore


def test_context_manager() -> None:
    with FakeModule("colorsys") as fake:
        assert isinstance(fake, FakeModule)

        with pytest.raises(AttributeError):
            colorsys.rgb_to_hls(1, 0, 0)

    assert colorsys.rgb_to_hls(1, 0, 0) == (0, 0.5, 1)


def test_missing_module() -> None:
    with pytest.raises(MissingModule):
        FakeModule("nonexistent")
