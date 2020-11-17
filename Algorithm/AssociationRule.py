class AssociationRule():

    def __init__(self):

        self.antecedent = []

        self.consequent = [],

        self.confidence = 0

        self.lift = 0

    def __repr__(self):

        return "Rule : " + str(self.antecedent) + "  --> : " + str(self.consequent) + "\n\tConfidence : " + str(self.confidence) + "\n\tLift : " + str(self.lift)+"\n"
