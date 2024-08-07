from admin.admin import Admin
from auth.models import Users, Session


admin_models = Admin()

admin_models.register(Users, list_display=("id", "username"))
admin_models.register(Session)




