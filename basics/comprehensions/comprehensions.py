# This loop builds a list by visiting each number in range(10)
# and appending its square to the list.
# Example: x = 0, 1, 2, ... 9
# Each step does: squares.append(x**2)
# So the result is: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# Map example: map() applies the same function to each value in the sequence.
# It does not create a list by itself, so we wrap it with list(...)
# to convert the result into a list of squares.
def square(x):
    return x**2

squares_map = list(map(square, range(10)))
print(squares_map)

# Explanation:
# - The for loop manually builds the list one item at a time.
# - map(square, range(10)) means: "take each number from 0 to 9 and pass it to square()".
# - list(...) turns the map object into a list so it prints nicely.
# - Both versions produce the same output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#list comprehension example: This is a more concise way to create the same list of squares.
squares_comprehension = [x**2 for x in range(10)];
print(squares_comprehension)


#simple example of list comprehension to extract vowels from a sentence with condition
sentence = "the rocket came back from mars"
vowels = [char for char in sentence if char in "aeiou"]
print(vowels)

#with complex filtering condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Extract even numbers greater than 5 using list comprehension
even_numbers_gt_5 = [num for num in numbers if num % 2 == 0 and num > 5];
print(even_numbers_gt_5)


complexSentence="the rocket came back from mars and it was a successful mission"
# Extract words longer than 3 characters using list comprehension
long_words=[word for word in complexSentence.split() if len(word) > 3]
print(long_words)

#with if-else condition
# Create a list of "even" or "odd" strings based on the numbers in the list
even_odd = ["even : " + str(num) if num % 2 == 0 else "odd : " + str(num) for num in numbers]
print(even_odd)

#Remove Duplicates With Set and Dictionary Comprehensions
exampleList = [1, 2, 3, 4, 5, 1, 2, 3]
# Using set comprehension to remove duplicates
unique_numbers_set = {num for num in exampleList}
print(unique_numbers_set)

# Using dictionary comprehension to remove duplicates and keep track of their first occurrence
unique_numbers_dict = {num: i for i, num in enumerate(exampleList)}
print(list(unique_numbers_dict.keys()))


#example of walrus operator in list comprehension
# The walrus operator (:=) allows assignment within an expression.

import random
def get_temperature():
    return random.randrange(50, 90)

print("Temperatures above 70 degrees:")
# Using the walrus operator to filter temperatures above 70
temperatures = [temp for _ in range(20) if (temp := get_temperature()) >= 70]
print(temperatures)
