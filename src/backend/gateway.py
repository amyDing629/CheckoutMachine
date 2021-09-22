import csv
from typing import List
from item import Item
class Gateway:
    def _get_item_list(self) -> List[Item]:
        item_list = []
        with open('src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item_list.append(Item(row['name'], row['price']))
        return item_list
    
    def _write_list_to_file(self, item_list: List[Item]):
        with open('src/items.csv', 'w', newline='') as csvfile:
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

    def remove_item_from_database(self, name: str) -> None:
        """
        Remove item with input name from database.
        """
        item_list = self._get_item_list()
        for item in item_list:
            if item.get_name() == name:
                item_list.remove(item)
        self._write_list_to_file(item_list)

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

