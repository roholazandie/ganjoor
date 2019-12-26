from dataclasses import dataclass
from typing import List


@dataclass
class Verse:
    number: int
    text: str

@dataclass
class Poem:
    title: str
    verses: List[Verse]

@dataclass
class Poet:
    name: str
    description: str

