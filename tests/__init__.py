# See ocdskit/tests/__init__.py
import sys
from difflib import ndiff
from io import BytesIO, TextIOWrapper
from pathlib import Path
from unittest.mock import patch


def path(filename):
    return Path("tests") / "fixtures" / filename


def read(filename, mode="rt", encoding=None, **kwargs):
    with path(filename).open(mode, encoding=encoding, **kwargs) as f:
        return f.read()


def run_streaming(capsys, monkeypatch, main, args, stdin):
    if not isinstance(stdin, bytes):
        stdin = b"".join(read(filename, "rb") for filename in stdin)

    with patch("sys.stdin", TextIOWrapper(BytesIO(stdin))):
        monkeypatch.setattr(sys, "argv", ["ocdskit", *args])
        main()

    return capsys.readouterr()


def assert_streaming(capsys, monkeypatch, main, args, stdin, expected):
    actual = run_streaming(capsys, monkeypatch, main, args, stdin)

    if not isinstance(expected, str):
        expected = "".join(read(filename) for filename in expected)

    assert actual.out == expected, "".join(ndiff(actual.out.splitlines(1), expected.splitlines(1)))
