from product import Product
from order import Order

def display_menu(products):
    print("--- Welcome to the Store ---")
    print("Please select a product:")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product.show_title()} - {product.show_price()}")


def take_order(products):
    try:
        choice = int(input("Enter the number of the product you want to order: "))
        if choice < 1 or choice > len(products):
            print("Invalid choice, please try again.")
            return take_order(products)
        
        selected_product = products[choice - 1]
        customer_name = input("Enter your name: ")
        quantity = int(input(f"How many {selected_product.title}s would you like to order? "))

        order = Order(quantity, customer_name, selected_product)
        print("Order Summary:")
        print(order.show_customer_name())
        print(order.show_quantity())
        print(order.show_product_price())
        print(order.calculate_total())

    except ValueError:
        print("Invalid input! Please enter a number.")
        take_order(products)


def main():

    product_1 = Product("Pen", 10)
    product_2 = Product("Paper", 50)
    product_3 = Product("Notebook", 100)
    product_4 = Product("Eraser", 5)

    products = [product_1, product_2, product_3, product_4]

    while True:
        display_menu(products)
        take_order(products)

        cont = input("Do you want to place another order? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for shopping with us!")
            break


if __name__ == "__main__":
    main()
