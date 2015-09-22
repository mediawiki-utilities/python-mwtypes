"""
.. autoclass:: mwtypes.Page
    :members:
"""
import jsonable

from .util import none_or


class Page(jsonable.Type):
    """
    Page metadata

    :Attributes:

        .. autoattribute:: mwtypes.Page.id
            :annotation: = Page ID : int

        .. autoattribute:: mwtypes.Page.title
            :annotation: = Page title: str

        .. autoattribute:: mwtypes.Page.namespace
            :annotation: = Namespace ID: str

        .. autoattribute:: mwtypes.Page.redirect
            :annotation: = Page name that this page redirects to : str | None

        .. autoattribute:: mwtypes.Page.restrictions
            :annotation: = A list of page editing restrictions :
                           list( `str` ) | `None`

    """
    __slots__ = ('id', 'title', 'namespace', 'redirect', 'restrictions')

    def initialize(self, id=None, title=None, namespace=None, redirect=None,
                   restrictions=None):
        self.id = none_or(id, int)
        """
        Page ID : `int`
        """

        self.title = none_or(title, str)
        """
        Page title (namespace excluded) : `str`
        """

        self.namespace = none_or(namespace, int)
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
