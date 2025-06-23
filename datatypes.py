# 1. Prompt for age and calculate next birthday age
age = int(input("How old are you? "))
next_age = age + 5
print(f"On your next birthday, you will be {next_age} years old.")

# 2. Prompt for number of egg cartons and calculate total eggs
cartons = int(input("How many egg cartons do you have? "))
total_eggs = cartons * 12
print(f"You have a total of {total_eggs} eggs.")

# 3. Prompt for number of cookies and people, calculate cookies per person
cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))

# Check to avoid division by zero
if people == 0:
    print("You cannot divide cookies among zero people.")
else:
    cookies_per_person = cookies / people
    print(f"Each person gets {cookies_per_person:.2f} cookies.")
