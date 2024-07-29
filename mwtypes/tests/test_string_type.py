from ..string_type import StringType


class FooBar(StringType):
    __slots__ = ('foo', 'bar')

    def initialize(self, string, foo, bar):
        self.foo = foo
        self.bar = bar

def test_string_type():

    foobar = FooBar("foobar", 1, 2)
    assert foobar == "foobar"
    assert foobar.foo == 1
    assert foobar.bar == 2
