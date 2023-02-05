class InputException(Exception):
    pass


class InputTypeException(ValueError):
    def __str__(self):
        return "You should enter 2 numbers!"


class CoordinatesException(TypeError):
    def __str__(self):
        return "Coordinates should be from 1 to 6!"


class BusyCellOnFieldException(InputException):
    def __str__(self):
        return 'This cell is already shot! Choose another one!'
