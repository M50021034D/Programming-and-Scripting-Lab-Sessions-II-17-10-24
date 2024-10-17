#creating strings
name1 = 'Shelton'
name2 = "Python is awesome!"
multi_line_string = """This is a multiline string."""

print(name1)
print(name2)
print(multi_line_string)

my_string = "Hello World"

# Indexing examples
first_char = my_string[0]   # 'H'
last_char = my_string[-1]   # 'd2'

# Slicing examples
hello = my_string[0:5]  # 'Hello'
world = my_string[6:]   # 'World'

print(first_char)
print(last_char)
print(hello)
print(world)

# Concatenation
greeting = "Hello " + "Shelton"
print(greeting)

# Repetition
repeated_greeting = "Hello! " * 3
print(repeated_greeting)

# String length
length = len(my_string)
print(f"The length of '{my_string}' is {length}")

sample_string = "     Python Programming      "

# Convert to lowercase
lower_case_string = sample_string.lower()
print(lower_case_string)

# Convert to uppercase
upper_case_string = sample_string.upper()
print(upper_case_string)

# Remove whitespaces from start and end
stripped_string = sample_string.strip()
print(stripped_string)

# String formatting
name = "Mark"
age = 22
# Using format method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# Using f-strings (Python 3.6+ Only)
f_string = f"My name is {name} and I am {age} years old."
print(f_string)

