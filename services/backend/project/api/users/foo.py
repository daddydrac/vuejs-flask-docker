from flask_restplus import Namespace, Resource

foo_namespace = Namespace("foo")


class Foo(Resource):
    def get(self):
        division_by_zero = 1 / 0
        return division_by_zero


foo_namespace.add_resource(Foo, "")
