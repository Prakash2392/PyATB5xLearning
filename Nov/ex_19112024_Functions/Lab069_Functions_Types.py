# 1. `The can't return -> non return`
# 2. They can return something
# 3. They have parameters
# 4. `They don't parameters / arguments`

# 1. `The can't return -> non return`
# No return and no parameter / No argument
def say_hello():
    print("Hello")


say_hello()


# 2. No return type and with argument
def greet(name):
    print("Hello", name)


greet("Prakash")


# 3. No return type and with default argument (# Positional argument)

def say_hello_argument(name="Prakash"):
    print("Hello", name.upper())


say_hello_argument("raj")
say_hello_argument()


def multiple_args(name1="A", name2="B"):
    print("Mul->", name1, name2)


multiple_args("Raj")
multiple_args("Prakash", "Raj")


# 4 Argument + Return type

def sum_of_two_no(a, b):
    return a + b


res = sum_of_two_no(3, 2)
print(res)


def sum_of_two(a=100, b=200):
    return a + b


res = sum_of_two(5, 5)
print(res)
res = sum_of_two()
print(res)
