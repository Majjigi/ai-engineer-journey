"""
Loops in Python
This script explains for loops, while loops, break, continue, and range().
"""


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. For loop
# ------------------------------------------------------------
print_section("Chunk 1: For loop")

for i in range(1, 6):
    print("Number:", i)


# ------------------------------------------------------------
# 2. Looping through a list
# ------------------------------------------------------------
print_section("Chunk 2: Looping through a list")

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)


# ------------------------------------------------------------
# 3. Looping through a string
# ------------------------------------------------------------
print_section("Chunk 3: Looping through a string")

for ch in "Python":
    print("Character:", ch)


# ------------------------------------------------------------
# 4. While loop
# ------------------------------------------------------------
print_section("Chunk 4: While loop")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# ------------------------------------------------------------
# 5. Break statement
# ------------------------------------------------------------
print_section("Chunk 5: Break statement")

for i in range(1, 10):
    if i == 5:
        break
    print("Value:", i)


# ------------------------------------------------------------
# 6. Continue statement
# ------------------------------------------------------------
print_section("Chunk 6: Continue statement")

for i in range(1, 7):
    if i == 3:
        continue
    print("Value:", i)


# ------------------------------------------------------------
# 7. Range function
# ------------------------------------------------------------
print_section("Chunk 7: Range function")

print("range(5):", list(range(5)))
print("range(2, 8):", list(range(2, 8)))
print("range(1, 10, 2):", list(range(1, 10, 2)))


# ------------------------------------------------------------
# 8. Nested loops
# ------------------------------------------------------------
print_section("Chunk 8: Nested loops")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i * j)


# ------------------------------------------------------------
# 9. Else with loops
# ------------------------------------------------------------
print_section("Chunk 9: Else with loops")

for i in range(1, 4):
    print("Looping:", i)
else:
    print("Loop finished without break.")


# ------------------------------------------------------------
# 10. Real-world example
# ------------------------------------------------------------
print_section("Chunk 10: Real-world example")

items = ["milk", "bread", "eggs"]
for item in items:
    print("Shopping item:", item)

print("Done shopping!")


# ------------------------------------------------------------
# 11. Summary
# ------------------------------------------------------------
print_section("Chunk 11: Summary")

print("For loops are used when you know how many times to repeat.")
print("While loops keep repeating until a condition becomes false.")
print("break stops the loop and continue skips the current iteration.")
print("range() helps generate numbers for loops.")
print("Loops are used in automation, data processing, and repeated tasks.")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. for i in range(3): print(i)")
print("2. while x < 3: print(x); x += 1")
print("3. for n in [1, 2, 3]: print(n)")
print("4. for i in range(1, 6): if i == 3: continue")
print("5. for i in range(1, 10): if i == 5: break")

for i in range(3):
    print("Example 1:", i)

x = 0
while x < 3:
    print("Example 2:", x)
    x += 1

for n in [1, 2, 3]:
    print("Example 3:", n)

for i in range(1, 6):
    if i == 3:
        continue
    print("Example 4:", i)

for i in range(1, 10):
    if i == 5:
        break
    print("Example 5:", i)

print("\nPractice makes it easier to understand loops in Python!")
