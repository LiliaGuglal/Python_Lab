class OrderManager:
    def __init__(self, items):
        self.items = [item.copy() for item in items]

    def total(self):
        if not self.items:
            return 0
        return sum(item['price'] for item in self.items)

    def most_expensive(self):
        if not self.items:
            return None 
        
        return max(self.items, key=lambda item: item['price'])

    def apply_discount(self, percent):
        if not (0 < percent <= 100):
            raise ValueError("Discount must be between 0 and 100")
        
        discount_multiplier = 1 - (percent / 100)
        
        for item in self.items:
            item['price'] *= discount_multiplier

    def __repr__(self):
        item_names = ', '.join([item['name'] for item in self.items])
        return f"OrderManager(items=[{item_names}])"