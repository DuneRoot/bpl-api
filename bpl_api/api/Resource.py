class Resource:

    def __init__(self, connection):
        """
        Creates a resource object

        :param connection: (bpl_api.Connection.Connection)
        """

        self._connection = connection

    def get(self, path, params=None):
        """
        Wrapper for bpl_api.Connection.Connection.get

        :param path: api endpoint path (string)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._connection.get(path, params=params)

    def post(self, path, json=None, params=None):
        """
        Wrapper for bpl_api.Connection.Connection.post

        :param path: api endpoint path (string)
        :param json: json for request (dict)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._connection.post(path, json=json, params=params)

    def put(self, path, json=None, params=None):
        """
        Wrapper for bpl_api.Connection.Connection.put

        :param path: api endpoint path (string)
        :param json: json for request (dict)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._connection.put(path, json=json, params=params)

    def delete(self, path, params=None):
        """
        Wrapper for bpl_api.Connection.Connection.delete

        :param path: api endpoint path (string)
        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self._connection.delete(path, params=params)
