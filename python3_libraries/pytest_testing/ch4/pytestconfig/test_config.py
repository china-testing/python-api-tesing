import pytest


def test_option(pytestconfig):
    print('"foo" set to:', pytestconfig.getoption('foo'))
    print('"myopt" set to:', pytestconfig.getoption('myopt'))


@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo


@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt


def test_fixtures_for_options(foo, myopt):
    print('"foo" set to:', foo)
    print('"myopt" set to:', myopt)


def test_pytestconfig(pytestconfig):
    print('args            :', pytestconfig.args)
    print('inifile         :', pytestconfig.inifile)
    print('invocation_dir  :', pytestconfig.invocation_dir)
    print('rootdir         :', pytestconfig.rootdir)
    print('-k EXPRESSION   :', pytestconfig.getoption('keyword'))
    print('-v, --verbose   :', pytestconfig.getoption('verbose'))
    print('-q, --quiet     :', pytestconfig.getoption('quiet'))
    print('-l, --showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style      :', pytestconfig.getoption('tbstyle'))


def test_legacy(request):
    print('\n"foo" set to:', request.config.getoption('foo'))
    print('"myopt" set to:', request.config.getoption('myopt'))
    print('"keyword" set to:', request.config.getoption('keyword'))
