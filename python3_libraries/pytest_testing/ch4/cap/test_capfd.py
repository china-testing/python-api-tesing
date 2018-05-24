def greeting(name):
    print('Hi,', name)


def test_greeting(capfd):
    greeting('Brian')
    out, err = capfd.readouterr()
    assert out == 'Hi, Brian\n'


def test_multiline(capfd):
    greeting('Brian')
    greeting('Nerd')
    out, err = capfd.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'


def test_disabling_capturing(capfd):
    print('this output is captured')
    with capfd.disabled():
        print('output not captured')
    print('this output is also captured')
