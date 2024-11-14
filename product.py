class Product:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show_title(self):
        return f"Product: {self.title}"

    def show_price(self):
        return f"Price: ${self.price:.2f}"

    def get_price(self):
        return self.price
    

    
