from mock import Mock
from modele_gateau import Gateau


def test_is_name_ok():
    test=Gateau("toto")
    assert False