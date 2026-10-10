"""
Lists in Python
This script explains lists with easy chunks and examples.
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Lists are collections of items
# ------------------------------------------------------------
print_section("Chunk 1: Lists are collections")

fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", True, 3.5]

print("fruits =", fruits, "type:", type(fruits))
print("numbers =", numbers, "type:", type(numbers))
print("mixed =", mixed, "type:", type(mixed))

# Lists can contain different types of values.
print("A list can hold strings, numbers, and booleans.")


# ------------------------------------------------------------
# 2. Accessing items in a list
# ------------------------------------------------------------
print_section("Chunk 2: Accessing list items")

print("fruits[0] =", fruits[0])
print("fruits[1] =", fruits[1])
print("fruits[-1] =", fruits[-1])
print("fruits[0:2] =", fruits[0:2])
print("fruits[1:] =", fruits[1:])
print("fruits[:2] =", fruits[:2])

print("numbers[2] =", numbers[2]) 
print("numbers[-2] =", numbers[-2])
print("numbers[0:2] =", numbers[0:2])
print("numbers[1:] =", numbers[1:])
print("numbers[:3] =", numbers[:3])

# Indexing starts from 0 in Python.
print("The first item is at index 0.")


# ------------------------------------------------------------
# 3. Changing items in a list
# ------------------------------------------------------------
print_section("Chunk 3: Updating list values")

colors = ["red", "green", "blue"]
colors[1] = "yellow"
colors[-3] = "orange"
colors[0:2] = ["purple", "pink"]
colors.append("brown")
colors.insert(2, "cyan")
print("colors after update:", colors)

colors.append("purple")
print("colors after append:", colors)


# ------------------------------------------------------------
# 4. Length of a list
# ------------------------------------------------------------
print_section("Chunk 4: Finding list size")

print("Length of fruits:", len(fruits))
print("Length of numbers:", len(numbers))
print("Length of colors:", len(colors))


# ------------------------------------------------------------
# 5. Adding items to a list
# ------------------------------------------------------------
print_section("Chunk 5: Adding items")

students = ["Asha", "Ravi"]
students.append("Meera")
print("After append:", students)

students.insert(1, "Kiran")
print("After insert:", students)

students.extend(["Anu", "Sam"])
print("After extend:", students)


# ------------------------------------------------------------
# 6. Removing items from a list
# ------------------------------------------------------------
print_section("Chunk 6: Removing items")

numbers_list = [10, 20, 30, 40, 50]
print("Before remove:", numbers_list)

numbers_list.remove(30)
print("After remove(30):", numbers_list)

popped = numbers_list.pop()
print("After pop():", numbers_list)
print("Popped item:", popped)

numbers_list.clear()
print("After clear():", numbers_list)


# ------------------------------------------------------------
# 7. Sorting and reversing
# ------------------------------------------------------------
print_section("Chunk 7: Sorting and reversing")

nums = [5, 2, 9, 1, 7]
print("Original:", nums)

nums.sort()
print("After sort():", nums)

nums.reverse()
print("After reverse():", nums)


# ------------------------------------------------------------
# 8. List operations
# ------------------------------------------------------------
print_section("Chunk 8: List operations")

list1 = [1, 2, 3]
list2 = [4, 5]

print("list1 + list2 =", list1 + list2)
print("list1 * 3 =", list1 * 3)
print("2 in list1?", 2 in list1)
print("9 in list1?", 9 in list1)
print("3 in list1 and 4 in list2?", 3 in list1 and 4 in list2)


# ------------------------------------------------------------
# 9. Slicing and copying
# ------------------------------------------------------------
print_section("Chunk 9: Slicing and copying")

letters = ["A", "B", "C", "D", "E"]
print("letters =", letters)
print("letters[1:4] =", letters[1:4])
print("letters[:3] =", letters[:3])
print("letters[::2] =", letters[::2])

copy_list = letters.copy()
print("copy_list =", copy_list)


# ------------------------------------------------------------
# 10. Looping through a list
# ------------------------------------------------------------
print_section("Chunk 10: Iterating through a list")

for fruit in fruits:
    print("Fruit:", fruit)

print("Sum of numbers:", sum([1, 2, 3, 4, 5]))
print("Maximum value:", max([10, 7, 15, 3]))
print("Minimum value:", min([10, 7, 15, 3]))


# ------------------------------------------------------------
# 11. Real-world example
# ------------------------------------------------------------
print_section("Chunk 11: Real-world list example")

cart = ["bread", "milk", "eggs"]
print("Shopping cart:", cart)
cart.append("banana")
print("After buying banana:", cart)
cart.remove("milk")
print("After removing milk:", cart)
print("Items in cart:", len(cart))


# ------------------------------------------------------------
# 12. Summary
# ------------------------------------------------------------
print_section("Chunk 12: Summary")

print("Lists are used to store multiple values in one variable.")
print("You can access, update, add, remove, slice, sort, and loop through lists.")
print("Common list methods: append(), insert(), remove(), pop(), sort(), reverse(), copy()")
print("Lists are one of the most important data types in Python.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. print([1, 2, 3])")
print("2. print(['a', 'b'][0])")
print("3. print(len([10, 20, 30]))")
print("4. print([1, 2, 3] + [4])")
print("5. print([1, 2, 3].append(4))")
print("6. print([3, 1, 2].sort())")
print("7. print('a' in ['a', 'b', 'c'])")
print("8. print([5, 10, 15][1:])")

# Real practice code examples
print([1, 2, 3])
print(['a', 'b'][0])
print(len([10, 20, 30]))
print([1, 2, 3] + [4])
print([1, 2, 3].append(4))
print([3, 1, 2].sort())
print('a' in ['a', 'b', 'c'])
print([5, 10, 15][1:])

# Real practice examples
print("Example 1:", [1, 2, 3])
print("Example 2:", ["a", "b"][0])
print("Example 3:", len([10, 20, 30]))
print("Example 4:", [1, 2, 3] + [4])
print("Example 5:", [1, 2, 3])
print("Example 6:", [3, 1, 2])
print("Example 7:", "a" in ["a", "b", "c"])
print("Example 8:", [5, 10, 15][1:])

print("\nPractice makes it easier to understand lists in Python!")
