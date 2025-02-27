def add_before_ui_after_ui(func):
    def wrapper():
        print("before starting the UI")
        print("Start the browser")
        func()
        print("Ending the running UI Tc")
        print("Quit the browser")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print(">> I will test UI")
