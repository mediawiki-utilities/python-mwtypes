# MediaWiki Types

This library provides a set of classes for working with MediaWiki data types.  
The point of this library is to help standardize different schemes and naming
patterns between the database, XML dumps and API responses.  

* **Installation:** ``pip install mwtypes``

## Types

* Contributor -- An 'id' and 'user_text' of a user
* Deleted -- The deleted/suppressed status of a revision or event
* Namespace -- Namespace ID and metadata ('aliases', 'canonical', 'content')
* Page -- Metadata about a page ('id', 'title', 'namespace', 'restrictions', etc.)
* Revision -- Metadata about a revision ('id', 'contributor', 'timestamp', etc.)
* Timestamp -- Basic operations and formatting of MediaWiki timestamp formats

## Timestamp example

    >>> import datetime, time
    >>> from mwtypes import Timestamp
    >>> Timestamp(1234567890)
    Timestamp('2009-02-13T23:31:30Z')
    >>> Timestamp(1234567890) == Timestamp("2009-02-13T23:31:30Z")
    True
    >>> Timestamp(1234567890) == Timestamp("20090213233130")
    True
    >>> Timestamp(1234567890) == Timestamp(datetime.datetime.utcfromtimestamp(1234567890))
    True
    >>> Timestamp(1234567890) == Timestamp(time.strptime("2009-02-13T23:31:30Z", "%Y-%m-%dT%H:%M:%SZ"))
    True
    >>> Timestamp(1234567890) == Timestamp(Timestamp(1234567890))
    True

You can also do math and comparisons of timestamps.::

    >>> from mwtypes import Timestamp
    >>> t = Timestamp(1234567890)
    >>> t
    Timestamp('2009-02-13T23:31:30Z')
    >>> t2 = t + 10
    >>> t2
    Timestamp('2009-02-13T23:31:40Z')
    >>> t += 1
    >>> t
    Timestamp('2009-02-13T23:31:31Z')
    >>> t2 - t
    9
    >>> t < t2
    True
