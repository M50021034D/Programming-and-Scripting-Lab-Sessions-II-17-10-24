
def greet():
    print("Hi, welcome to functions tutorial")

greet()

def greet(name):
    print(f"Hello, {name}")

greet("Mark")

def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(67, 34)
print("Sum: ", sum_result)

square = lambda x: x * x

print("Square of 79:", square(79))

add = "+"
subtract = "-"
multiply = "*"
divide = "/"




calculate = lambda x, y, z: x (add, subtract, multiply, divide) 

print(calculate(10, add, 87))
