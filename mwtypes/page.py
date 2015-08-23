import jsonable

from .util import none_or


class Page(jsonable.Type):
    """
    Page meta data.
    """
    __slots__ = ('id', 'title', 'namespace', 'redirect', 'restrictions')

    def initialize(self, id, title, namespace, redirect=None,
                   restrictions=None):
        self.id = int(id)
        """
        Page ID : `int`
        """

        self.title = str(title)
        """
        Page title (namespace excluded) : `str`
        """

        self.namespace = int(namespace)
        """
        Namespace ID : `int`
        """

        self.redirect = none_or(redirect, str)
        """
        Page name that the page redirects to : `str` | `None`
        """

        self.restrictions = none_or(restrictions, list)
        """
        A list of page editing restrictions : list( `str` ) | `None`
        """
