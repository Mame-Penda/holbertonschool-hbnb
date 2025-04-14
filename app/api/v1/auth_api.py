from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
)
from app.services import facade

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    @api.response(200, 'Success')
    @api.response(401, 'Invalid credentials')
    @api.response(500, 'Internal server error')
    def post(self):
        """Authenticate user and return access and refresh JWT tokens"""
        credentials = api.payload  # Get the email and password from the request payload

        try:
            # Step 1: Retrieve the user based on the provided email
            user = facade.get_user_by_email(credentials['email'])
            
            # Step 2: Check if the user exists and the password is correct
            if not user or not user.verify_password(credentials['password']):
                return {'error': 'Invalid credentials'}, 401

            # Step 3: Create access and refresh tokens
            access_token = create_access_token(identity=str(user.id), additional_claims={'is_admin': user.is_admin})
            refresh_token = create_refresh_token(identity=str(user.id))

            # Step 4: Return the tokens to the client
            return {'access_token': access_token, 'refresh_token': refresh_token}, 200

        except Exception as e:
            return {'error': 'Internal server error'}, 500


@api.route('/refresh')
class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    @api.response(200, 'Success')
    @api.response(401, 'Invalid refresh token')
    def post(self):
        """Generate a new access token using a refresh token"""
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}, 200


@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    @api.response(200, 'Success')
    @api.response(401, 'Unauthorized')
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = get_jwt_identity()  # Retrieve the user's identity from the token
        return {'message': f'Hello, user {current_user}'}, 200
