"""
.. autoclass:: mwtypes.Namespace
    :members:
"""
import jsonable

from .util import none_or


class Namespace(jsonable.Type):
    """
    Namespace metadata.

    :Attributes:

        .. autoattribute:: mwtypes.Namespace.id
            :annotation: = Namespace ID : int

        .. autoattribute:: mwtypes.Namespace.name
            :annotation: = Namespace name : str

        .. autoattribute:: mwtypes.Namespace.aliases
            :annotation: = Alias names for this namespace : set(str)

        .. autoattribute:: mwtypes.Namespace.case
            :annotation: = Case sensitivity information : str | None

        .. autoattribute:: mwtypes.Namespace.canonical
            :annotation: = Canonical name of the namespace : str | None

        .. autoattribute:: mwtypes.Namespace.content
            :annotation: = Is considered a content namespace? : `bool` | `None`

    """

    __slots__ = ('id', 'name', 'aliases', 'case', 'canonical', 'content')

    def initialize(self, id, name, canonical=None, aliases=None, case=None,
                   content=None):

        self.id = int(id)

        self.name = str(name)

        self.aliases = none_or(aliases, set)

        self.case = none_or(case, str)

        self.canonical = none_or(canonical, str)

        self.content = none_or(content, bool)
