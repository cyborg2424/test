import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        total = end - start
        print("The time is", total)
    return wrapper()


@calculate_time
def total_time():
    time.sleep(5)


total_time()