from student import Student
import pytest

s = None

def test_addclass(s):
    s.add_class('test-class')
    assert s.classes == ['test-class']
    print('done')

def run_all():
    print('running tests')
    s = Student('test-username', 'test-uni')
    test_addclass(s)
    print('done')

run_all()