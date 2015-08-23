import jsonable

from .util import none_or


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
