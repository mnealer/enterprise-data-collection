from admin.components import WebComponent
from admin import admin_models


class AdminTableComponent(WebComponent):
    def __init__(self, request):
        parts = request.url.split('/')
        self.model_name = parts[parts.index("model") + 1]
        self.admin_model = admin_models[admin_models]

    def render_header(self):
        return WebComponent.render_def(template="/admin/components/templates/table.html",
                                       definame="table_header",
                                       model=self.model_name,
                                       list_display= self.admin_model["list_display"])

    def render_body(self, data):
        return WebComponent.render_def(template="/admin/components/templates/table.html",
                                       defname="table_body",
                                       model=self.model_name,
                                       data=data,
                                       list_display= self.admin_model["list_display"])
