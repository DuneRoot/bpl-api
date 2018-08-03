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
