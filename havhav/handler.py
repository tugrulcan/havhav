from typing import Any, List

from pydantic import BaseModel
from requests import Session
from requests.adapters import HTTPAdapter
from requests_toolbelt.sessions import BaseUrlSession

from havhav.models import DogAPIResponse

BASE_URL = "https://dog-api.kinduff.com/api/facts"


class DogAPIHandler(BaseModel):
    session: BaseUrlSession = Session()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.session = BaseUrlSession(base_url=BASE_URL)
        # Set base url for requests
        self.session.headers.update({"Content-Type": "application/json"})
        self.session.headers.update({"Accept": "application/json"})
        self.session.headers.update({"User-Agent": "havhav"})

        adapter = HTTPAdapter(max_retries=3)
        self.session.mount(BASE_URL, adapter)

    def get_dog_facts(self, number_of_facts: int = 1) -> List[str]:
        """
        Get dog facts from API

        :param number_of_facts:
        :return:
        """
        response = self.fetch_facts(number_of_facts=number_of_facts)
        return [fact for fact in response.facts]

    def fetch_facts(self, number_of_facts: int) -> DogAPIResponse:
        response = self.session.get(
            url=BASE_URL,
            params={"number": number_of_facts},
            timeout=3,
        )
        return DogAPIResponse(**response.json())

    class Config:
        arbitrary_types_allowed = True


def get_dog_facts(number_of_facts: int = 1) -> List[str]:
    return DogAPIHandler().get_dog_facts(number_of_facts=number_of_facts)
