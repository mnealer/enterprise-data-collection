from browser import document

from typing import List


class FormElement:
    def __init__(self, id: str, form, validators: List[str]):
        self.id = id
        self.status = True
        self.validators = validators
        self.form = form
        self.element = document[self.id]
        self.element.bind("input", self.validate)

    def validate(self, event):
        for validator_name in self.validators:
            validator = getattr(self, validator_name, None)
            if validator:
                if not validator(self.element.value):
                    self.status = False
                    break
        else:
            self.status = True

        if self.form:
            self.form.validate()

    def some_validator(self, value):
        # any custom validators can be added as methods of the class.
        # This is just an example of validators
        if value:
            return True
        else:
            return False


class FormClass:
    def __init__(self, elements: List[FormElement]):
        self.elements = elements

    def validate(self):
        for element in self.elements:
            # Calling validate method on each element in form
            element.validate()

        # Generally, usage would look something like this:


