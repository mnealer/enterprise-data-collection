from tortoise.models import Model
from typing import Type, Tuple


class Admin:

    def __init__(self):
        self.models = {}
        self.title = "Fast Admin"

    def register(self, model: Type[Model], list_display: Tuple = ("id",)) -> None:
        self.models[model.__name__] = model.describe()
        self.models[model.__name__]['list_display'] = list_display
        self.models[model.__name__]['model'] = model

    def model_list(self) -> Tuple:
        return tuple(self.models.keys())

