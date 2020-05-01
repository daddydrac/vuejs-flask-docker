# services/users/project/api/ping.py


from flask_restplus import Namespace, Resource

foo_namespace = Namespace("foo")


class Foo(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


foo_namespace.add_resource(Foo, "")