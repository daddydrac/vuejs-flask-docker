# services/users/project/api/__init__.py


from flask_restplus import Api

from project.api.auth import auth_namespace
from project.api.ping import ping_namespace
from project.api.users.views import users_namespace
from project.api.users.foo import foo_namespace
from project.api.bar import bar_namespace
from project.api.yo import yo_namespace
from project.api.test import test_namespace

api = Api(version="1.0", title="Users API", doc="/swagger")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(auth_namespace, path="/auth")
api.add_namespace(foo_namespace, path="/foo")
api.add_namespace(bar_namespace, path="/bar")
api.add_namespace(yo_namespace, path="/yo")
api.add_namespace(test_namespace, path="/test")

