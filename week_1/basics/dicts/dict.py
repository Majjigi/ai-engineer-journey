"""
Dictionaries in Python
This script explains dictionaries with easy chunks and examples.
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Dictionaries store key-value pairs
# ------------------------------------------------------------
print_section("Chunk 1: Dictionaries store key-value pairs")

student = {"name": "Aisha", "age": 21, "city": "Hyderabad"}
print("student =", student)
print("type:", type(student))

# Each key is paired with a value.
print("student['name'] =", student["name"])
print("student['age'] =", student["age"])


# ------------------------------------------------------------
# 2. Creating a dictionary
# ------------------------------------------------------------
print_section("Chunk 2: Creating dictionaries")

empty_dict = {}
car = {"brand": "Toyota", "model": "Corolla", "year": 2024}
person = {"first_name": "John", "last_name": "Doe", "email": "john@example.com"}

print("empty_dict =", empty_dict)
print("car =", car)
print("person =", person)


# ------------------------------------------------------------
# 3. Accessing values
# ------------------------------------------------------------
print_section("Chunk 3: Accessing values")

print("car['brand'] =", car["brand"])
print("car.get('model') =", car.get("model"))
print("person.get('email') =", person.get("email"))

# If a key does not exist, .get() returns None instead of raising an error.
print("person.get('phone') =", person.get("phone"))


# ------------------------------------------------------------
# 4. Adding and updating values
# ------------------------------------------------------------
print_section("Chunk 4: Adding and updating data")

student["course"] = "Python"
print("After adding course:", student)

student["age"] = 22
print("After updating age:", student)


# ------------------------------------------------------------
# 5. Removing items
# ------------------------------------------------------------
print_section("Chunk 5: Removing items")

book = {"title": "Python Basics", "author": "Sam", "pages": 180}
print("Before remove:", book)

removed_value = book.pop("pages")
print("After pop('pages'):", book)
print("Removed value:", removed_value)

book.popitem()
print("After popitem():", book)

book.clear()
print("After clear():", book)


# ------------------------------------------------------------
# 6. Checking keys and values
# ------------------------------------------------------------
print_section("Chunk 6: Keys, values, and items")

product = {"name": "Laptop", "price": 75000, "stock": 10}
print("Keys:", product.keys())
print("Values:", product.values())
print("Items:", product.items())

print("Is 'name' in product?", "name" in product)
print("Is 'price' in product?", "price" in product)


# ------------------------------------------------------------
# 7. Looping through a dictionary
# ------------------------------------------------------------
print_section("Chunk 7: Iterating through a dictionary")

for key in student:
    print("Key:", key, "Value:", student[key])

print("\nLooping through keys:")
for k in product:
    print(k)

print("\nLooping through values:")
for v in product.values():
    print(v)

print("\nLooping through key-value pairs:")
for key, value in product.items():
    print(key, "=>", value)


# ------------------------------------------------------------
# 8. Nested dictionaries
# ------------------------------------------------------------
print_section("Chunk 8: Nested dictionaries")

employee = {
    "name": "Rahul",
    "details": {
        "age": 28,
        "role": "Developer",
        "city": "Bengaluru"
    }
}

print("employee =", employee)
print("employee['details']['role'] =", employee["details"]["role"])
print("employee['details']['city'] =", employee["details"]["city"])


# ------------------------------------------------------------
# 9. Dictionary length
# ------------------------------------------------------------
print_section("Chunk 9: Finding dictionary size")

print("Length of student:", len(student))
print("Length of car:", len(car))
print("Length of product:", len(product))


# ------------------------------------------------------------
# 10. Real-world example
# ------------------------------------------------------------
print_section("Chunk 10: Real-world dictionary example")

shopping_cart = {
    "items": ["bread", "milk", "eggs"],
    "total": 250,
    "status": "pending"
}

print("Shopping cart:", shopping_cart)
print("Items:", shopping_cart["items"])
print("Total:", shopping_cart["total"])
shopping_cart["status"] = "paid"
print("Updated status:", shopping_cart["status"])


# ------------------------------------------------------------
# 11. Summary
# ------------------------------------------------------------
print_section("Chunk 11: Summary")

print("Dictionaries store data as key-value pairs.")
print("Keys are unique and used to access values.")
print("You can add, update, remove, loop, and nest dictionaries.")
print("Common methods: get(), keys(), values(), items(), pop(), popitem(), clear()")
print("Dictionaries are very useful for storing structured data.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. print({'name': 'Alice', 'age': 20})")
print("2. print({'a': 1, 'b': 2}['a'])")
print("3. print({'x': 1}.get('y'))")
print("4. print({'one': 1, 'two': 2}.keys())")
print("5. print({'one': 1, 'two': 2}.values())")
print("6. print(len({'a': 1, 'b': 2}))")
print("7. print('name' in {'name': 'John'})")
print("8. print({'details': {'city': 'Delhi'}}['details']['city'])")

# Real practice code examples
print("Example 1:", {"name": "Alice", "age": 20})
print("Example 2:", {"a": 1, "b": 2}["a"])
print("Example 3:", {"x": 1}.get("y"))
print("Example 4:", {"one": 1, "two": 2}.keys())
print("Example 5:", {"one": 1, "two": 2}.values())
print("Example 6:", len({"a": 1, "b": 2}))
print("Example 7:", "name" in {"name": "John"})
print("Example 8:", {"details": {"city": "Delhi"}}["details"]["city"])

print("\nPractice makes it easier to understand dictionaries in Python!")
