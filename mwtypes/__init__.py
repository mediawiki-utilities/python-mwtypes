"""
This library provides a set of standardized types to be used when processing
MediaWiki data.  All of the types in this package make use of jsonable
(https://github.com/halfak/python-jsonable) and therefor can be trivially
serialized as JSON documents.

License: MIT -- see https://github.com/mediawiki-utilities/python-mwtypes
"""
from .namespace import Namespace
from .page import Page
from .revision import Revision
from .user import User
from .log_item import LogItem
from .timestamp import Timestamp

__version__ = "0.2.0"

__all__ = (Namespace, Page, Revision, User, LogItem, Timestamp)
