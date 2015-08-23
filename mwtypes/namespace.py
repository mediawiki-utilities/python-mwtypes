import jsonable

from .util import none_or


class Namespace(jsonable.Type):
    """
    Namespace meta data.
    """

    __slots__ = ('id', 'name', 'aliases', 'case', 'canonical')

    def initialize(self, id, name, canonical=None, aliases=None, case=None,
                   content=None):

        self.id = int(id)
        """
        Namespace ID : `int`
        """

        self.name = str(name)
        """
        Namespace name : `str`
        """

        self.aliases = none_or(aliases, set)
        """
        Alias names for this namespace : set( `str` )
        """

        self.case = none_or(case, str)
        """
        Case sensitivity information : `str` | `None`
        """

        self.canonical = none_or(canonical, str)
        """
        Canonical name of the namespace : `str` | `None`
        """

        self.content = none_or(content, bool)
        """
        Is considered a content namespace? : `bool` | `None`
        """
