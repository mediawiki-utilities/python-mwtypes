import jsonable

from .util import none_or


class Contributor(jsonable.Type):
    """
    Contributor meta data.
    """
    __slots__ = ('id', 'user_text')

    def initialize(self, id=None, user_text=None):
        self.id = none_or(id, int)
        """
        Contributing user's identifier : `int` | None
        """

        self.user_text = none_or(user_text, str)
        """
        Username or IP address of the user at the time of the edit : `str` | None
        """
