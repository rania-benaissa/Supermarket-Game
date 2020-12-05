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

To start the game, run the *Application.py* file in **GUI folder** :

![start](/Readme_images/start.png)

## Exemple

* Once the game has started, the player takes on the role of cashier and sees various customers enter his supermarket.

![selection](/Readme_images/selection.jpg)

* The list in the upper right corner represents the purchased items and the items to guess.

* To help the player make the right choices, he can consult each client's transactions list (list and comboBox located on the lower right corner).

* The list on the lower left corner is a list of items among which figure the items to guess.

* The player must choose as many items as it is missing and must submit his choices by clicking on 'Submit selection'.

![response](/Readme_images/response.jpg)

* When the player has submitted his choices, the purchases list will be updated.

* The correct purchases list will appear in the upper left corner and its items will be compared to the items suggested by the player.

* If the player makes at least one correct guess, the corresponding item will have a green background and the player will receive 200 success points for each correct prediction.

* While if any chosen item is not among the correct purchases, it will have a red background.

* If none of the chosen items is a correct guess, the customer will be disappointed.

* Thus the player can move on to the next customer by clicking on the green arrow and the game will be restarted.