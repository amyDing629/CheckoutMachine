from typing import List, Tuple
from backend.item import Item
from backend.gateway import Gateway
class CheckOut:
    """
    Use case for checking out items.
    Parameters:
        item_list (List[Tuple[Item, int]]): a list of items that is included in the check out
        tax: float
    
    """
    def __init__(self):
        self.item_list: List[Tuple[Item, int]] = []
        self.tax = 0.13
    
    def change_tax(self, tax: float) -> None:
        self.tax = tax

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
            price = gateway.get_price_by_name(item_name)
            self.item_list.append((Item(item_name, price), quantity))
            return True
        return False
        
    def remove_item_from_list(self, item_name: str, quantity: int) -> None:
        """
        Remove item from item list.
        If quantity smaller than previous item quantity, exist quantity = previous quantity - removed quantity.
        If quantity equals or larger, remove item
        """
        item_info = self.get_item_by_name(item_name)
        if quantity < item_info[1]:
            item_info[1] -= quantity
        else:
            self.item_list.remove(item_info)

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
            total_sum += item_info[0].get_price()*item_info[1]*(1+self.tax)*(1-item_info[0].get_discount())
        return total_sum
