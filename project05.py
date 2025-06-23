# Creative Addition:
# I added support for item quantities. The user can specify how many of each item they are adding.
# The program calculates the total price based on the item price multiplied by quantity.

def display_menu():
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item(names, prices, quantities):
    name = input("What item would you like to add? ")
    try:
        price = float(input(f"What is the price of '{name}'? "))
        quantity = int(input(f"How many '{name}' would you like to add? "))
    except ValueError:
        print("Invalid input. Please enter numbers for price and quantity.")
        return
    names.append(name)
    prices.append(price)
    quantities.append(quantity)
    print(f"'{name}' has been added to the cart.")

def view_cart(names, prices, quantities):
    if len(names) == 0:
        print("Your shopping cart is empty.")
        return
    print("The contents of the shopping cart are:")
    for i in range(len(names)):
        total_price = prices[i] * quantities[i]
        print(f"{i + 1}. {names[i]} - ${prices[i]:.2f} x {quantities[i]} = ${total_price:.2f}")

def remove_item(names, prices, quantities):
    if len(names) == 0:
        print("Your shopping cart is empty.")
        return
    view_cart(names, prices, quantities)
    try:
        index = int(input("Which item would you like to remove? ")) - 1
        if 0 <= index < len(names):
            removed_item = names.pop(index)
            prices.pop(index)
            quantities.pop(index)
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("Sorry, that is not a valid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def compute_total(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

# Main program
print("Welcome to the Shopping Cart Program!")

item_names = []
item_prices = []
item_quantities = []

while True:
    display_menu()
    choice = input("Please enter an action: ")

    if choice == "1":
        add_item(item_names, item_prices, item_quantities)
    elif choice == "2":
        view_cart(item_names, item_prices, item_quantities)
    elif choice == "3":
        remove_item(item_names, item_prices, item_quantities)
    elif choice == "4":
        compute_total(item_prices, item_quantities)
    elif choice == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
