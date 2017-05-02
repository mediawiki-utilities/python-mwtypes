MediaWiki Types
===============
This library provides a set of standardized types to be used when processing
MediaWiki data.  All of the types in this package make use of `jsonable
<https://github.com/halfak/python-jsonable/>`_ and therefore can be trivially
serialized as JSON documents.

:Installation: ``pip install mwtypes``

This package is a work in progress, so many types are not implemented.  But
those types that *are* implemented are complete and well-tested.

Contents:

.. toctree::
    :maxdepth: 2

    revision
    page
    log_item
    timestamp
    namespace

Authors
-------
* Aaron Halfaker -- https://github.com/halfak

Pull requests welcome @ https://github.com/mediawiki-utilities/python-mwtypes


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
