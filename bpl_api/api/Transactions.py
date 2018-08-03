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

    def _post_transaction(self, transaction):
        return self._connection.post_url(
            "http://" + self._connection.get_address() + "/peer/transactions",
            json={
                "transactions": [transaction]
            }
        )

    def send(self, transaction):
        return self._post_transaction(transaction)
