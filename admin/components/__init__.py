from mako.template import Template
from functools import lru_cache
from pathlib import Path


class TemplateNotFound(Exception):
    def __init__(self):
        pass


class WebComponent:

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def render_template(cls, template, **kwargs):

        return template.render(**kwargs)

    @classmethod
    @lru_cache(maxsize=1024, typed=True)
    def render_def(cls, template, defname, **kwargs):
        if not Path(template).exists():
            raise TemplateNotFound()
        template = Template(template)
        return template.get_def(defname).render(**kwargs)


class AdminBreadCrumb(WebComponent):
    def __init__(self, url):
        self.url = url
        self.template = """<nav class="breadcrumb">
                        <ul>
                            % for item in breadcrumbs
                            ${breadcrumb_item(url=item['url'], icon=item['icon'], is_last=loop.last}
                            % endfor
                        </ul>
                    </nav>
                    
                    
                    <%def name="breadcrumb_item()">
                        <li class="${'is-active' if is-last}">
                            <a href="${url}">
                                <span class="icon is-small">
                                    <i class="fas ${icon}"></i>
                                </span>
                                <span>${title}</span>
                            </a>
                        </li>
                    </%def>
        """

    def render(self):
        return Template(self.template).render(breadcrumbs=self.__create_crumbs__())

    def __create_crumbs__(self) -> list:
        parts = self.url.split("/")
        if "model" in parts and "new" in parts:
            model_name = parts[parts.index("model") + 1]
            return [
                {"url": "/admin/", "icon": "home", "title": "Home", "last": False},
                {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last": False},
                {"url": self.url, "icon": "new", "title": "Edit", "last": True}
            ]

        elif "edit" in parts:
            model_name = parts[parts.index("model") + 1]
            record_id = parts[parts.index("record") + 1]
            return [
                {"url": "/admin/", "icon": "home", "title": "Home", "last": False},
                {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last": False},
                {"url": f"/admin/mode;{model_name}/record/{record_id}", "icon": "record", "title": record_id, "last": False},
                {"url": self.url, "icon": "edit", "title": "Edit", "last": True}
            ]

        elif "record" in parts:
            model_name = parts[parts.index("model") + 1]
            record_id = parts[parts.index("record") + 1]
            return [
                {"url": "/admin/", "icon": "home", "title": "Home", "last": False},
                {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last": False},
                {"url": self.url, "icon": "record", "title": record_id, "last": True},
            ]

        elif "model" in parts:
            model_name = parts[parts.index("model") + 1]
            return [
                {"url": "/admin/", "icon": "home", "title": "Home", "last": False},
                {"url": f"/admin/model/{model_name}", "icon": "home", "title": "Home", "last": True},
            ]
        else:
            return [
                {"url": "/admin/", "icon": "home", "title": "Home", "last": True}]


class AdminPagination(WebComponent):
    def __init__(self, request, page_count:int, current_page:int) -> None:
        if "?" in request.url:
            self.url = request.url.split("?")[0]
        else:
            self.url = request.url
        self.page_count = page_count
        self.current_page = current_page

    def render(self):
        if self.page_count <= 6:
            defname = "lt6_pagination"
        elif self.current_page <=3:
            defname = "near_start_pagination"
        elif self.page_count - self.current_page <= 3:
            defname= "near_end_pagination"
        else:
            defname = "standard_pagination"
        return WebComponent.render_def(template="/admin/components/templates/pagination.html",
                                       defname=defname,
                                       current_page=self.current_page,
                                       page_count=self.page_count,
                                       url=self.url)



