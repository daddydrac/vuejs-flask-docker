# services/users/project/api/users/admin.py


from flask import current_app

from project import bcrypt
from flask_admin.contrib.sqla import ModelView


class UsersAdminView(ModelView):
    column_searchable_list = (
        "username",
        "email",
    )
    column_editable_list = (
        "username",
        "email",
        "created_date",
    )
    column_filters = (
        "username",
        "email",
    )
    column_sortable_list = (
        "username",
        "email",
        "active",
        "created_date",
    )
    column_default_sort = ("created_date", True)

    def on_model_change(self, form, model, is_created):
        model.password = bcrypt.generate_password_hash(
            model.password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()
