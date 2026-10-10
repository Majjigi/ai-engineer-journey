"""
Conditions in Python
This script explains if, elif, else, comparison operators, and boolean logic.
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Comparison operators
# ------------------------------------------------------------
print_section("Chunk 1: Comparison operators")

print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("8 > 3:", 8 > 3)
print("2 < 9:", 2 < 9)
print("10 >= 10:", 10 >= 10)
print("4 <= 7:", 4 <= 7)


# ------------------------------------------------------------
# 2. If statement
# ------------------------------------------------------------
print_section("Chunk 2: If statement")

age = 18
if age >= 18:
    print("You are an adult.")

score = 75
if score >= 60:
    print("You passed the exam.")


# ------------------------------------------------------------
# 3. If else statement
# ------------------------------------------------------------
print_section("Chunk 3: If-else statement")

marks = 45
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# ------------------------------------------------------------
# 4. If elif else statement
# ------------------------------------------------------------
print_section("Chunk 4: If-elif-else")

number = 0
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# ------------------------------------------------------------
# 5. Logical operators
# ------------------------------------------------------------
print_section("Chunk 5: Logical operators")

x = 10
print("x > 5 and x < 15:", x > 5 and x < 15)
print("x > 12 or x < 5:", x > 12 or x < 5)
print("not (x == 10):", not (x == 10))


# ------------------------------------------------------------
# 6. Nested conditions
# ------------------------------------------------------------
print_section("Chunk 6: Nested conditions")

has_id = True
is_adult = True

if has_id:
    if is_adult:
        print("You can enter the club.")
    else:
        print("You are too young.")
else:
    print("Please show your ID.")


# ------------------------------------------------------------
# 7. Using conditions with strings
# ------------------------------------------------------------
print_section("Chunk 7: Conditions with strings")

name = "Alice"
if name == "Alice":
    print("Hello Alice!")
else:
    print("Unknown user")


# ------------------------------------------------------------
# 8. Conditions with lists
# ------------------------------------------------------------
print_section("Chunk 8: Conditions with lists")

items = ["book", "pen"]
if "book" in items:
    print("The book is in the list.")
else:
    print("The book is not in the list.")


# ------------------------------------------------------------
# 9. Real-world example
# ------------------------------------------------------------
print_section("Chunk 9: Real-world example")

temperature = 31
if temperature > 30:
    print("It is very hot outside.")
elif temperature > 20:
    print("The weather is pleasant.")
else:
    print("It is cold.")


# ------------------------------------------------------------
# 10. Summary
# ------------------------------------------------------------
print_section("Chunk 10: Summary")

print("Conditions let your program make decisions.")
print("Use if, elif, and else to check different cases.")
print("Comparison operators compare values.")
print("Logical operators combine conditions.")
print("Conditions are used in everyday programs like login, grading, and filtering.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. if 5 > 3: print('Yes')")
print("2. if 10 % 2 == 0: print('Even')")
print("3. if 7 < 5: print('Small') else: print('Big')")
print("4. if x > 0: print('Positive')")
print("5. age = 20; if age >= 18: print('Adult')")
print("6. if 'a' in 'apple': print('Found')")

if 5 > 3:
    print("Example 1: Yes")

if 10 % 2 == 0:
    print("Example 2: Even")

if 7 < 5:
    print("Small")
else:
    print("Example 3: Big")

x = 7
if x > 0:
    print("Example 4: Positive")

age = 20
if age >= 18:
    print("Example 5: Adult")

if 'a' in 'apple':
    print("Example 6: Found")

print("\nPractice makes it easier to understand conditions in Python!")
