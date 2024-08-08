from typing import Type
from tortoise.models import Model


def get_enum_values(model_class: Type[Model], fieldname: str) -> list:
    """
    For a given Tortoise ORM model and a field that should be an enum Field
    this function returns a list of the values for the given field
    :param model_class:
    :param fieldname:
    :return list[]:
    """
    a = model_class.meta.field_map[fieldname].enum_type
    b = a.__dict__['_member_map_'].values()
    return [v for v in b]
