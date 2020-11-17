class ItemSet():

    def __init__(self):

        self.items = []

        self.support = 0

    def __repr__(self):

        return "Itemset : " + str(self.items) + " \n\tSupport : " + str(self.support) + "\n"
