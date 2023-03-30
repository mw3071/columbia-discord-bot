from student import Student
import pytest

s = None

def test_add_class(s):
    print('testing add class')
    s.add_class('test-class')
    assert s.classes == ['test-class']
    print('done')

def test_add_prof(s):
    print('testing add profs')
    s.add_prof('test-prof')
    assert s.profs == ['test-prof']
    print('done')

def test_remove_class(s):
    print('testing remove class')
    s.remove_class('test-class')
    assert s.classes == []
    print('done')

def test_remove_prof(s):
    print('testing remove profs')
    s.remove_prof('test-prof')
    assert s.profs == []
    print('done')

def test_set_uni(s):
    print('testing set uni')
    s.set_uni('uni-test')
    assert s.uni == 'uni-test'

def test_get_classes(s):
    assert s.get_classes() == ['test-class']

def test_get_profs(s):
    assert s.get_profs() == ['test-prof']

def run_all():
    print('running tests')
    s = Student('test-username', 'test-uni')
    test_set_uni(s)
    test_add_class(s)
    test_add_prof(s)
    test_get_classes(s)
    test_get_profs(s)
    test_remove_class(s)
    test_remove_prof(s)
    print('all tests complete')

run_all()