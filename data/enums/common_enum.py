from enum import Enum


class SearchMode(Enum):
    RETURN = "Return"
    ONY_WAY = "One-way"


class Way(Enum):
    ORIGIN = "origin"
    DESTINATION = "destination"
