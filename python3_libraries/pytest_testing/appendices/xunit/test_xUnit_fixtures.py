def setup_module(module):
    print(f'\nsetup_module() for {module.__name__}')


def teardown_module(module):
    print(f'teardown_module() for {module.__name__}')


def setup_function(function):
    print(f'setup_function() for {function.__name__}')


def teardown_function(function):
    print(f'teardown_function() for {function.__name__}')


def test_1():
    print('test_1()')


def test_2():
    print('test_2()')


class TestClass:
    @classmethod
    def setup_class(cls):
        print(f'setup_class() for class {cls.__name__}')

    @classmethod
    def teardown_class(cls):
        print(f'teardown_class() for {cls.__name__}')

    def setup_method(self, method):
        print(f'setup_method() for {method.__name__}')

    def teardown_method(self, method):
        print(f'teardown_method() for {method.__name__}')

    def test_3(self):
        print('test_3()')

    def test_4(self):
        print('test_4()')
