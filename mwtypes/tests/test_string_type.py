from nose.tools import eq_

from ..string_type import StringType


class FooBar(StringType):
    __slots__ = ('foo', 'bar')

    def initialize(self, string, foo, bar):
        self.foo = foo
        self.bar = bar

def test_string_type():

    foobar = FooBar("foobar", 1, 2)
    eq_(foobar, "foobar")
    eq_(foobar.foo, 1)
    eq_(foobar.bar, 2)
