import pytest


def test_fn_1():
    print(' == test fn 1 == ')


def test_fn_2():
    print(' == test fn 2 == ')


@pytest.mark.xfail
def test_fn_xfail():
    assert 1 == 0


@pytest.mark.skip(reason="skip forever")
def test_fn_skip():
    assert 1 == 0




# def test_fn_1():
#     print(" === 1 == ")
#
# def test_fn_2():
#     print(" === 2 == ")