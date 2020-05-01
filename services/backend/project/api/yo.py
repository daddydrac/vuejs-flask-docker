# services/users/project/api/ping.py


from flask_restplus import Namespace, Resource

yo_namespace = Namespace("yo")


class Yo(Resource):
    def get(self):
        return {"status": "success", "message": "Yo!"}


yo_namespace.add_resource(Yo, "")
