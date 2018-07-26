from bpl_api.api.Resource import Resource


class Accounts(Resource):

    def account(self, address):
        """
        Retrieve an account

        :param address: BPL address (string)
        :return: (dict)
        """

        return self.get("accounts", {"address": address})

    def balance(self, address):
        """
        Retrieve the balance of an account

        :param address: BPL address (string)
        :return: (dict)
        """

        return self.get("accounts/getBalance", {"address": address})

    def public_key(self, address):
        """
        Retrieve the public key of an account

        :param address: BPL address (string)
        :return: (dict)
        """

        return self.get("accounts/getPublicKey", {"address": address})

    def delegate_fee(self):
        """
        Retrieve the delegate registration fee

        :return: (dict)
        """

        return self.get("accounts/delegates/fee")

    def votes(self, address):
        """
        Retrieve the voted delegate of an account

        :param address: BPL address (string)
        :return: (dict)
        """

        return self.get("accounts/delegates", {"address": address})

    def vote(self, delegates, secret, second_secret=None, public_key=None):
        """
        Vote for a delegate

        :param delegates: #TODO
        :param secret: secret passphrase (string)
        :param second_secret: second secret passphrase (string)
        :param public_key: public key (string)
        :return: (dict)
        """

        return self.put("accounts/delegates", json={
            "secret": secret,
            "delegates": delegates,
            "secondSecret": second_secret,
            "publicKey": public_key
        })
