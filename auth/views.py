from flask_restx import Resource, Namespace,fields
from flask import request
from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_namespace = Namespace('auth',description="namespace for authentication")


signup_model=auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'username':fields.String(required=True),
        'email':fields.String(required=True),
        'password':fields.String(required=True),

    }
)


@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    def post(self):
        """
            Create a new user account
        """
        data=request.get_json()
        new_user = User(
            usename=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))
        )

        new_user.save()






@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Generate a JWT pair
        """
        pass
