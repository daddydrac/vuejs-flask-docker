# services/users/project/api/test.py


from flask_restplus import Namespace, Resource

test_namespace = Namespace("test")


class Test(Resource):
    def get(self):
        return {"status": "success", "message": "test!"}


test_namespace.add_resource(Test, "")
