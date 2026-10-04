
"""
Number Fundamentals in Python
This script explains the main number types and operations in easy-to-understand chunks.
"""

import math


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Integer numbers (int)
# ------------------------------------------------------------
print_section("Chunk 1: Integers (int)")

age = 25
score = 100
temperature = -10

print("age =", age, "type:", type(age))
print("score =", score, "type:", type(score))
print("temperature =", temperature, "type:", type(temperature))

print("Addition:", 10 + 5)
print("Subtraction:", 20 - 7)
print("Multiplication:", 6 * 4)
print("Division:", 20 / 5)
print("Floor division:", 20 // 3)
print("Modulus:", 20 % 3)
print("Exponent:", 2 ** 5)


# ------------------------------------------------------------
# 2. Decimal numbers (float)
# ------------------------------------------------------------
print_section("Chunk 2: Floating-point numbers (float)")

price = 19.99
height = 5.8
pi_value = 3.14159

print("price =", price, "type:", type(price))
print("height =", height, "type:", type(height))
print("pi_value =", pi_value, "type:", type(pi_value))

print("Addition:", 2.5 + 1.5)
print("Subtraction:", 8.4 - 2.1)
print("Multiplication:", 3.5 * 2)
print("Division:", 10 / 4)
print("Power:", 2.0 ** 3)

# Important: floats can have precision limits in Python.
print("Precision example:", 0.1 + 0.2)


# ------------------------------------------------------------
# 3. Complex numbers
# ------------------------------------------------------------
print_section("Chunk 3: Complex numbers")

z1 = 3 + 4j
z2 = 2 - 1j

print("z1 =", z1, "type:", type(z1))
print("z2 =", z2, "type:", type(z2))
print("Addition:", z1 + z2)
print("Multiplication:", z1 * z2)
print("Real part:", z1.real)
print("Imaginary part:", z1.imag)


# ------------------------------------------------------------
# 4. Number operations in Python
# ------------------------------------------------------------
print_section("Chunk 4: Basic arithmetic operations")

x = 12
y = 5

print("x =", x, "y =", y)
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)

# Parentheses change the order of operations.
result = (10 + 5) * 3 - 4
print("(10 + 5) * 3 - 4 =", result)


# ------------------------------------------------------------
# 5. Comparison operators
# ------------------------------------------------------------
print_section("Chunk 5: Comparing numbers")

print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("7 > 3:", 7 > 3)
print("4 < 9:", 4 < 9)
print("10 >= 10:", 10 >= 10)
print("2 <= 1:", 2 <= 1)

# Comparison is often used in conditions.
mark = 85
print("Is mark greater than or equal to 80?", mark >= 80)


# ------------------------------------------------------------
# 6. Type conversion
# ------------------------------------------------------------
print_section("Chunk 6: Converting numbers from one type to another")

num_str = "42"
print("Original string:", num_str, "type:", type(num_str))

num_int = int(num_str)
print("int('42') =", num_int, "type:", type(num_int))

num_float = float("3.14")
print("float('3.14') =", num_float, "type:", type(num_float))

num_str_again = str(123)
print("str(123) =", num_str_again, "type:", type(num_str_again))

print("int(7.9) =", int(7.9))
print("round(7.9) =", round(7.9))
print("round(7.49) =", round(7.49))


# ------------------------------------------------------------
# 7. Boolean values are numbers in Python
# ------------------------------------------------------------
print_section("Chunk 7: Boolean values")

is_active = True
is_admin = False

print("is_active =", is_active, "type:", type(is_active))
print("is_admin =", is_admin, "type:", type(is_admin))

print("True as int:", int(True))
print("False as int:", int(False))
print("True == 1:", True == 1)
print("False == 0:", False == 0)


# ------------------------------------------------------------
# 8. Math module
# ------------------------------------------------------------
print_section("Chunk 8: Using Python math functions")

print("square root of 16:", math.sqrt(16))
print("absolute value of -12:", abs(-12))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.9):", math.floor(4.9))
print("power: 2^8 =", pow(2, 8))
print("log(100):", math.log(100))
print("pi:", math.pi)
print("e:", math.e)


# ------------------------------------------------------------
# 9. A practical example
# ------------------------------------------------------------
print_section("Chunk 9: Real-world number example")

items = 4
price_per_item = 12.5
discount = 10

subtotal = items * price_per_item
discount_amount = subtotal * discount / 100
final_total = subtotal - discount_amount

print("Items:", items)
print("Price per item:", price_per_item)
print("Subtotal:", subtotal)
print("Discount:", discount, "%")
print("Discount amount:", discount_amount)
print("Final total:", final_total)


# ------------------------------------------------------------
# 10. Summary
# ------------------------------------------------------------
print_section("Chunk 10: Summary")

print("Python has several numeric types:")
print("- int: whole numbers like 10, -3, 0")
print("- float: decimal numbers like 3.14, 2.0")
print("- complex: numbers like 3 + 4j")
print("- bool: True/False, which behave like 1 and 0")
print("\nPython supports arithmetic, comparisons, conversions, and math functions.")
print("These are the building blocks for calculations in programming!")


# ------------------------------------------------------------
# Optional extra challenge
# ------------------------------------------------------------
print_section("Extra Challenge")

# Try these in the Python shell:
# 1. print(5 + 7)
# 2. print(10 / 3)
# 3. print(10 // 3)
# 4. print(float("9.5"))
# 5. print(complex(2, 3))
# 6. print(round(2.675, 2))

print("Practice makes it easy to understand numbers in Python!")

print(++1) # This will print 1, as the unary plus operator does not change the value.
print(--1) # This will print -1, as the unary minus operator negates the value. 

print(5+3)
print(5//265)
print(10-10.523)
print(float("3.14"))
print(complex(1, 2))
print(round(2.675, 2))

print("\nEnd of Number Fundamentals in Python.");