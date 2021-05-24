from io import StringIO
from toolbox.lib import prime_n


def test_prime_n():
    assert type(prime_n(58)) == str
