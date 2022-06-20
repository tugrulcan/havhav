from typing import List

import pytest

from havhav.handler import DogAPIHandler
from havhav.models import DogAPIResponse


@pytest.fixture(scope="module", autouse=True)
def handler() -> DogAPIHandler:
    return DogAPIHandler()


def test_fetch_dog_fact(handler: DogAPIHandler) -> None:
    count = 1
    response: DogAPIResponse = handler.fetch_facts(number_of_facts=count)
    assert response.success is True
    assert response.facts is not None
    assert len(response.facts) == count

    count = 999
    response = handler.fetch_facts(number_of_facts=count)
    assert response.success is True
    assert response.facts is not None
    assert len(response.facts) == 100


def test_get_dog_fact(handler: DogAPIHandler) -> None:
    """
    Test get_dog_fact
    """
    # Get dog facts from API
    count = 1
    facts: List[str] = handler.get_dog_facts(number_of_facts=count)
    assert len(facts) == count
    assert facts[0] is not None
    assert facts[0] != ""
