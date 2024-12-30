from dataclasses import dataclass
@dataclass
class Neighbor:

    name: str
    direction: str

@dataclass
class Country:

    name: str
    rank: str
    year: str
    gdppc: str
    neighbors: list[Neighbor]

@dataclass
class Data:

    countrys: list[Country]

