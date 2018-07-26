import requests

from bpl_api.Exceptions import BPLRequestException


class Connection:

    def __init__(self, address):
        """
        Connection interface to node.
        Automatically retrieves nethash and places it in the headers.

        :param address: address of node to connect too (string) (format: ip:port)
        """

        self._address = address
        self._session = requests.session()

        self._session.headers.update({
            "port": "1",
            "Content-Type": "application/json",
            "os": "linux3.2.0-4-amd64",
            "version": "0.3.0",
            "nethash": self._get_nethash()
        })

    def _get_nethash(self):
        """
        Retrieve the nethash of the blockchain

        :return: nethash (string)
        """

        return self.get("blocks/getNethash")["nethash"]

    def _handle_response(self, response):
        """
        Handles responses. If invalid raises a BPLRequestException.

        :param response: response from API (response object)
        :return: (dict)
        """

        if not response.content:
            raise BPLRequestException({
                "message": "no content in response",
                "response": response.json()
            })

        if not response.ok:
            raise BPLRequestException({
                "message": "Method: {0}, URL: {1}, Status Code: {2}".format(
                    response.request.method,
                    response.request.url,
                    response.status_code
                ),
                "response": response.json()
            })

        return response.json()

    def _get_url(self, path):
        """
        Gets the full URL for the api endpoint

        :param path: api endpoint path (string)
        :return: URL (string)
        """

        return "http://" + self._address + "/" + "api" + "/" + path

    def get(self, path, params=None):
        """
        Performs a GET request

        :param path: api endpoint path (string)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._handle_response(self._session.get(
            self._get_url(path),
            params=params
        ))

    def post(self, path, json=None, params=None):
        """
        Performs a POST request

        :param path: api endpoint path (string)
        :param json: json for request (dict)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._handle_response(self._session.post(
            self._get_url(path),
            json=json,
            params=params
        ))

    def put(self, path, json=None, params=None):
        """
        Performs a PUT request

        :param path: api endpoint path (string)
        :param json: json for request (dict)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._handle_response(self._session.put(
            self._get_url(path),
            json=json,
            params=params
        ))

    def delete(self, path, params=None):
        """
        Performs a DELETE request

        :param path: api endpoint path (string)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._handle_response(self._session.delete(
            self._get_url(path),
            params=params
        ))
