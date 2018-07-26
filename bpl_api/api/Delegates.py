from bpl_api.api.Resource import Resource


class Delegates(Resource):

    def delegate(self, username=None, public_key=None):
        """
        Retrieve a delegate

        :param username: username for the delegate (string)
        :param public_key: public key for the delegate (string)
        :return: (dict)
        """

        return self.get("delegates/get", {
            "username": username,
            "publicKey": public_key
        })

    def count(self):
        """
        Retrieve the total count of delegates

        :return: (dict)
        """

        return self.get("delegates/count")

    def fee(self):
        """
        Retrieve the delegate registration fee

        :return: (dict)
        """

        return self.get("delegates/fee")

    def total_forged(self, generator_public_key):
        """
        Retrieve the total forged of a delegate

        :param generator_public_key: public key for the delegate (string)
        :return: (dict)
        """

        return self.get("delegates/forging/getForgedByAccount", {
            "generatorPublicKey": generator_public_key
        })

    def voters(self, public_key):
        """
        List all voters of a delegate

        :param public_key: public key for the delegate
        :return: (dict)
        """

        return self.get("delegates/voters", {
            "publicKey": public_key
        })

    def all_delegates(self, limit=25):
        """
        List all delegates

        :param limit: maximum number of delegates in response (integer)
        :return: (dict)
        """

        return self.get("delegates", {
            "limit": limit
        })

    def search(self, q, limit=25):
        """
        Search all delegates

        :param q: search query by which the resources will be filtered
        :param limit: maximum number of blocks in response (integer)
        :return: (dict)
        """

        return self.get("delegates/search", {
            "q": q,
            "limit": limit
        })

    def enable_delegate(self, username, secret, second_secret=None):
        """
        Change status from account to delegate

        :param username: username for the account (string)
        :param secret: secret passphrase of the account (string)
        :param second_secret: second secret passphrase of the account (string)
        :return: (dict)
        """

        return self.put("delegates", json={
            "username": username,
            "secret": secret,
            "secondSecret": second_secret
        })

    def enable_forging(self, secret):
        """
        Enable forging for the delegate

        :param secret: secret passphrase for the delegate (string)
        :return: (dict)
        """

        self.post("delegates/forging/enable", json={
            "secret": secret
        })

    def disable_forging(self, secret):
        """
        Disable forging for the delegate

        :param secret: secret passphrase for the delegate (string)
        :return: (dict)
        """

        self.post("delegates/forging/disable", json={
            "secret": secret
        })

    def next_forgers(self, limit=25):
        """
        Lists the next forgers

        :param limit: maximum number of forgers in response (integer)
        :return: (dict)
        """

        return self.get("delegates/getNextForgers", {
            "limit": limit
        })

    def forging_status(self, public_key):
        """
        Retrieves forging status of a delegate

        :param public_key: public key for the delegate (string)
        :return: (dict)
        """

        return self.get("delegates/forging/status", {
            "publicKey": public_key
        })
