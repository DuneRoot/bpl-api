from bpl_api.api.Resource import Resource


class Blocks(Resource):

    def block(self, id):
        """
        Retrieve a block

        :param id: block id (string)
        :return: (dict)
        """

        return self.get("blocks/get", {"id": id})

    def all_blocks(self, limit=25):
        """
        List all blocks

        :param limit: maximum number of blocks in response (integer)
        :return: (dict)
        """

        return self.get("blocks", {
            "limit": limit
        })

    def epoch(self):
        """
        Retrieve the epoch of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getEpoch")

    def height(self):
        """
        Retrieve the height of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getHeight")

    def nethash(self):
        """
        Retrieve the nethash of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getNethash")

    def fee(self):
        """
        Retrieve a fee

        :return: (dict)
        """

        return self.get("blocks/getFee")

    def fees(self):
        """
        List all fees of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getFees")

    def milestone(self):
        """
        Retrieve the milestone of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getMilestone")

    def last_reward(self):
        """
        Retrieve the reward of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getLastReward")

    def supply(self):
        """
        Retrieve the supply of the blockchain

        :return: (dict)
        """

        return self.get("blocks/getSupply")

    def status(self):
        """
        Retrieve the status of the blockchain

        :return:  (dict)
        """

        return self.get("blocks/getStatus")
