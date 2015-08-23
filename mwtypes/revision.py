import jsonable

from .contributor import Contributor
from .deleted import Deleted
from .timestamp import Timestamp
from .util import none_or


class Revision(jsonable.Type):
    """
    Revision metadata and text
    """
    __slots__ = ('id', 'timestamp', 'contributor', 'minor', 'comment',
                 'text', 'bytes', 'sha1', 'parent_id', 'model', 'format',
                 'deleted')

    def initialize(self, id, timestamp, contributor=None, minor=None,
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

        self.contributor = Contributor(contributor or Contributor())
        """
        Contributor metadata : :class:`~mwtypes.Contributor`
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

        self.deleted = Deleted(deleted or Deleted())
        """
        The deleted/suppressed status of the revision.
        """
