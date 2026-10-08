"""
01_variables_and_types.py
-------------------------
Topic: Python basics - variables, strings, numbers, input() and print()

What this program demonstrates:
    - Storing values in variables
    - The main basic data types: str, int, float, bool
    - Checking a value's type with type()
    - Basic string operations (joining, upper/lower, length, f-strings)
    - Basic number operations (+, -, *, /, //, %, **)
    - Reading user input with input() and converting it with int()/float()
    - Showing results with print()

How to run:
    python 01_variables_and_types.py
"""

# ---------------------------------------------------------------
# PART 1: Variables and data types
# A variable is a name that points to a value.
# Python figures out the type automatically from the value.
# ---------------------------------------------------------------
name = "Asha"          # str   (text, written inside quotes)
age = 25               # int   (whole number)
height_m = 1.62        # float (number with a decimal point)
is_learning = True     # bool  (True or False)

print("=== Part 1: Variables and types ===")
print("name:", name, "->", type(name))
print("age:", age, "->", type(age))
print("height_m:", height_m, "->", type(height_m))
print("is_learning:", is_learning, "->", type(is_learning))

# ---------------------------------------------------------------
# PART 2: Working with strings
# ---------------------------------------------------------------
first_name = "Ada"
last_name = "Lovelace"

full_name = first_name + " " + last_name   # + joins strings together

print("\n=== Part 2: Strings ===")
print("Full name:", full_name)
print("Uppercase:", full_name.upper())     # all capital letters
print("Lowercase:", full_name.lower())     # all small letters
print("Length:", len(full_name), "characters")  # len() counts characters

# An f-string lets you put variables directly inside text.
print(f"Hello, {full_name}! Nice to meet you.")

# ---------------------------------------------------------------
# PART 3: Working with numbers
# ---------------------------------------------------------------
a = 17
b = 5

print("\n=== Part 3: Numbers ===")
print("a + b  =", a + b)    # addition
print("a - b  =", a - b)    # subtraction
print("a * b  =", a * b)    # multiplication
print("a / b  =", a / b)    # division (always gives a float)
print("a // b =", a // b)   # floor division (drops the decimal part)
print("a % b  =", a % b)    # remainder after division
print("a ** b =", a ** b)   # power (17 to the power of 5)

# ---------------------------------------------------------------
# PART 4: Getting input from the user
# input() always returns TEXT (a str), even if the user types digits.
# To do maths, convert it with int() or float().
# ---------------------------------------------------------------
print("\n=== Part 4: Your turn! ===")
user_name = input("What is your name? ")
birth_year_text = input("What year were you born? ")   # this is a str
price_text = input("Enter the price of an item (e.g. 49.99): ")

birth_year = int(birth_year_text)   # convert text -> whole number
price = float(price_text)           # convert text -> decimal number

# Simple calculations using the user's values
current_year = 2026
approx_age = current_year - birth_year
total_for_three = price * 3

print(f"\nHi {user_name}!")
print(f"You will be about {approx_age} years old in {current_year}.")
print(f"Three items at {price} each cost {total_for_three:.2f} in total.")
# ':.2f' means "show 2 digits after the decimal point"

# ---------------------------------------------------------------
# WHAT I LEARNED
# ---------------------------------------------------------------
# 1. A variable stores a value, and = assigns it (name = "Asha").
# 2. The basic types are str, int, float and bool; type() shows which.
# 3. Strings can be joined with +, changed with .upper()/.lower(),
#    measured with len(), and mixed with variables using f-strings.
# 4. Numbers support + - * / // % ** (note: / always gives a float).
# 5. input() always returns text, so I must convert it with int()
#    or float() before doing maths.
# 6. print() shows results; f-strings make the output easy to read.
