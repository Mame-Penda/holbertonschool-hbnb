from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')


# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True,
                                description='First name of the user'),
    'last_name': fields.String(required=True,
                               description='Last name of the user'),
    'email': fields.String(required=True,
                           description='Email of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        try:
            user_data = api.payload
            existing_user = facade.get_user_by_email(user_data['email'])
            if existing_user:
                return {'error': 'Email already registered'}, 400

            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'first_name': new_user.first_name,
                    'last_name': new_user.last_name,
                    'email': new_user.email}, 201

        except ValueError as error:
            return {'error': str(error)}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Get a list of all users"""
        users = facade.user_repo.get_all()
        return [{'id': user.id, 'first_name': user.first_name,
                 'last_name': user.last_name, 'email': user.email
                 } for user in users], 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'user is successfully retrieved')
    @api.response(404, 'the user does not exist')
    def get(self, user_id):
        """get user by his id"""
        user_id = facade.get_user(user_id)
        if not user_id:
            return {'error': 'the user does not exist'}, 404
        return {'id': user_id.id, 'first_name': user_id.first_name,
                'last_name': user_id.last_name, 'email': user_id.email}, 200

    @api.response(200, 'User details updated successfully')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'User not found')
    @api.expect(user_model)
    def put(self, user_id):
        """Update user details by ID"""
        user_data = api.payload
        try:
            user = facade.update_user(user_id, user_data)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
                }, 200
        except ValueError as error:
            return {'error': str(error)}, 400
        except KeyError as error:
            return {'error': str(error)}, 404
