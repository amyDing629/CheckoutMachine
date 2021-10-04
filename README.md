CSC301H Assignment 1
# A1 deployment video link(ggogle drive share link)
https://drive.google.com/file/d/1H66g_olIGCNCH_6VeHuG64eQCUvP-_1S/view?usp=sharing
gi
# Running process
## step 1
Git clone the repository, open in local
## step 2
* if you do not have python in your local, install python of version 3
* if you have python3 installed in your local, the create the virtual environment for the folder, Then activate the virtual environment

Run the command
```
$ python3 -m venv <name_of_virtualenv>
```
Activate Command
Mac OS / Linux
```
$ source <name_of_virtualenv>/bin/activate
```
Windows
```
$ <name_of_virtualenv>/bin/activate
```
## step 3
install Django
```
$ python -m pip install Django
```
## step 4
Open the terminal, make the root until directory mysite
```
C:\Users\siwei\OneDrive\Desktop\assignment-1-6-tangsiwei0831-dingyiy1\mysite> 
```
Then run the command line
```
$ python manage.py runserver
```

## step 5 Test the project
```
$ python manage.py test
```

# Conditions
## add item into check out list
* If item is already added into the checkout list, then add the new quantity to the checkout quantity. If item has not been added into the checkout list, then add the item and the quantity to the checkout list.
## remove item from checkout list
* If the remove quantity is larger than or equal to the quantity in the checkout list, then we remove the item from the checkout list. If the remove quantity is smaller than the quantity in the checkout list, then minus the remove quantity from the checkout quantity

## database
* Database only restore the item name and price
* If item is already added in the database, the we do not add the item. If the item is not in the database, then add it into the database.
* If we want to remove the item from databse, if item exists in databse, then we can remove. If it does not exist, then we do nothing.
* The draft data in database than can be used for add and remove
```
name,price
apple,2.0
pear,2
banana,1.0
hat,10.0
orange,3.0
toy,10.0
```


