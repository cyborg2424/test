def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper


@doubler
def test_doubler():
    print("doubler")


test_doubler()