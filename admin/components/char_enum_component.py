from admin.components import WebComponent
from typing import Type
from tortoise.models import Model


class CharEnumComponent(WebComponent):

    def __init__(self, model: Type[Model], field_name: str, form_id:str, value: str = None):
        self.model = model
        self.form_id = form_id
        self.field_name = field_name
        self.options = self.__get_choices__()
        if value:
            self.__set_value__(value)
        self.constraints = self.model._meta.fields_map[self.field_name].contraints
        self.allow_null = self.model._meta.fields_map[self.field_name].null
        self.default = self.model._meta.fields_map[self.field_name].default
        if not self.default:
            self.help_text = "This field is required."
        else:
            self.help_text = "Select from the options only"


    def  __get_choices__(self):
        a = self.model._meta.field_map[self.field_name].enum_type
        b = a.__dict__['_member_map_'].values()
        return [{"value": v.__dict__['_value_'], "display": v.__dict__['_name_'], "selected":False } for v in b]

    def __set_value__(self, value: str) -> None:
        options = []
        for op in self.options:
            if value == op["value"]:
                rec = op
                rec["selected"] = True
                options.append(rec)
            else:
                options.append(op)
        self.options = options
        return

