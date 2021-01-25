import connexion

from swagger_server.models.alert import Alert  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util

from .default_handler import DefaultHandler

def get_ping():  # noqa: E501
    DefaultHandler.handle_get_ping()
    return 'OK'


def get_users_user_id(user_id, key=None):  # noqa: E501
    """Get User Info by User ID

    Retrieve the information of the user with the matching user ID. # noqa: E501

    :param user_id: Id of an existing user.
    :type user_id: int
    :param key: Your Api Key To Access This Site
    :type key: str

    :rtype: User
    """
    return 'do some magic!'


def get_users_user_id_alerts(user_id):  # noqa: E501
    """Get all alerts bound to a user

    Get a list of alert that the user owns # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: List[Alert]
    """
    return 'do some magic!'


def get_users_user_id_alerts_ticker(user_id, ticker):  # noqa: E501
    """Get alerts bound to user matches the ticker

    Get the alert of a specific ticker for a user # noqa: E501

    :param user_id: 
    :type user_id: str
    :param ticker: 
    :type ticker: str

    :rtype: List[Alert]
    """
    return 'do some magic!'


def get_users_user_id_alerts_ticker_alert_id(user_id, ticker, alert_id):  # noqa: E501
    """Get a specific alert by id

     # noqa: E501

    :param user_id: 
    :type user_id: str
    :param ticker: 
    :type ticker: str
    :param alert_id: 
    :type alert_id: str

    :rtype: Alert
    """
    return 'do some magic!'


def patch_users_user_id(user_id, body=None):  # noqa: E501
    """Update User Information

    Update the infromation of an existing user. # noqa: E501

    :param user_id: Id of an existing user.
    :type user_id: int
    :param body: Patch user properties to update.
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_user(body=None):  # noqa: E501
    """Create New User

    Create a new user. # noqa: E501

    :param body: Post the necessary fields for the API to create a new user.
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_users_user_id_alert(user_id, body=None):  # noqa: E501
    """Create an alert with expected rules

    Create a new alert for a specific ticker on a specific event # noqa: E501

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
