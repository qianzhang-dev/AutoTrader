import connexion
import six

from swagger_server.models.alert_request import AlertRequest  # noqa: E501
from swagger_server.models.alert_response import AlertResponse  # noqa: E501
from swagger_server.models.monitor_request import MonitorRequest  # noqa: E501
from swagger_server.models.monitor_response import MonitorResponse  # noqa: E501
from swagger_server.models.user_request import UserRequest  # noqa: E501
from swagger_server.models.user_response import UserResponse  # noqa: E501
from swagger_server import util


def delete_users_user_id(user_id):  # noqa: E501
    """delete_users_user_id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_users_user_id_alerts_ticker_alert_id(user_id, ticker, alert_id):  # noqa: E501
    """delete_users_user_id_alerts_ticker_alert_id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param ticker: The ticker of alerts to be specified
    :type ticker: str
    :param alert_id: Id of an existing alert
    :type alert_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_users_user_id_monitors_monitor_id(user_id, monitor_id):  # noqa: E501
    """delete_users_user_id_monitors_monitor_id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param monitor_id: Id of the registered monitor
    :type monitor_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_ping():  # noqa: E501
    """Healthcheck Endpoint

    Healthcheck endpoint of the current site # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_users_user_id(user_id):  # noqa: E501
    """Get User Info by User ID

    Retrieve the information of the user with the matching user ID. # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int

    :rtype: UserResponse
    """
    return 'do some magic!'


def get_users_user_id_alerts(user_id):  # noqa: E501
    """Get all alerts bound to a user

    Get a list of alert that the user owns # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int

    :rtype: List[AlertResponse]
    """
    return 'do some magic!'


def get_users_user_id_alerts_ticker(user_id, ticker):  # noqa: E501
    """Get alerts bound to user matches the ticker

    Get the alert of a specific ticker for a user # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param ticker: The ticker of alerts to be specified
    :type ticker: str

    :rtype: List[AlertResponse]
    """
    return 'do some magic!'


def get_users_user_id_alerts_ticker_alert_id(user_id, ticker, alert_id):  # noqa: E501
    """Get a specific alert by id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param ticker: The ticker of alerts to be specified
    :type ticker: str
    :param alert_id: Id of an existing alert
    :type alert_id: int

    :rtype: AlertResponse
    """
    return 'do some magic!'


def get_users_user_id_monitors(user_id, event_type):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param event_type: The list of eventTypes (e.g. upCross50MA,downCross100MA)
    :type event_type: str

    :rtype: List[MonitorResponse]
    """
    return 'do some magic!'


def get_users_user_id_monitors_monitor_id(user_id, monitor_id):  # noqa: E501
    """Your GET endpoint

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param monitor_id: Id of the registered monitor
    :type monitor_id: int

    :rtype: MonitorResponse
    """
    return 'do some magic!'


def patch_users_user_id(user_id, body=None):  # noqa: E501
    """Update User Information

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: UserResponse
    """
    if connexion.request.is_json:
        body = UserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def patch_users_user_id_alerts_ticker_alert_id(user_id, ticker, alert_id):  # noqa: E501
    """patch_users_user_id_alerts_ticker_alert_id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param ticker: The ticker of alerts to be specified
    :type ticker: str
    :param alert_id: Id of an existing alert
    :type alert_id: int

    :rtype: AlertResponse
    """
    return 'do some magic!'


def patch_users_user_id_monitors_monitor_id(user_id, monitor_id):  # noqa: E501
    """patch_users_user_id_monitors_monitor_id

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param monitor_id: Id of the registered monitor
    :type monitor_id: int

    :rtype: MonitorResponse
    """
    return 'do some magic!'


def post_login():  # noqa: E501
    """post_login

     # noqa: E501


    :rtype: UserResponse
    """
    return 'do some magic!'


def post_user(body=None):  # noqa: E501
    """Create New User

    Create a new user. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UserResponse
    """
    if connexion.request.is_json:
        body = UserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_users_user_id_alert(user_id, body=None):  # noqa: E501
    """Create an alert with expected rules

    Create a new alert for a specific ticker on a specific event # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AlertRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_users_user_id_monitor(user_id, body=None):  # noqa: E501
    """post_users_user_id_monitor

     # noqa: E501

    :param user_id: Id of an existing user
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MonitorRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


### Overwrite
from .ping_controller import PingController
from .user_controller import UserController
from .alert_controller import AlertController