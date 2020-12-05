# Supermarket Game
 Supermarket game using an optimized implementation of **Apriori algorithm** in Python

## Table of contents
* [Description](#description)
* [Technologies](#technologies)
* [DataSet](#dataset)
* [Apriori Algorithm](#apriori-algorithm)
  * [Test](#test)
  * [Exemple](#exemple)
* [Game](#game)
  * [Execution](#execution)
  * [Exemple](#exemple)

# Description

# Technologies
To run this game, install:
* Python 3.*
* PyQt5
* Pygame
* Itertools
* Pandas
* Numpy (if you would like to test the **Apriori algorithm**)


# DataSets

In _**Data** folder_ , you will find assets and datasets used in the game: 
* _**Assets** folder_: contains images, backgrounds and icons.
* _**customers.csv** file_: contains 6 characters with their corresponding image URL in _**Assets** folder_.
* _**items.csv** file_: contains 42 items that are defined by their name and corresponding image URL in _**Assets** folder_.
* _**transactions.csv** file_: contains 120 transaction.

In _**Test** folder_, you will find datasets that are used to test the **Apriori algorithm**: 

* _**store_data** file_: contains 7500 transactions on 120 items.
* _**customers.csv** file_: contains 2000 transactions on 42 items.

# Apriori Algorithm

The  **Apriori algorithm**'s implementation is located in _**Algorithm** folder_.

## Implementation

* To reduce the algorithm's complexity, we will use and manipulate DataFrames.

* The algorithm considers 3 parameters : MinSup, MinConf and MinLift.

* To reduce the association rules number:

 * We will only consider frequent ItemSets made up of three to six items (1-items and 2-items are calculated but ignored).

 * We will only consider association rules which contains at least 2 antecedents.
   For example if we take a frequent ItemSet made up of 4 items as shown in the following figure: 

   ![itemset](/Readme_images/itemset_frequent_4_items.jpg)

   Instead of generating 14 association rules, the algorithm will only generate 10 that are considered **relevant**:
   ![association_rules](/Readme_images/association_rules.jpg)

 ## Tests

 The results obtained by applying the algorithm on a dataset of 7500 transactions on 120 items are shown below:
 ![results](/Readme_images/results1.jpg)

 
 
# Game

## Execution

## Exemple
