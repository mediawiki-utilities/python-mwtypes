"""
.. autoclass:: mwtypes.Slots
    :members:

.. autoclass:: mwtypes.Content
    :members:
"""
import jsonable

from .util import none_or


class Slots(jsonable.Type):
    __slots__ = ('sha1', 'contents')

    def initialize(self, sha1, contents):
        self.sha1 = none_or(sha1, str)
        """
        A sha1 generated from all of the contents
        """

        self.contents = {
            name: none_or(content, Content)
            for name, content in contents.items()}
        """
        The contents of the slots
        """

    def __getitem__(self, name):
        return self.contents[name]

    def __contains__(self, name):
        return name in self.contents

    def get(self, name, default=None):
        if name in self.contents:
            return self.content[name]
        else:
            return default


class Content(jsonable.Type):
    __slots__ = ('role', 'origin', 'model', 'format', 'deleted', 'location',
                 'bytes', 'sha1', 'text')

    def initialize(self, role=None, origin=None, model=None, format=None,
                   deleted=None, location=None, bytes=None, sha1=None,
                   text=None):
        self.role = none_or(role, str)
        """
        The role-name of the content slot
        """

        self.origin = none_or(origin, int)
        """
        The origin of the content
        """

        self.model = none_or(model, str)
        """
        The model of the content
        """

        self.format = none_or(format, str)
        """
        The format of the content
        """

        self.deleted = none_or(deleted, bool)
        """
        True if the text has been deleted/suppressed.
        """

        self.location = none_or(location, str)
        """
        A URI representing the location of the content.
        """

        self.bytes = none_or(bytes, int)
        """
        The byte length of the content
        """

        self.sha1 = none_or(sha1, str)
        """
        A sha1 hash of the content
        """

        self.text = none_or(text, str)
        """
        A text representation of the content
        """
