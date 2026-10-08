# 04_lists.py
# Topic: lists
# Uses things from 01 (variables, input, int), 02 (if, in/comparisons)
# and 03 (for loops, running total, while loop)

# ---- part 1: making a list ----
# a list holds many values in one variable, written inside [ ]
print("Part 1: making lists")
marks = [45, 72, 88, 60, 91]
fruits = ["apple", "banana", "mango"]
mixed = ["Ravi", 21, 5.8, True]    # a list can hold different types too
empty = []                         # empty list, I can add stuff later

print(marks)
print(fruits)
print(mixed)
print("empty list:", empty)
print(type(marks))                 # <class 'list'>

# ---- part 2: indexing ----
# every item has a position number called an index
# it starts at 0, not 1! (the first item is 0 steps from the start)
print("\nPart 2: indexing")
print("first mark:", marks[0])
print("second mark:", marks[1])
print("fifth mark:", marks[4])
# marks[5] would give an IndexError because the last index is 4
# (5 items -> indexes 0,1,2,3,4)

# negative index counts from the END
print("last mark:", marks[-1])          # -1 is the last item
print("second last mark:", marks[-2])

# ---- part 3: slicing ----
# list[start:stop] -> includes start, stops BEFORE stop (like range)
print("\nPart 3: slicing")
print("marks[1:4] =", marks[1:4])       # index 1, 2, 3
print("marks[:3] =", marks[:3])         # nothing before colon = from the start
print("marks[2:] =", marks[2:])         # nothing after colon = till the end
print("marks[-2:] =", marks[-2:])       # last two items

# ---- part 4: changing a list ----
print("\nPart 4: changing a list")
pets = ["dog", "cat", "fish"]
print("start:", pets)

pets.append("rabbit")           # adds to the END
print("after append:", pets)

pets.insert(1, "parrot")        # insert(position, item) puts it at that index
print("after insert:", pets)

pets.remove("cat")              # removes the item by its VALUE
print("after remove:", pets)

last_one = pets.pop()           # removes the last item AND gives it back
print("popped:", last_one)
print("after pop:", pets)

pets.pop(0)                     # pop(0) removes the item at index 0
print("after pop(0):", pets)

pets[0] = "hamster"             # change a value using its index
print("after changing index 0:", pets)

# ---- part 5: useful functions ----
print("\nPart 5: len, sum, min, max, sorted")
print("how many marks:", len(marks))
print("total:", sum(marks))
print("lowest:", min(marks))
print("highest:", max(marks))
print("sorted:", sorted(marks))
print("sorted backwards:", sorted(marks, reverse=True))
print("original is still the same:", marks)   # sorted() doesn't change the list

# ---- part 6: looping through a list ----
print("\nPart 6: looping")
for fruit in fruits:
    print("I like", fruit)

# if I need the index as well I can use range(len(...))
for i in range(len(fruits)):
    print(i, "->", fruits[i])

# ---- part 7: checking if something is in a list ----
print("\nPart 7: using in")
print("banana" in fruits)          # True
print("grapes" in fruits)          # False
if "mango" in fruits:
    print("yes we have mango")
if "grapes" not in fruits:
    print("no grapes, need to buy some")

# ---- part 8: marks analysis ----
# using the loop + running total idea from file 03
print("\nPart 8: marks analysis")
class_marks = [56, 78, 91, 45, 67, 83, 39]

total = 0
for m in class_marks:
    total = total + m
average = total / len(class_marks)

highest = max(class_marks)
lowest = min(class_marks)

print("marks:", class_marks)
print("average:", round(average, 2))      # round(x, 2) = 2 decimal places
print("highest:", highest)
print("lowest:", lowest)

passed = 0
for m in class_marks:
    if m >= 40:                           # if from file 02
        passed = passed + 1
print(passed, "out of", len(class_marks), "students passed")

# ---- part 9: shopping list ----
print("\nPart 9: shopping list")
shopping = ["milk", "bread", "eggs"]
print("my list:", shopping)

item = input("What else do you need to buy? ")
if item in shopping:
    print(item, "is already on the list")
else:
    shopping.append(item)
    print("added", item)

print("final list:")
for i in range(len(shopping)):
    print(i + 1, "-", shopping[i])        # i + 1 so it starts from 1
print("total items:", len(shopping))

# ---- part 10: collect numbers until 'done' ----
# while loop from file 03 + list append
print("\nPart 10: collect numbers")
numbers = []
while True:
    entry = input("Enter a number (or type done): ")
    if entry == "done":
        break                             # break from file 03
    numbers.append(int(entry))            # input is text so int() first

if len(numbers) == 0:
    print("You didn't enter any numbers.")
else:
    print("You entered:", numbers)
    print("count:", len(numbers))
    print("sum:", sum(numbers))
    print("average:", round(sum(numbers) / len(numbers), 2))
    print("biggest:", max(numbers))
    print("smallest:", min(numbers))

# ---------------------------------------------------------------
# What I learned
# ---------------------------------------------------------------
# - a list stores many values in one variable, made with [ ]
# - indexing starts at 0, so the last index is len(list) - 1
# - negative index counts from the end (-1 is the last item)
# - slicing [start:stop] includes start but stops BEFORE stop
# - append() adds at the end, insert(i, x) adds at a position,
#   remove(x) removes by value, pop() removes by position (default last)
# - I can change an item with list[i] = new_value
# - len, sum, min, max work on lists, and sorted() gives a new sorted
#   list without changing the original
# - for item in list loops through every item
# - "x in list" checks if something is in the list (True/False)
# - the running total from file 03 is basically what sum() does
# - while True + break is useful when I don't know how many times
#   the loop should run
