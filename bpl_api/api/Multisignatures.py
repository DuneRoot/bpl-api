from bpl_api.api.Resource import Resource


class Multisignatures(Resource):

    def pending_multisignature_transactions(self, public_key):
        """
        Retrieves the pending multisignature transactions for an account

        :param public_key: public key for the account (string)
        :return: (string)
        """

        return self.get("multisignatures/pending", {
            "publicKey": public_key
        })

    def accounts(self, public_key):
        """
        #TODO

        :param public_key: #TODO
        :return: (dict)
        """

        return self.get("multisignatures/accounts", {
            "publicKey": public_key
        })

    def sign(self, id, secret, public_key=None):
        """
        Sign a transaction with a secret passphrase

        :param id: transactionId of the transaction (string)
        :param secret: secret passphrase for the next signature (string)
        :param public_key: public key for the sender (string)
        :return: (dict)
        """

        return self.post("multisignatures/sign", json={
            "transactionId": id,
            "secret": secret,
            "publicKey": public_key
        })

    def add_multisignature(self, secret, lifetime, min, keysgroup):
        """
        Adds a multisignature to a transaction

        :param secret: secret passphrase for the account (string)
        :param lifetime: #TODO
        :param min: #TODO
        :param keysgroup: #TODO
        :return: (dict)
        """

        return self.put("multisignatures", json={
            "secret": secret,
            "lifetime": lifetime,
            "min": min,
            "keysgroup": keysgroup
        })
