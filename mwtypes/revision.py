"""
.. autoclass:: mwtypes.Revision
    :members:

"""
import jsonable

from .page import Page
from .slots import Slots
from .timestamp import Timestamp
from .user import User
from .util import none_or


class Deleted(jsonable.Type):
    """
    Represents information about the deleted/suppressed status of a revision
    and it's associated data.

    :Attributes:

        .. autoattribute:: mwtypes.revision.Deleted.text
            :annotation: = Is the main slot content of this revision
                           deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.revision.Deleted.comment
            :annotation: = Is the text of this revision deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.revision.Deleted.user
            :annotation: = Is the user of this revision deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.revision.Deleted.restricted
            :annotation: = Is the revision restricted? : bool | None
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

        * DELETED_TEXT = 1
        * DELETED_COMMENT = 2
        * DELETED_USER = 4
        * DELETED_RESTRICTED = 8
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

    :Attributes:
        .. autoattribute:: mwtypes.Revision.id
            :annotation: = Revision ID : int

        .. autoattribute:: mwtypes.Revision.timestamp
            :annotation: = Revision timestamp : mwtypes.Timestamp | None

        .. autoattribute:: mwtypes.Revision.user
            :annotation: = Contributing user metadata : mwtypes.User` | None

        .. autoattribute:: mwtypes.Revision.page
            :annotation: = Page metadata : mwtypes.Page | None

        .. autoattribute:: mwtypes.Revision.minor
            :annotation: = Is revision a minor change? : bool | None

        .. autoattribute:: mwtypes.Revision.comment
            :annotation: = Comment left with revision : str | None

        .. autoattribute:: mwtypes.Revision.text
            :annotation: = Content of text : str | None

        .. autoattribute:: mwtypes.Revision.bytes
            :annotation: = Number of bytes of content : int | None

        .. autoattribute:: mwtypes.Revision.sha1
            :annotation: = sha1 hash of the content : str | None

        .. autoattribute:: mwtypes.Revision.parent_id
            :annotation: = Revision ID of preceding revision : int | None

        .. autoattribute:: mwtypes.Revision.model
            :annotation: = TODO: ??? : str | None

        .. autoattribute:: mwtypes.Revision.format
            :annotation: = TODO: ??? : str | None

        .. autoattribute:: mwtypes.Revision.deleted
            :annotation: = The deleted/suppressed status of the revision :
                           mwtypes.revision.Deleted | None

        .. autoattribute:: mwtypes.Revision.slots
            :annotation: = The content of the revision :
                           mwtypes.Slots | None
    """
    __slots__ = ('id', 'timestamp', 'user', 'page', 'minor', 'comment',
                 'slots', 'parent_id', 'deleted')

    User = User
    Deleted = Deleted

    def initialize(self, id, timestamp=None, user=None, page=None, minor=None,
                   comment=None, slots=None, parent_id=None, deleted=None):

        self.id = none_or(id, int)
        """
        Revision ID : `int`
        """

        self.timestamp = none_or(timestamp, Timestamp)
        """
        Revision timestamp : :class:`mwtypes.Timestamp`
        """

        self.user = none_or(user, User)
        """
        Contributing user metadata : :class:`~mwtypes.User`
        """

        self.page = none_or(page, Page)
        """
        Page metadata : :class:`~mwtypes.Page`
        """

        self.minor = none_or(minor, bool)
        """
        Is revision a minor change? : `bool`
        """

        self.comment = none_or(comment, str)
        """
        Comment left with revision : `str`
        """

        self.parent_id = none_or(parent_id, int)
        """
        Revision ID of preceding revision : `int` | `None`
        """

        self.deleted = none_or(deleted, self.Deleted)
        """
        The deleted/suppressed status of the revision.
        """

        self.slots = none_or(slots, Slots)
        """
        The content of the revision
        """

        if self.slots is not None and 'main' in self.slots:
            main_slot = self.slots['main']
            self.text = none_or(main_slot.text, str)
            self.sha1 = none_or(main_slot.sha1, str)
            self.model = none_or(main_slot.model, str)
            self.format = none_or(main_slot.format, str)
            self.bytes = none_or(main_slot.bytes, int)
        else:
            self.text = None
            self.sha1 = None
            self.model = None
            self.format = None
            self.bytes = None
