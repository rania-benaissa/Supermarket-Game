import time as t
import numpy as np
import pandas as pd
import sys

sys.path.append('D:/M1/S2/DM/project/')

from Algorithm.aPrioriAlgorithm import aPrioriAlgorithm


def constructItems(purchases):

    vals = []

    for column in purchases:

        vals += purchases[column].unique().tolist()

    vals = list(dict.fromkeys(vals))

    vals = [x for x in vals if str(x) != 'nan']

    return pd.DataFrame(vals)


# THIS IS FOR A DATASET OF 2000 TRANSACTIONS
purchases = pd.read_csv('Test/store_data.csv',
                        sep=',', dtype=str, header=None)

items = constructItems(purchases)

start = t.time()

apriori = aPrioriAlgorithm(purchases, items, 0.01, 1, 0)
apriori.run()

end = t.time()
print("--- %s secondes ---" % (end - start))

# this function is to know if there s a redundant value in each row

# for val in vals:

#     df = purchases.isin([val]).sum(1)

#     if(len([val]) in df.values):

#         for i in range(0, len(df)):

#             row = df[i]

#             if(row > 1):

#                 print(str(i) + ","+str(row))
