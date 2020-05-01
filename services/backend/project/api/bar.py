# services/users/project/api/ping.py


from flask_restplus import Namespace, Resource

bar_namespace = Namespace("bar")


class Bar(Resource):
    def get(self):
        return {"status": "success", "message": "baz!"}


bar_namespace.add_resource(Bar, "")
