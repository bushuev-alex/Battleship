from field import Field
import numpy as np


class UserGamer:

    def __init__(self, user_field: Field, ai_field: Field):
        self.user_field = user_field.field
        self.ai_field = ai_field.field


class AIGamer:

    def __init__(self, user_field: Field, ai_field: Field):
        self.user_field = user_field.field
        self.ai_field = ai_field.field


if __name__ == "__main__":
    user = UserGamer()
    print(user.user_field)
