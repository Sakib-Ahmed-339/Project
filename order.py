class Order:
    
    def __init__(self, quantity, customer_name, product):
        self.quantity = quantity
        self.customer_name = customer_name
        self.product = product

    def show_quantity(self):
        return f"Quantity: {self.quantity}"

    def show_customer_name(self):
        return f"Customer name: {self.customer_name}"

    def show_product_price(self):
        tax = self.product.get_price() * 0.2
        price = self.product.get_price()
        final_price = price + tax
        return f"Price per unit including tax: ${final_price:.2f}"

    def calculate_total(self):
        price_with_tax = self.product.get_price() * 1.2
        total_price = self.quantity * price_with_tax
        return f"Total order price (including tax): ${total_price:.2f}"