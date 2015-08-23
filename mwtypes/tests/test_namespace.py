import pickle

from nose.tools import eq_

from ..namespace import Namespace


def test_namespace():
    # Minimal arguments
    n = Namespace(10, 'Foobar')
    eq_(n.id, 10)
    eq_(n.name, 'Foobar')
    eq_(n.aliases, None)
    eq_(n.case, None)
    eq_(n.canonical, None)
    eq_(n.content, None)

    # All the arguments
    n = Namespace(10, 'Foobar', aliases={'Foob', 'Bar'}, case='first-upper',
                  canonical='Ferpbar', content=False)
    eq_(n.id, 10)
    eq_(n.name, 'Foobar')
    eq_(n.aliases, {'Foob', 'Bar'})
    eq_(n.case, "first-upper")
    eq_(n.canonical, "Ferpbar")
    eq_(n.content, False)

    # JSON and Pickle
    eq_(n, Namespace(n.to_json()))
    eq_(n, pickle.loads(pickle.dumps(n)))
