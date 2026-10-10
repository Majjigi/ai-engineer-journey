# Simple examples to understand f-strings in Python
#
name = "Alice"
age = 30
city = "Paris"

# Basic f-string
print(f"Hello, {name}!")

# f-string with expressions
print(f"{name} is {age} years old.")

# f-string with multiple values
print(f"{name} lives in {city}.")

# Formatting numbers
pi = 3.14159
print(f"Value of pi: {pi:.2f}")

# Using dictionary values
person = {"name": "Bob", "age": 25}
print(f"{person['name']} is {person['age']} years old.")

# Using arithmetic inside f-string
print(f"Next year, {name} will be {age + 1}.")
