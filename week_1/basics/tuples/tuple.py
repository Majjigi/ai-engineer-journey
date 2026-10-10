"""
Tuples in Python
This script explains tuples with easy chunks and examples.
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Tuples are ordered collections
# ------------------------------------------------------------
print_section("Chunk 1: Tuples are ordered collections")

point = (10, 20)
colors = ("red", "green", "blue")
mixed = (1, "hello", True)

print("point =", point, "type:", type(point))
print("colors =", colors, "type:", type(colors))
print("mixed =", mixed, "type:", type(mixed))

# Tuples are immutable, meaning they cannot be changed once created.
print("Tuples cannot be modified after creation.")


# ------------------------------------------------------------
# 2. Creating tuples
# ------------------------------------------------------------
print_section("Chunk 2: Creating tuples")

empty_tuple = ()
name_tuple = ("Alice",)
nums = (1, 2, 3, 4)

print("empty_tuple =", empty_tuple)
print("name_tuple =", name_tuple)
print("nums =", nums)


# ------------------------------------------------------------
# 3. Accessing tuple items
# ------------------------------------------------------------
print_section("Chunk 3: Accessing tuple items")

print("point[0] =", point[0])
print("point[1] =", point[1])
print("colors[-1] =", colors[-1])
print("nums[1:3] =", nums[1:3])
print("nums[:2] =", nums[:2])


# ------------------------------------------------------------
# 4. Tuple length
# ------------------------------------------------------------
print_section("Chunk 4: Finding tuple size")

print("Length of point:", len(point))
print("Length of colors:", len(colors))
print("Length of nums:", len(nums))


# ------------------------------------------------------------
# 5. Concatenation and repetition
# ------------------------------------------------------------
print_section("Chunk 5: Joining tuples")

first = (1, 2)
second = (3, 4)
print("first + second =", first + second)
print("first * 3 =", first * 3)


# ------------------------------------------------------------
# 6. Tuple unpacking
# ------------------------------------------------------------
print_section("Chunk 6: Unpacking tuples")

x, y = point
print("x =", x)
print("y =", y)

p1, p2, p3 = colors
print("p1 =", p1)
print("p2 =", p2)
print("p3 =", p3)


# ------------------------------------------------------------
# 7. Counting and searching
# ------------------------------------------------------------
print_section("Chunk 7: Counting and searching")

sample = (1, 2, 2, 3, 4, 2)
print("sample.count(2) =", sample.count(2))
print("sample.index(3) =", sample.index(3))


# ------------------------------------------------------------
# 8. Iterating through a tuple
# ------------------------------------------------------------
print_section("Chunk 8: Looping through a tuple")

for color in colors:
    print("Color:", color)


# ------------------------------------------------------------
# 9. Tuple methods
# ------------------------------------------------------------
print_section("Chunk 9: Tuple methods")

print("colors.count('red') =", colors.count("red"))
print("colors.index('green') =", colors.index("green"))


# ------------------------------------------------------------
# 10. Real-world example
# ------------------------------------------------------------
print_section("Chunk 10: Real-world tuple example")

coord = (40.7128, -74.0060)
print("Coordinates:", coord)
print("Latitude:", coord[0])
print("Longitude:", coord[1])


# ------------------------------------------------------------
# 11. Summary
# ------------------------------------------------------------
print_section("Chunk 11: Summary")

print("Tuples are ordered and immutable.")
print("They are useful for fixed data that should not change.")
print("Common operations: indexing, slicing, concatenation, unpacking, count(), index()")
print("Tuples are often used for coordinates, records, and fixed values.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. print((1, 2, 3))")
print("2. print((10, 20)[0])")
print("3. print(len((1, 2, 3)))")
print("4. print((1, 2) + (3, 4))")
print("5. print((1, 2, 2).count(2))")
print("6. print((3, 1, 2).index(1))")
print("7. print(('a', 'b', 'c')[1:])")
print("8. x, y = (5, 10); print(x, y)")

print("Practice makes it easier to understand tuples in Python!")
print((1, 2, 3));
print((10, 20)[0]); 
print(len((1, 2, 3)));
print((1, 2) + (3, 4));
print((1, 2, 2).count(2));
print((3, 1, 2).index(1));
print(('a', 'b', 'c')[1:]);
x, y = (5, 10)
print(x, y)

print("Example 1:", (1, 2, 3))
print("Example 2:", (10, 20)[0])
print("Example 3:", len((1, 2, 3)))
print("Example 4:", (1, 2) + (3, 4))
print("Example 5:", (1, 2, 2).count(2))
print("Example 6:", (3, 1, 2).index(1))
print("Example 7:", ("a", "b", "c")[1:])

x, y = (5, 10)
print("Example 8:", x, y)

print("\nPractice makes it easier to understand tuples in Python!")
