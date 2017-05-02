"""
.. autoclass:: mwtypes.User
    :members:

"""
import jsonable

from .util import none_or


class User(jsonable.Type):
    """
    Contributing user metadata.

    :Attributes:

        .. autoattribute:: mwtypes.User.id
            :annotation: = Contributing user's identifier : int | None

        .. autoattribute:: mwtypes.User.text
            :annotation: = Username or IP address of the user at the time of
                           the edit : str | None


    """
    __slots__ = ('id', 'text')

    def initialize(self, id=None, text=None):
        self.id = none_or(id, int)
        """
        Contributing user's identifier : int | None
        """

        self.text = none_or(text, str)
        """
        Username or IP address of the user at the time of the edit : str | None
        """
