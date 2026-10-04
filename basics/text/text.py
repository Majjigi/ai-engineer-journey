"""
Text in Python (Strings)
This script explains strings with easy chunks and examples.
"""



def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1. Strings are text
# ------------------------------------------------------------
print_section("Chunk 1: Strings are text")

name = "Alice"
message = 'Hello, Python!'
city = "Hyderabad"

print("name =", name, "type:", type(name))
print("message =", message, "type:", type(message))
print("city =", city, "type:", type(city))

# Strings can be created using single quotes or double quotes.
print("Single quotes example:", 'Hi there')
print("Double quotes example:", "Hi there")


# ------------------------------------------------------------
# 2. Concatenation
# ------------------------------------------------------------
print_section("Chunk 2: Joining strings")

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print("first_name =", first_name)
print("last_name =", last_name)
print("full_name =", full_name)

print("Hello " + "World")
print("Python " + "is " + "fun")


# ------------------------------------------------------------
# 3. Repetition
# ------------------------------------------------------------
print_section("Chunk 3: Repeating strings")

print("ha" * 3)
print("Python" * 2)
print("=" * 10);


# ------------------------------------------------------------
# 4. Length of a string
# ------------------------------------------------------------
print_section("Chunk 4: Finding string length")

text = "Welcome"
print("text =", text)
print("Length of text:", len(text))
print("Length of 'Python':", len("Python"))


# ------------------------------------------------------------
# 5. Indexing and slicing
# ------------------------------------------------------------
print_section("Chunk 5: Accessing characters")

word = "Python"
print("word =", word)
print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])
print("First 3 letters:", word[0:3])
print("From index 2 to end:", word[2:])
print("Every second character:", word[::2])
print("Every third character:", word[::3])




# ------------------------------------------------------------
# 6. Common string methods
# ------------------------------------------------------------
print_section("Chunk 6: Useful string methods")

sentence = "  python programming is easy  "
print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Strip spaces:", sentence.strip()) # Removes leading and trailing spaces
print("Replace:", sentence.replace("python", "Java"))
print("Split:", sentence.strip().split())
print("Starts with 'p'?:", sentence.strip().startswith("p"))
print("Ends with 'y'?:", sentence.strip().endswith("y"))


# ------------------------------------------------------------
# 7. String formatting
# ------------------------------------------------------------
print_section("Chunk 7: Formatting strings")

name = "Sara"
age = 22

print("My name is", name, "and I am", age, "years old")
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")


# ------------------------------------------------------------
# 8. Checking content
# ------------------------------------------------------------
print_section("Chunk 8: Checking text content")

email = "hello@example.com"
print("Contains '@':", '@' in email)
print("Contains 'gmail':", 'gmail' in email)
print("Is alpha?:", "Hello".isalpha())
print("Is digit?:", "123".isdigit())


# ------------------------------------------------------------
# 9. Escape characters
# ------------------------------------------------------------
print_section("Chunk 9: Special characters")

print("Hello\nWorld")
print("This is a tab\tspace")
print("He said: \"Python is great!\"")
print("Backslash: \\ ")


# ------------------------------------------------------------
# 10. A practical example
# ------------------------------------------------------------
print_section("Chunk 10: Real-world text example")

message = "Welcome to Python!"
print("Message:", message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Length:", len(message))
print("First 7 letters:", message[:7])
print("Last 6 letters:", message[-6:])


# ------------------------------------------------------------
# 11. Summary
# ------------------------------------------------------------
print_section("Chunk 11: Summary")

print("Strings are text values in Python")
print("We can join, repeat, slice, format, and check strings")
print("Common methods: upper(), lower(), strip(), replace(), split()")
print("Strings are very useful for user input, messages, and data")


# ------------------------------------------------------------
# Practice examples
# ------------------------------------------------------------
print_section("Try These Examples")

print("1. print('Hello')")
print("2. print('Python' * 3)")
print("3. print('Hello World'[0])")
print("4. print('python'.upper())")
print("5. print('  hello  '.strip())")
print("6. print('A,B,C'.split(','))")
print("7. print(len('Programming'))")
print("8. print('hello' in 'hello world')")

# Real practice code examples
print("Example 1:", "Hello")
print("Example 2:", "Python" * 3)
print("Example 3:", "Hello World"[0])
print("Example 4:", "python".upper())
print("Example 5:", "  hello  ".strip())
print("Example 6:", "A,B,C".split(','))
print("Example 7:", len("Programming"))
print("Example 8:", "hello" in "hello world")

print("\nPractice makes it easier to understand text in Python!")
