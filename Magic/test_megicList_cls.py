from dataclasses import dataclass

import pytest

from Automation.Magic_List.MagicList import MagicList

@dataclass
class Person(object):
    age: int = 1


def test_magic_list_support_initialized_assigned_types():
    # Given a magic list with cls type of Person
    # When accessing "valid" boundary
    # We will have a new person when accessing it.
    a = MagicList(cls_type=Person)
    a[0].age = 5
    assert a[0] == Person(age=5)


def test_magic_list_support_assigned_types_but_enforce_extend_boundary_check():
    # Given a magic list with cls type of Person
    # When accessing "invalid" boundary
    # We won't have a new person when accessing it.
    a = MagicList(cls_type=Person)
    with pytest.raises(IndexError):
        a[1].age = 5


if __name__ == '__main__':
    pytest.main()