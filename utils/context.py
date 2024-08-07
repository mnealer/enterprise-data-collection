from fastapi import Request
from mako.template import Template
from typing import Dict, Any
from functools import lru_cache
from pathlib import Path


class TemplateNotFound(Exception):
    def __init__(self):
        pass


@lru_cache(maxsize=1012, typed=True)
def render_template(template_string: str, context: Dict[str, Any], request: Request = None) -> str:
    if not Path(template_string).exists():
        raise TemplateNotFound()
    template = Template(template_string)
    if request is not None:
        context["request"] = request

    return template.render(**context)
