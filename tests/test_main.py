from typing import Optional, Sequence

import pytest

from pytest import LogCaptureFixture

from havhav.main import main


@pytest.mark.parametrize("hav", [[], ["2"]])
def test_main_happy_path(
    hav: Optional[Sequence[str]], capsys: LogCaptureFixture
) -> None:
    actual = main(hav)
    out, err = capsys.readouterr()

    assert actual == 0
    assert len(out) >= 1
    assert err == ""


def test_main_exception(capsys: LogCaptureFixture) -> None:
    actual = main(["a"])
    out, err = capsys.readouterr()

    assert actual == 1
    assert out == ""
    assert err == "havhav number of facts must be an integer!\n"
