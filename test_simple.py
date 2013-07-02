from mergegettext import simple, files


BASE="""
#: a:2
test
"""


LOCAL = BASE.replace('a:2', 'a:3')
OTHER = BASE.replace('a:2', 'a:4')


def test_simple():
    assert simple(BASE, LOCAL, OTHER) == OTHER


def test_files(tmpdir, monkeypatch):
    tmpdir.join('base').write(BASE)
    tmpdir.join('local').write(LOCAL)
    tmpdir.join('other').write(OTHER)

    monkeypatch.chdir(tmpdir)
    files('base', 'local', 'other')
    result = tmpdir.join('local').read()
    assert result == OTHER

