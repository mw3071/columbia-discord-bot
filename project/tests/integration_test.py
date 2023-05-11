import sys
sys.path.insert(1, '../')
import student

def test():
    print('running tests')
    s = student.Student('test-username', 'test-uni')

    s.add_class('test-class-1')
    assert s.classes == ['test-class-1']
    s.add_class('test-class-2')
    assert s.classes == ['test-class-1', 'test-class-2']

    s.add_prof('test-prof-1')
    assert s.profs == ['test-prof-1']
    s.add_prof('test-prof-2')
    assert s.profs == ['test-prof-1', 'test-prof-2']

    s.remove_class('test-class-1')
    assert s.classes == ['test-class-2']
    s.remove_class('test-class-2')
    assert s.classes == []

    s.remove_prof('test-prof-2')
    assert s.profs == ['test-prof-1']
    s.remove_prof('test-prof-1')
    assert s.profs == []
    