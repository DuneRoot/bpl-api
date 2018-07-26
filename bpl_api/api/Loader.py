from bpl_api.api.Resource import Resource


class Loader(Resource):

    def status(self):
        """
        Retrieves the status

        :return: (dict)
        """

        return self.get("loader/status")

    def synchronisation_status(self):
        """
        Retrieves the synchronisation status

        :return: (dict)
        """

        return self.get("loader/status/sync")

    def configuration(self):
        """
        Retrieves the configuration

        :return: (dict)
        """

        return self.get("loader/autoconfigure")
