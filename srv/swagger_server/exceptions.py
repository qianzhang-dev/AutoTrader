from connexion import ProblemException
from flask.wrappers import Response
from json import dumps

from .constants import SWAGGER_URL_PREFIX


class EmailAlreadyRegistered(ProblemException):
    def __init__(self, email: str, error_code: int = 409):
        self.message = f'Email {email} is already registered'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class AlertAlreadyCreated(ProblemException):
    def __init__(self, ticker: str, event_type: str, price: float, id: int, error_code: int = 409):
        self.message = f'Alert {ticker} {event_type} {price} is already created @ id = {id}'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class UserNotFound(ProblemException):
    def __init__(self, user_id: int, error_code: int = 404):
        self.message = f'User {user_id} is not found'
        self.error_code = error_code
        super(ProblemException, self).__init__()

class AlertNotFound(ProblemException):
    def __init__(self, alert_id: int, error_code: int = 404):
        self.message = f'Alert {alert_id} is not found'
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

class InvalidRequestBody(ProblemException):
    def __init__(self, error_code: int = 400):
        self.message = (
            'Request body is not a valid json or missing specific field. '
            f'Please visit {SWAGGER_URL_PREFIX} for the request body schematic.'
        )
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