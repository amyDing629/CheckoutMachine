class Item:
    """
    Checkout Items.
    Parameters:
        name(str): item name
        price(float): item's original price
        discount(float): the discount that is applied to the item
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.discount = 0
    
    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> str:
        return self.price

    def change_name(self, update_name: str) -> None:
        self.name = update_name

    def change_price(self, update_price: float) -> None:
        self.price = update_price

    def add_discount(self, discount: float) -> None:
        self.discount = discount
