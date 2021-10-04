from django.db import models
import csv
from typing import List, Tuple, Optional
DATA_FILE_PATH = 'items.csv'
class Item(models.Model):
    """
    Checkout Items.
    Parameters:
        name(str): item name
        price(float): item's original price
        discount(float): the discount that is applied to the item
    """
    def __init__(self, name: str, price: float):
        super().__init__()
        self.name = name
        self.price = price
        self.discount = 0
    
    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price
    
    def get_discount(self) -> float:
        return self.discount

    def change_name(self, update_name: str) -> None:
        self.name = update_name

    def change_price(self, update_price: float) -> None:
        self.price = update_price

    def change_discount(self, discount: float) -> None:
        self.discount = discount

class CheckOut(models.Model):
    """
    Use case for checking out items.
    Parameters:
        item_list (List[Tuple[Item, int]]): a list of items that is included in the check out
        tax: float
    
    """
    def __init__(self):
        super().__init__()
        self.item_list: List[Tuple[Item, int]] = []
        self.tax = 0.13
    
    def change_tax(self, tax: float) -> None:
        self.tax = tax

    def get_tax(self) -> float:
        return self.tax

    def get_item_by_name(self, item_name: str) -> Tuple[Item, int]:
        for item_info in self.item_list:
            if item_info[0].get_name() == item_name:
                return item_info
    
    def get_item_list(self) -> List[Tuple[Item, int]]:
        return self.item_list

    def add_item_to_list(self, item_name: str, quantity: int) -> bool:
        """
        Precondition: item_name exists in database.
        Get item price from the .csv file. 
        Create new item object and add to item list.
        Return False when the item is not in the database, thus cannot be added.
        """
        gateway = Gateway()
        if gateway.check_item_in_database(item_name):
            item_list = self.get_item_list()
            for i in range(len(item_list)):
                if item_list[i][0].get_name() == item_name:
                    item_list[i] = (item_list[i][0], item_list[i][1] + quantity)
                    return True
            price = gateway.get_price_by_name(item_name)
            self.item_list.append((Item(item_name, price), quantity))
            return True
        return False
    
    def edit_price(self, item_name: str, price: float) -> None:
        Gateway().edit_item_price(item_name, price)
        for item_info in self.get_item_list():
            if item_info[0].get_name() == item_name:
                self.remove_item_from_list(item_name, None)
                self.add_item_to_list(item_name, item_info[1])
        
    def remove_item_from_list(self, item_name: str, quantity: Optional[int]) -> None:
        """
        Remove item from item list.
        If quantity smaller than previous item quantity, exist quantity = previous quantity - removed quantity.
        If quantity equals or larger, remove item
        """
        item_info = self.get_item_by_name(item_name)
        self.item_list.remove(item_info)
        if quantity is not None:
            if quantity < item_info[1]:
                self.item_list.append((item_info[0], item_info[1] - quantity))
    
    def add_discount(self, item_name, discount: float) -> None:
        """
        Change item's discount value
        """
        item_info = self.get_item_by_name(item_name)
        item_info[0].change_discount(discount)
        
    def count_sum(self) -> float:
        """
        Count final check out value
        """
        total_sum = 0
        for item_info in self.item_list:
            total_sum += float(item_info[0].get_price())*int(item_info[1])*(1+self.tax)*(1-item_info[0].get_discount())
        total_sum = float(format(total_sum, '.2f'))
        return total_sum

class Gateway(models.Model):
    def _get_item_list(self) -> List[Item]:
        item_list = []
        with open(DATA_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_list.append(Item(row['name'], float(row['price'])))
        return item_list
    
    def _write_list_to_file(self, item_list: List[Item]):
        with open(DATA_FILE_PATH, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'price'])
            writer.writerow({'name': 'name', 'price': 'price'})
            for item in item_list:
                writer.writerow({'name': item.get_name(), 'price': item.get_price()})
        return item_list
 
    def add_item_to_database(self, name: str, price: float) -> None:
        """
        Return False when the item name has already existed in the database, 
        thus cannot be added.
        """
        if not self.check_item_in_database(name):
            item_list = self._get_item_list()
            item_list.append(Item(name, price))
            self._write_list_to_file(item_list)
            return True
        return False

    def remove_item_from_database(self, name: str) -> bool:
        """
        Remove item with input name from database.
        If item not in database, remove nothing.
        Return true if item is in database and is removed.
        Return False if item is not in database.
        """
        if not self.check_item_in_database(name):
            return False
        item_list = self._get_item_list()
        for item in item_list:
            if item.get_name() == name:
                item_list.remove(item)
        self._write_list_to_file(item_list)
        return True

    def check_item_in_database(self, name: str) -> bool:
        """
        Check if the item with input name exists in the database.
        """
        item_list = self._get_item_list()
        for item in item_list:
            if name == item.get_name():
                return True
        return False

    def get_price_by_name(self, name: str) -> float:
        """
        Get item's price by name.
        """
        item_list = self._get_item_list()
        for item in item_list:
            if item.get_name() == name:
                return item.get_price()

    def edit_item_price(self, name: str, price: float) -> bool:
        """
        Edit item's price. 
        Return true is item in database.
        Return false if item is not in database.
        """
        if not self.check_item_in_database(name):
            return False
        item_list = self._get_item_list()
        if self.check_item_in_database(name):
            for item in item_list:
                if item.get_name() == name:
                    item.change_price(price)
        self._write_list_to_file(item_list)
        return True
            


