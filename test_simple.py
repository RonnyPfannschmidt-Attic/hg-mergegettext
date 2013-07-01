from mergegettext import simple


BASE="""
#: a:2
test
"""


LOCAL = BASE.replace('a:2', 'a:3')
OTHER = BASE.replace('a:2', 'a:4')


def test_simple():
    assert simple(BASE, LOCAL, OTHER) == OTHER
