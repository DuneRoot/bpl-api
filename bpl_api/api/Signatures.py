from bpl_api.api.Resource import Resource


class Signatures(Resource):

    def fee(self):
        """
        Retrieve the signature registration fee

        :return: (dict)
        """

        return self.get("signatures/fee")

    def add_signature(self, secret, second_secret=None):
        """
        #TODO

        :param secret: secret passphrase for the account (string)
        :param second_secret: second secret passphrase for the account (string)
        :return: (dict)
        """

        self.put("signatures", json={
            "secret": secret,
            "secondSecret": second_secret
        })
