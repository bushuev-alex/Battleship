from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ShipCoordinates:
    row_start: int
    row_end: int
    col_start: int
    col_end: int


@dataclass(slots=True, frozen=True)
class ShotCoordinates:
    row: int
    col: int
