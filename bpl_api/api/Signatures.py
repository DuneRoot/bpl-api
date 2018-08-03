from bpl_api.api.Resource import Resource


class Signatures(Resource):

    def fee(self):
        """
        Retrieve the signature registration fee

        :return: (dict)
        """

        return self.get("signatures/fee")
