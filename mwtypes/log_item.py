"""
.. autoclass:: mwtypes.LogItem
    :members:

"""
import jsonable

from .timestamp import Timestamp
from .user import User
from .util import none_or


class Deleted(jsonable.Type):
    """
    Represents information about the deleted/suppressed status of a log item
    and it's associated data.

    :Attributes:

        .. autoattribute:: mwtypes.log_item.Deleted.action
            :annotation: = Is the action of this log item deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.log_item.Deleted.comment
            :annotation: = Is the text of this log item deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.log_item.Deleted.user
            :annotation: = Is the user of this log item deleted/suppressed? :
                           bool | None

        .. autoattribute:: mwtypes.log_item.Deleted.restricted
            :annotation: = Is the log item restricted? : bool | None
    """

    __slots__ = ('action', 'comment', 'user', 'restricted')

    def initialize(self, action=None, comment=None, user=None,
                   restricted=None):
        self.action = none_or(action, bool)
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
        Constructs a `Deleted` using the `tinyint` value of the `log_deleted`
        column of the `logging` MariaDB table.

        * DELETED_ACTION = 1
        * DELETED_COMMENT = 2
        * DELETED_USER = 4
        * DELETED_RESTRICTED = 8
        """
        bin_string = bin(integer)

        return cls(
            action=len(bin_string) >= 1 and bin_string[-1] == "1",
            comment=len(bin_string) >= 2 and bin_string[-2] == "1",
            user=len(bin_string) >= 3 and bin_string[-3] == "1",
            restricted=len(bin_string) >= 4 and bin_string[-4] == "1"
        )


class Page(jsonable.Type):
    """
    Log item page information

    :Attributes:

        .. autoattribute:: mwtypes.log_item.Page.namespace
            :annotation: = namespace ID : int

        .. autoattribute:: mwtypes.log_item.Page.title
            :annotation: = title : str
    """
    __slots__ = ('namespace', 'title')

    def initialize(self, namespace=None, title=None):
        self.namespace = none_or(namespace, int)
        self.title = none_or(title, str)


class LogItem(jsonable.Type):
    """
    Log item metadata

    :Attributes:
        .. autoattribute:: mwtypes.LogItem.id
            :annotation: = Log item ID : int

        .. autoattribute:: mwtypes.LogItem.timestamp
            :annotation: = Log item timestamp :
                           mwtypes.Timestamp | None

        .. autoattribute:: mwtypes.LogItem.user
            :annotation: = Contributing user metadata :
                           mwtypes.User | None

        .. autoattribute:: mwtypes.LogItem.page
            :annotation: = Contributing user metadata :
                           mwtypes.log_item.Page | None

        .. autoattribute:: mwtypes.LogItem.comment
            :annotation: = Comment left with log item : str | None

        .. autoattribute:: mwtypes.LogItem.type
            :annotation: = Content of text : str | None

        .. autoattribute:: mwtypes.LogItem.action
            :annotation: = Content of text : str | None

        .. autoattribute:: mwtypes.LogItem.text
            :annotation: = Content of text : str | None

        .. autoattribute:: mwtypes.LogItem.params
            :annotation: = Content of params : str | None

        .. autoattribute:: mwtypes.LogItem.deleted
            :annotation: = The deleted/suppressed status of the log item :
                           mwtypes.log_item.Deleted | None
    """
    __slots__ = ('id', 'timestamp', 'user', 'page', 'comment', 'type',
                 'action', 'text', 'params', 'deleted')

    Deleted = Deleted
    Page = Page

    def initialize(self, id, timestamp=None, user=None, page=None,
                   comment=None, type=None, action=None, text=None,
                   params=None, deleted=None):

        self.id = int(id)
        """
        Log item ID : `int`
        """

        self.timestamp = none_or(timestamp, Timestamp)
        """
        log item timestamp : :class:`mwtypes.Timestamp`
        """

        self.user = none_or(user, User)
        """
        Contributing user metadata : :class:`mwtypes.User`
        """

        self.page = none_or(page, self.Page)
        """
        Related page : :class:`mwtypes.log_item.Page`
        """

        self.comment = none_or(comment, str)
        """
        Comment left with log item : `str`
        """

        self.type = none_or(type, str)
        """
        Type of log item : `str`
        """

        self.action = none_or(action, str)
        """
        Action of log item : `str`
        """

        self.text = none_or(text, str)
        """
        Content of text : `str`
        """

        self.params = none_or(params, str)
        """
        Content of params : `str`
        """

        self.deleted = none_or(deleted, self.Deleted)
        """
        The deleted/suppressed status of the log item.
        """
