from connexion import ProblemException
from flask.wrappers import Response
from json import dumps


class EmailAlreadyRegistered(ProblemException):
    def __init__(self, email: str, error_code: int = 409):
        self.message = f'Email {email} is already registered'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class UserNotFound(ProblemException):
    def __init__(self, user_id: str, error_code: int = 404):
        self.message = f'User {user_id} is not found'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class AuthorizationFailure(ProblemException):
    def __init__(self, username: str, error_code: int = 401):
        self.message = f'User {username} failed to authorize'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class NoAuthorization(ProblemException):
    def __init__(self, error_code: int = 401):
        self.message = 'Authorization is required while "Authorization" header is empty'
        self.error_code = error_code
        super(ProblemException, self).__init__()
    
def render_exception_message(exception):
    return Response(
        response=dumps({
            "error_message": exception.message,
            "error_code": exception.error_code
        }),
        status=exception.error_code,
        content_type='application/json'
    )