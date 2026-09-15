## Task 1
# Ask for name (string)
name = input("Enter your name: ")

# Ask for age (string by default); convert to int
age = int(input("Enter your age: "))

# Ask for your height in metres (string by default); convert to float
height = float(input("Enter your height in metres (e.g. 1.75): "))

# TODO: Print a greeting that includes name, age, and height,
# clearly formatted. Example: "Hello, Sam! You are 20 years old and 1.75 m tall."

print(f"Hello, {name}! You are {age} years old and {height} m tall.")


## Task 2
# Ask for your city (string)
city = input("Which city do you live in? ")

# Ask for travel time in minutes (convert to int)
travel_minutes = int(input("How many minutes does it take to travel to your university? "))

# Ask for your favourite decimal number (convert to float)
fav_decimal = float(input("Enter your favourite decimal number: "))

# TODO: Display a message combining these values.
# Example: "You live in Oxford, travel takes 15 minutes, and your favourite number is 3.14"

print(f"You live in {city}, travel takes {travel_minutes}, and your favourite number is {fav_decimal}")


## Task 3
# Input two numbers (convert to float)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask for operation
operation = input("Choose operation (+, -, *, /): ")

# TODO: Use if/elif to perform the correct operation:
# - + : add
# - - : subtract
# - * : multiply
# - / : divide (check for division by zero using boolean expression)
#
# Example structure:
# if operation == "+":
#     result = num1 + num2
# elif operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero"
# ...
# TODO: Print the result or error message accordingly

valid = True

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
        valid = False
else:
    result = "Invalid operation"
    valid = False

if valid:
    print(f"{num1} {operation} {num2} = {result}")
else:
    print(result)

## Task 5

def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")
    
    valid = True
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
            valid = False
    else:
        result = "Invalid operation"
        valid = False
    
    if valid:
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print(result)

loop = True

while loop:
    calculate()
    
    repeat = str(input("Would you like to calculate again? (yes/no): ")).strip().lower()
    
    while repeat not in {"yes", "no"}:
        repeat = str(input("Please enter 'yes' or 'no': ")).strip().lower()
        
    if repeat == "no":
        loop = False


## Task 6

# i have read everything, and this does not require code, ill put a link to the git repo.
# https://github.com/ikyynites/ucen-intro-code