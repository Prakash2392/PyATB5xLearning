import time


def time_dec(func):
    def wraper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("total time taken by func -->", end_time - start_time)

    return wraper()


def print_logs(func):
    def wrapper():
        print("starting log")
        func()
        print("Ending log")

    return wrapper()


@time_dec
@print_logs
def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2)


@time_dec
@print_logs
def test_ui_2():
    print("Add a function, time taken by this function")
    time.sleep(5)
