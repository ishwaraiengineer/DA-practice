"""
02_conditionals.py
------------------
Topic: Python basics - making decisions with conditions

Builds on 01_variables_and_types.py (variables, input(), int(), print()).

What this program demonstrates:
    - Comparison operators: ==, !=, <, >, <=, >=
    - if / elif / else to choose between different paths
    - Logical operators: and, or, not
    - Indentation (the spaces that show which lines belong to an if)
    - A simple grade checker
    - A simple voting-age checker

How to run:
    python 02_conditionals.py
"""

# ---------------------------------------------------------------
# PART 1: Comparison operators
# A comparison gives back a bool (True or False), the type you
# met in file 01.
# ---------------------------------------------------------------
x = 10
y = 7

print("=== Part 1: Comparison operators ===")
print("x == y :", x == y)   # equal to
print("x != y :", x != y)   # not equal to
print("x > y  :", x > y)    # greater than
print("x < y  :", x < y)    # less than
print("x >= 10:", x >= 10)  # greater than or equal to
print("y <= 5 :", y <= 5)   # less than or equal to
# Careful: a single = ASSIGNS a value, a double == COMPARES values.

# ---------------------------------------------------------------
# PART 2: if / elif / else
# Python checks the conditions from top to bottom and runs ONLY
# the first block whose condition is True.
# The indented lines (4 spaces) belong to the line above them.
# ---------------------------------------------------------------
temperature = 32

print("\n=== Part 2: if / elif / else ===")
if temperature > 35:
    print("It is very hot today.")
elif temperature > 25:
    print("It is warm today.")
elif temperature > 15:
    print("It is mild today.")
else:
    print("It is cold today.")

# ---------------------------------------------------------------
# PART 3: Logical operators: and, or, not
#   and -> True only if BOTH conditions are True
#   or  -> True if AT LEAST ONE condition is True
#   not -> flips True to False and False to True
# ---------------------------------------------------------------
age = 20
has_ticket = True

print("\n=== Part 3: and, or, not ===")
print("Adult AND has ticket:", age >= 18 and has_ticket)
print("Under 12 OR has ticket:", age < 12 or has_ticket)
print("NOT has ticket:", not has_ticket)

if age >= 18 and has_ticket:
    print("You may enter the cinema.")

# ---------------------------------------------------------------
# PART 4: Simple grade checker
# input() gives text, so we convert it to a number with int()
# (same idea as in file 01).
# ---------------------------------------------------------------
print("\n=== Part 4: Grade checker ===")
score = int(input("Enter your exam score (0-100): "))

if score < 0 or score > 100:
    # 'or' catches any score outside the valid range
    print("Invalid score. Please enter a number between 0 and 100.")
elif score >= 90:
    print("Grade: A (Excellent)")
elif score >= 75:
    print("Grade: B (Good)")
elif score >= 60:
    print("Grade: C (Satisfactory)")
elif score >= 40:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")
# The order matters: we check the highest score first. If we
# checked score >= 40 first, every passing score would get a D.

# ---------------------------------------------------------------
# PART 5: Simple voting-age checker
# ---------------------------------------------------------------
print("\n=== Part 5: Voting-age checker ===")
voter_age = int(input("Enter your age: "))
VOTING_AGE = 18   # capital letters = a value we do not plan to change

if voter_age < 0:
    print("Age cannot be negative.")
elif voter_age >= VOTING_AGE:
    print("You are eligible to vote.")
else:
    years_left = VOTING_AGE - voter_age
    print(f"You are not old enough to vote yet. Wait {years_left} more year(s).")

# ---------------------------------------------------------------
# WHAT I LEARNED
# ---------------------------------------------------------------
# 1. Comparison operators (==, !=, <, >, <=, >=) produce True or False.
# 2. = assigns a value; == compares two values.
# 3. if / elif / else lets the program choose one path; Python runs
#    only the first block whose condition is True.
# 4. Indentation shows which lines belong inside an if block.
# 5. and needs both conditions True, or needs at least one, and not
#    reverses a result.
# 6. The order of elif checks matters: check the strictest first.
# 7. int(input(...)) turns typed text into a number so I can compare it.
