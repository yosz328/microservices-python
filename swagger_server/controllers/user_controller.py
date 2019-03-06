import connexion
import six
import requests
import json

from swagger_server.models.get_lat_lon import GetLatLon  # noqa: E501
from swagger_server import util
from google_request import get_coordinades


def get_estimated(body):  # noqa: E501
    """obtener tiempo estimado

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    print(body)
    if connexion.request.is_json:
        #print ("hello")
        body = connexion.request.get_json()  # noqa: E501
        #change
        headers = {'Content-Type': 'application/json'}
        r = requests.post("http://52.168.132.142/v2/get_latlon", data=json.dumps(body), headers=headers)
        data = requests.post("http://52.168.132.142/v2/get_time", data=r, headers=headers)

    return  data.json()
