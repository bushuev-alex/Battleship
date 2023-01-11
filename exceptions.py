class InputException(Exception):
    pass


class InputTypeException(InputException):
    def __str__(self):
        return "You should enter 2 numbers!"


class CoordinatesException(InputException):
    def __str__(self):
        return "Coordinates should be from 1 to 6!"


class ShotOnFieldException(InputException):
    def __str__(self):
        return 'This cell is already shot! Choose another one!'
