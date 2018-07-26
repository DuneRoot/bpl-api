from bpl_api.api.Resource import Resource


class Peers(Resource):

    def peer(self, ip, port):
        """
        Retrieve a peer

        :param ip: IP address for the peer (string)
        :param port: port for the peer (integer)
        :return: (dict)
        """

        return self.get("peers/get", {
            "ip": ip,
            "port": port
        })

    def all_peers(self, limit=25):
        """
        List all peers

        :param limit: maximum number of peers in response (integer)
        :return: (dict)
        """

        return self.get("peers", {
            "limit": limit
        })

    def version(self):
        """
        Retrieve the core version

        :return: (dict)
        """

        return self.get("peers/version")
