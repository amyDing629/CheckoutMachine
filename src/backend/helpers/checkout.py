from item import Item
class CheckOut:
    """
    Use case for checking out items.
    Parameters:
        item_list (List[Tuple[Item, int]]): a list of items that is included in the check out
        tax: float
    
    """
    def __init__(self):
        self.item_list = []
        self.tax = 0.13
    
    def change_tax(self, tax: float) -> None:
        self.tax = tax

    def add_item_to_list(self, item_name: str, quantity: int) -> None:
        """
        Precondition: item_name exists in database.
        Get item price from the .csv file. 
        Create new item object and add to item list.
        """
        pass

    def remove_item_from_list(self, item_name: str, quantity: int) -> None:
        """
        Remove item from item list.
        If quantity smaller than previous item quantity, exist quantity = previous quantity - removed quantity.
        If quantity equals or larger, remove item
        """
        pass

    def add_discount(self, item_name, discount: float) -> None:
        """
        Change item's discount value
        """
        pass

    def count_sum(self) -> float:
        """
        Count final check out value
        """
        pass

