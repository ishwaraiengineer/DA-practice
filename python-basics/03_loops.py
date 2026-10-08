# 03_loops.py
# Topic: loops (for, while, break, continue)
# Uses stuff from 01 (variables, input, int) and 02 (if, comparisons)

# ---- part 1: for loop with range() ----
# range(5) gives 0,1,2,3,4 (starts at 0 and stops BEFORE 5)
print("Part 1: for loop")
for i in range(5):
    print("i is", i)

# range(start, stop) -> starts at 1, stops before 6
for n in range(1, 6):
    print("n is", n)

# range(start, stop, step) -> jumps by 2 each time
for n in range(2, 11, 2):
    print("even number:", n)

# ---- part 2: multiplication table ----
print("\nPart 2: multiplication table")
number = int(input("Which table do you want? "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# ---- part 3: running total (accumulator) ----
# make a variable that starts at 0 and keep adding to it inside the loop
print("\nPart 3: sum of 1 to 100")
total = 0
for i in range(1, 101):      # 101 because range stops before the last number
    total = total + i        # same as total += i
print("The sum of 1 to 100 is", total)

# same idea but with a counter to count even numbers
even_count = 0
for i in range(1, 101):
    if i % 2 == 0:           # % gives the remainder (from file 02/01)
        even_count = even_count + 1
print("Even numbers from 1 to 100:", even_count)

# ---- part 4: while loop ----
# a for loop runs a set number of times
# a while loop keeps going as long as the condition is True
print("\nPart 4: while loop")
count = 1
while count <= 5:
    print("count is", count)
    count = count + 1        # if I forget this line the loop never ends!

# ---- part 5: break and continue ----
# break = stop the whole loop right now
# continue = skip the rest of this round and go to the next one
print("\nPart 5: break and continue")
for i in range(1, 11):
    if i == 3:
        continue             # skips 3, so 3 never gets printed
    if i == 7:
        break                # stops the loop at 7, so 7 is not printed either
    print("number:", i)

# ---- part 6: input validation ----
# keep asking until the user types something valid
print("\nPart 6: input validation")
age = int(input("Enter your age (1 to 120): "))
while age < 1 or age > 120:  # "or" from file 02
    print("That's not a valid age, try again.")
    age = int(input("Enter your age (1 to 120): "))
print("Thanks! Your age is", age)

# ---- part 7: looping through a string ----
# a for loop can go through text one letter at a time
print("\nPart 7: looping through a string")
word = input("Type a word: ")
vowels = 0
for letter in word:
    print(letter)
    if letter.lower() in "aeiou":   # .lower() so capital letters count too
        vowels = vowels + 1
print("The word", word, "has", vowels, "vowels")

# ---------------------------------------------------------------
# What I learned
# ---------------------------------------------------------------
# - for loops repeat something a set number of times, and range()
#   makes the numbers (it stops BEFORE the last number)
# - range(start, stop, step) lets me choose where to start and how
#   much to jump
# - the running total pattern: start at 0, then total = total + i
#   inside the loop
# - while loops keep going while the condition is True, so I need to
#   change something inside or it runs forever
# - break stops the loop completely, continue just skips one round
# - a while loop is good for input validation (ask again until the
#   answer is okay)
# - I can loop through a string and get one letter at a time
