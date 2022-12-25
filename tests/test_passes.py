import pytest

from tests.expectations import EXPECTED
from tests.utils import get_contract_analysis


@pytest.mark.parametrize("filename,expected", EXPECTED)
def test_passes(filename, expected):
    path = f"examples/{filename}.vy"
    actual = get_contract_analysis(path)
    assert actual == expected
