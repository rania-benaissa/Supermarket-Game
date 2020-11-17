from Algorithm.ItemSet import ItemSet
from Algorithm.AssociationRule import AssociationRule

import itertools as iter

import pandas as pd


class aPrioriAlgorithm:

    def __init__(self, data1, items, minS, minC, minL):

        # transactions
        self.dataSet = data1

        # reeucpere les items du supermarché
        self.items = self.getItems(items)

        self.frequentItems = []

        self.assocRules = []

        self.minSup = minS

        self.minConf = minC

        self.minLift = minL

        self.level = 1

        print("Transactions number = " + str(len(data1)))
        print("Items number = " + str(len(items)))
        print("MinSup = " + str(minS))
        print("MinConf = " + str(minC))
        print("MinLift = " + str(minL))

    # get items from data1 Frame

    def getItems(self, items):

        self.items = []

        for i in range(0, len(items)):

            item = ItemSet()

            row = items.iloc[i]

            item.items.append(row.iloc[0])

            self.items.append(item)

        return self.items

    def calculateSupport(self):

        frequent_lvl = []

        for i in range(0, len(self.items)):

            item = self.items[i]

            # counts for each row the number of existant items
            df = self.dataSet.isin(item.items).sum(1)

            if(len(item.items) in df.values):

                item.support = df.value_counts()[len(
                    item.items)] / len(self.dataSet)
            else:
                item.support = 0

            if(item.support >= self.minSup):

                # save frequent items
                self.frequentItems.append(item)
                frequent_lvl.append(item)

        return frequent_lvl


# build the k-itemset

    def generateK_itemset(self, frequent_lvl):

        print( str(self.level) + "-Itemset frequent items number "
              + " : " + str(len(frequent_lvl)))

        # create the next level

        # if the itemset is not empty

        if(frequent_lvl):

            self.level += 1

            self.items = []

            for i in range(0, len(frequent_lvl)):

                for j in range(i + 1, len(frequent_lvl)):

                    form = True

                    item = ItemSet()

                    for k in range(0, self.level - 2):

                        # si il y a pas suffisament d elements en commun on peut pas former

                        if(frequent_lvl[i].items[k] != frequent_lvl[j].items[k]):

                            form = False
                            break

                        else:

                            item.items.append(
                                frequent_lvl[i].items[k])

                    # SI L ON PEUT FORMER DE NOUVEAUX ITEMSETS

                    if(form):
                        item.items.append(
                            frequent_lvl[i].items[self.level - 2])
                        item.items.append(
                            frequent_lvl[j].items[self.level - 2])
                        self.items.append(item)

            # apres le for si il n'y a toujours pas d'elements dans items c est que l'on a pas pu former
            # du coup l'algo doit s'arreter
            if(self.items):
                return True
            else:
                return False

        else:
            return False

    def associationRules(self):

        for items in self.frequentItems:

            if(len(items.items) > 2):

                self.generateRules(items.items)

    # generer les regles d'un itemset frequent "items"
    def generateRules(self, items):

        j = len(items) - 1

        for i in range(1, len(items)):

            data1 = set(iter.combinations(items, i))

            data2 = set(iter.combinations(items, j))

            j -= 1

            for val1 in data1:

                for val2 in data2:

                 # elaguer les regles dont antecedent <2
                    if(len(list(val1)) >= 2):
                        # s'il n existe pas une val de val1 dans val2

                        if(not set(val1).intersection(set(val2))):

                            assoc = AssociationRule()

                            assoc.antecedent = list(val1)

                            assoc.consequent = list(val2)

                            self.assocRules.append(assoc)

    def calculateConfLift(self):

        remainingRules = []

        for rule in self.assocRules:

            AuB = rule.antecedent + rule.consequent

            for items in self.frequentItems:

                # si l antecedent contient un itemset des itemsets frequents

                if(len(items.items) == len(rule.antecedent) and set(items.items).issubset(rule.antecedent)):

                    supA = items.support

                if(len(items.items) == len(rule.consequent) and set(items.items).issubset(rule.consequent)):

                    supB = items.support

                if(len(items.items) == len(AuB) and set(items.items).issubset(AuB)):

                    supAB = items.support

            rule.confidence = supAB / supA

            rule.lift = supAB / (supA * supB)

            if(rule.confidence >= self.minConf and rule.lift >= self.minLift):

                remainingRules.append(rule)

        self.assocRules = remainingRules

    def run(self):

        loop = True

        # ici j arrete l'algo au lvl 6 (6 items dans un itemset frequent ) + verification minSup
        while(loop and self.level <= 6):

            # calculate frequent items + compare its support
            frequent_lvl = self.calculateSupport()

            loop = self.generateK_itemset(frequent_lvl)

        print("Total frequent items  = " + str(len(self.frequentItems)))

        # generation des regles d'association en ne prenant que des itemset de taille >2 + dont  l antecedant >1
        self.associationRules()

        print("Rules number : " + str(len(self.assocRules)))

        # calcul de la confiance et du lift + suppression des regles d'association selon minConf et minLift
        self.calculateConfLift()

        print("Valid rules number : " + str(len(self.assocRules)))
