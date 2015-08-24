import jsonable

from .timestamp import Timestamp
from .util import none_or


class User(jsonable.Type):
    """
    Contributing user meta data.
    """
    __slots__ = ('id', 'text')

    def initialize(self, id=None, text=None):
        self.id = none_or(id, int)
        """
        Contributing user's identifier : `int` | None
        """

        self.text = none_or(text, str)
        """
        Username or IP address of the user at the time of the edit : `str` | None
        """

class Deleted(jsonable.Type):
    """
    Represents information about the deleted/suppressed status of a revision
    and it's associated data.
    """

    __slots__ = ('text', 'comment', 'user', 'restricted')

    def initialize(self, text=None, comment=None, user=None, restricted=None):
        self.text = none_or(text, bool)
        """
        Is the text of this revision deleted/suppressed? : `bool`
        """

        self.comment = none_or(comment, bool)
        """
        Is the comment of this revision deleted/suppressed? : `bool`
        """

        self.user = none_or(user, bool)
        """
        Is the user of this revision deleted/suppressed? : `bool`
        """

        self.restricted = none_or(restricted, bool)
        """
        Is the revision restricted? : `bool`
        """

    @classmethod
    def from_int(cls, integer):
        """
        Constructs a `Deleted` using the `tinyint` value of the `rev_deleted`
        column of the `revision` MariaDB table.
        DELETED_TEXT = 1;
        DELETED_COMMENT = 2;
        DELETED_USER = 4;
        DELETED_RESTRICTED = 8.
        """
        bin_string = bin(integer)

        return cls(
            text=len(bin_string) >= 1 and bin_string[-1] == "1",
            comment=len(bin_string) >= 2 and bin_string[-2] == "1",
            user=len(bin_string) >= 3 and bin_string[-3] == "1",
            restricted=len(bin_string) >= 4 and bin_string[-4] == "1"
        )

class Revision(jsonable.Type):
    """
    Revision metadata and text
    """
    __slots__ = ('id', 'timestamp', 'user', 'minor', 'comment',
                 'text', 'bytes', 'sha1', 'parent_id', 'model', 'format',
                 'deleted')

    User = User
    Deleted = Deleted

    def initialize(self, id, timestamp, user=None, minor=None,
                   comment=None, text=None, bytes=None, sha1=None,
                   parent_id=None, model=None, format=None, deleted=None):

        self.id = none_or(id, int)
        """
        Revision ID : `int`
        """

        self.timestamp = none_or(timestamp, Timestamp)
        """
        Revision timestamp : :class:`mwtypes.Timestamp`
        """

        self.user = self.User(user or self.User())
        """
        Contributing user metadata : :class:`~mwtypes.Revision.User`
        """

        self.minor = False or none_or(minor, bool)
        """
        Is revision a minor change? : `bool`
        """

        self.comment = none_or(comment, str)
        """
        Comment left with revision : `str`
        """

        self.text = none_or(text, str)
        """
        Content of text : `str`
        """

        self.bytes = none_or(bytes, int)
        """
        Number of bytes of content : `str`
        """

        self.sha1 = none_or(sha1, str)
        """
        sha1 hash of the content : `str`
        """

        self.parent_id = none_or(parent_id, int)
        """
        Revision ID of preceding revision : `int` | `None`
        """

        self.model = none_or(model, str)
        """
        TODO: ??? : `str`
        """

        self.format = none_or(format, str)
        """
        TODO: ??? : `str`
        """

        self.deleted = self.Deleted(deleted or self.Deleted())
        """
        The deleted/suppressed status of the revision.
        """
