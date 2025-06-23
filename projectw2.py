# Meal Price Calculator
# Extra Feature: Added option for drinks per person and calculates the total accordingly.

# Ask for meal prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask for number of people
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Extra Feature: Ask for drink price and assume one drink per person
drink_price = float(input("What is the price of a drink? "))
total_people = num_children + num_adults
total_drinks_cost = drink_price * total_people

# Calculate subtotal
child_total = child_meal_price * num_children
adult_total = adult_meal_price * num_adults
subtotal = child_total + adult_total + total_drinks_cost

# Display subtotal
print(f"\nSubtotal: ${subtotal:.2f}")

# Ask for sales tax
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Compute sales tax and total
sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax

# Display tax and total
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

# Ask for payment and compute change
payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total

# Display change
print(f"Change: ${change:.2f}")
