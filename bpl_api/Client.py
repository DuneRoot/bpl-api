from importlib import import_module

from bpl_api.Connection import Connection
from bpl_api.Constants import API_ENDPOINTS
from bpl_api.Exceptions import BPLAPIException


class Client:

    def __init__(self, address):
        """
        Creates the API interface

        :param address: address of node to connect too (string) (format: ip:port)
        """

        self._connection = Connection(address)

    def api(self, api_endpoint):
        """
        Gets the API methods for the specified api_endpoint

        :param api_endpoint: valid api_endpoint (string)
        :return: (api_endpoint object)
        """

        api_endpoint = api_endpoint.lower()

        if api_endpoint not in API_ENDPOINTS:
            raise BPLAPIException({
              "message": "api endpoint not valid.",
              "api endpoint": api_endpoint,
              "api endpoints": API_ENDPOINTS
            })

        return getattr(
            import_module("bpl_api.api.{0}".format(api_endpoint.capitalize())),
            api_endpoint.capitalize()
        )(self._connection)
