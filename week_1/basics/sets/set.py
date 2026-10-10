"""
Sets in Python
This script explains sets with easy chunks and examples.
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Sets are unordered collections
# ------------------------------------------------------------
print_section("Chunk 1: Sets are unordered collections")

numbers = {1, 2, 3, 4, 5}
letters = {"a", "b", "c"}
print("numbers =", numbers, "type:", type(numbers))
print("letters =", letters, "type:", type(letters))

# A set cannot have duplicate values.
print("duplicates removed:", {1, 2, 2, 3, 3, 4})


# ------------------------------------------------------------
# 2. Creating sets
# ------------------------------------------------------------
print_section("Chunk 2: Creating sets")

empty_set = set()
fruits = {"apple", "banana", "mango"}
colors = set(["red", "green", "blue"])

print("empty_set =", empty_set)
print("fruits =", fruits)
print("colors =", colors)


# ------------------------------------------------------------
# 3. Adding and removing items
# ------------------------------------------------------------
print_section("Chunk 3: Adding and removing items")

animals = {"cat", "dog"}
animals.add("lion")
print("After add:", animals)

animals.remove("dog")
print("After remove:", animals)

animals.discard("tiger")
print("After discard:", animals)


# ------------------------------------------------------------
# 4. Set operations
# ------------------------------------------------------------
print_section("Chunk 4: Set operations")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("A =", set_a)
print("B =", set_b)
print("A union B =", set_a | set_b)
print("A intersection B =", set_a & set_b)
print("A difference B =", set_a - set_b)
print("A symmetric difference B =", set_a ^ set_b)


# ------------------------------------------------------------
# 5. Length of a set
# ------------------------------------------------------------
print_section("Chunk 5: Finding set size")

print("Length of numbers:", len(numbers))
print("Length of fruits:", len(fruits))
print("Length of animals:", len(animals))


# ------------------------------------------------------------
# 6. Membership test
# ------------------------------------------------------------
print_section("Chunk 6: Checking membership")

print("3 in numbers?", 3 in numbers)
print("8 in numbers?", 8 in numbers)
print("'banana' in fruits?", "banana" in fruits)
print("'grape' in fruits?", "grape" in fruits)


# ------------------------------------------------------------
# 7. Looping through a set
# ------------------------------------------------------------
print_section("Chunk 7: Iterating through a set")

for item in fruits:
    print("Fruit:", item)


# ------------------------------------------------------------
# 8. Set comprehension
# ------------------------------------------------------------
print_section("Chunk 8: Set comprehension")

squares = {x * x for x in range(1, 6)}
print("Squares:", squares)

# Only unique values remain in a set.
names = ["Alice", "Bob", "Alice", "Charlie"]
unique_names = {name for name in names}
print("Unique names:", unique_names)


# ------------------------------------------------------------
# 9. Real-world example
# ------------------------------------------------------------
print_section("Chunk 9: Real-world set example")

cart1 = {"apple", "banana", "milk"}
cart2 = {"banana", "bread", "eggs"}

common_items = cart1 & cart2
print("Cart 1:", cart1)
print("Cart 2:", cart2)
print("Common items:", common_items)
print("All items in either cart:", cart1 | cart2)


# ------------------------------------------------------------
# 10. Summary
# ------------------------------------------------------------
print_section("Chunk 10: Summary")

print("Sets store unique items without order.")
print("You can add, remove, and check membership.")
print("Sets support mathematical operations like union and intersection.")
print("Sets are useful when you need unique values only.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. print({1, 2, 3})")
print("2. print({1, 2, 2, 3})")
print("3. print(len({1, 2, 3}))")
print("4. print({1, 2, 3} | {3, 4})")
print("5. print({1, 2, 3} & {3, 4})")
print("6. print(2 in {1, 2, 3})")
print("7. print({x for x in range(5)})")
print("8. print({'apple', 'banana'} - {'banana'})")

print("Example 1:", {1, 2, 3})
print("Example 2:", {1, 2, 2, 3})
print("Example 3:", len({1, 2, 3}))
print("Example 4:", {1, 2, 3} | {3, 4})
print("Example 5:", {1, 2, 3} & {3, 4})
print("Example 6:", 2 in {1, 2, 3})
print("Example 7:", {x for x in range(5)})
print("Example 8:", {"apple", "banana"} - {"banana"})

print("\nPractice makes it easier to understand sets in Python!")
