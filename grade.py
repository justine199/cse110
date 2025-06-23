#ask the user for the grade
grade = float(input("what is the grade percent? "))

letter = ""
#figure out the latter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif  grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

#get the last digit
last_digit = grade % 10
print(last_digit)







#determine the sign
if last_digit >= 7:
    sign = "+"
elif last_digit <= 3: 
    sign = "-"
else:
    sign = ""       

#Handle the exception (A+, F+, F-)
if letter == "A" and sign == "+":
    sign = ""

if letter == "F":
     sign = ""    
    


#display the letter grade
print(f"You have earned the grade{letter}{sign}")    

if grade >= 70:
    print("congratulstions! you passed the course")    
else:
    print("sorry, please try the course again")    
#display the latter grade
print(f"your earned grade is {letter}")