from bpl_api.api.Resource import Resource


class Transactions(Resource):

    def transaction(self, id):
        """
        Retrieve a transaction

        :param id: transactionId for the transaction (string)
        :return: (dict)
        """

        return self.get("transactions/get", {"id": id})

    def all_transactions(self, params=None):
        """
        Lists all transactions

        :param params: parameters for request (dict)
        :return: (dict)
        """

        return self.get("transactions", params)

    def unconfirmed_transaction(self, id):
        """
        Retrieve an unconfirmed transaction

        :param id: transactionId for the unconfirmed transaction (string)
        :return: (dict)
        """

        return self.get("transactions/unconfirmed/get", {
            "id": id
        })

    def all_unconfirmed_transactions(self, address=None, public_key=None):
        """
        List all unconfirmed transactions

        :param address: address by which the resources will be filtered (string)
        :param public_key: sender public key by which the resources will be filtered (string)
        :return: (dict)
        """

        return self.get("transactions/unconfirmed", {
            "senderPublicKey": public_key,
            "address": address
        })

    def send(self, recipient_id, amount, secret, second_secret=None, public_key=None):
        return self.put("transactions", json={
            "recipientId": recipient_id,
            "amount": amount,
            "secret": secret,
            "secondSecret": second_secret,
            "publicKey": public_key
        })
