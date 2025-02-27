def add_extra_security(func):

    def wrapper():
        print("1. Before the function is called")
        print("2. Add helmet, glove, knee guard, License")
        func()
        print("3. After the function is called")
        print("4. Secure driving, Leave all items")

    return wrapper()

@add_extra_security
def drive_ola_scooter():
    print("ola")

@add_extra_security
def drive_scooty():
    print("Normal Function!!")
    print("I'm driving scooty")









