from dataclasses import dataclass
from typing import NamedTuple


@dataclass(slots=True, frozen=True)
class ShipCoordinates:
    row_start: int
    row_end: int
    col_start: int
    col_end: int


class ShotCoordinates(NamedTuple):
    row: int
    col: int
