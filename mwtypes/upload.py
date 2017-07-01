"""
.. autoclass:: mwtypes.Upload
    :members:

"""
import jsonable

from .timestamp import Timestamp
from .user import User
from .util import none_or


class Upload(jsonable.Type):
    """
    Upload event metadata

    :Attributes:
        .. autoattribute:: mwtypes.Upload.timestamp
            :annotation: = Upload timestamp : mwtypes.Timestamp | None

        .. autoattribute:: mwtypes.Upload.user
            :annotation: = Contributing user metadata : mwtypes.User` | None

        .. autoattribute:: mwtypes.Upload.comment
            :annotation: = Comment left with upload : str | None

        .. autoattribute:: mwtypes.Upload.filename
            :annotation: = File name without "File:" prefix and "_"
                           instead of spaces : str | None

        .. autoattribute:: mwtypes.Upload.source
            :annotation: = A URI : str | None

        .. autoattribute:: mwtypes.Upload.size
            :annotation: = Number of bytes of content : int | None

    """
    __slots__ = ('timestamp', 'user', 'comment', 'filename', 'source', 'size')

    def initialize(self, timestamp=None, user=None, comment=None,
                   filename=None, source=None, size=None):

        self.timestamp = none_or(timestamp, Timestamp)
        """
        Upload timestamp : mwtypes.Timestamp | None
        """

        self.user = none_or(user, User)
        """
        Contributing user metadata : :class:`~mwtypes.User`
        """

        self.comment = none_or(comment, str)
        """
        Comment left with upload : str | None
        """

        self.filename = none_or(filename, str)
        """
        File name without "File:" prefix and "_" instead of spaces : str | None
        """

        self.source = none_or(source, str)
        """
        A URI : str | None
        """

        self.size = none_or(size, int)
        """
        Number of bytes of content : int | None
        """
