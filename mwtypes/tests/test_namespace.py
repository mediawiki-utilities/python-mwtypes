import pickle

from ..namespace import Namespace


def test_namespace():
    # Minimal arguments
    n = Namespace(10, 'Foobar')
    assert n.id == 10
    assert n.name == 'Foobar'
    assert n.aliases == None
    assert n.case == None
    assert n.canonical == None
    assert n.content == None

    # All the arguments
    n = Namespace(10, 'Foobar', aliases={'Foob', 'Bar'}, case='first-upper',
                  canonical='Ferpbar', content=False)
    assert n.id == 10
    assert n.name == 'Foobar'
    assert n.aliases == {'Foob', 'Bar'}
    assert n.case == "first-upper"
    assert n.canonical == "Ferpbar"
    assert n.content == False

    # JSON and Pickle
    assert n == Namespace(n.to_json())
    assert n == pickle.loads(pickle.dumps(n))
