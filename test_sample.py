import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def f():
    raise SystemExit(1)


def test_f_raises_systemexit():
    with pytest.raises(SystemExit):
        f()