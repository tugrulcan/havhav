from typing import List

from pydantic import BaseModel


class DogAPIResponse(BaseModel):
    facts: List[str]
    success: bool
