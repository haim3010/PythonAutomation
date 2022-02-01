import pytest

from Automation.Magic_List import MagicList


def test_skip_boundary_check_with_0():
    # Given a magic list
    # When accessing it with "valid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()
    a[0] = 5
    assert a[0] == 5


def test_skip_boundary_check_with_valid_boundary_advanced():
    # Given a magic list
    # When accessing it with "valid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()
    for i in range(10):
        assert a == list(range(i))
        a[i] = i


def test_skip_boundary_check_with_valid_negative_boundary_advanced():
    # Given a magic list
    # When accessing it with "valid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()
    for i in range(10):
        assert a == list(range(i))
        a[-1] = i


def test_skip_boundary_check_with_minus_one():
    # Given a magic list
    # When accessing it with "valid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()
    a[-1] = 5


@pytest.mark.parametrize("val", range(2, 10))
def test_skip_boundary_check_with_bigger_gap(val):
    # Given a magic list
    # When accessing it with "invalid"  boundary check
    # We wish to add the value to the list.
    a = MagicList()

    with pytest.raises(IndexError):
        a[val] = 5


@pytest.mark.parametrize("val", range(2, 10))
def test_skip_boundary_check_with_negative_indexes(val: int):
    # Given a magic list
    # When accessing it with "invalid" boundary check
    # We wish to add the value to the list.
    a = MagicList()
    with pytest.raises(IndexError):
        a[-val] = 5


if __name__ == '__main__':
    pytest.main()