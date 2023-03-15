
def func(x):
    return x + 1
def funx(x):
    return x + 1
def inc(s):
    return s + 2

def test_answerx():
    assert funx(4) == 5

def test_answer():
    assert func(3) == 5


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
    def test_answer(self):
        assert inc(3) == 5

    