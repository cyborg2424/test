import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        total_time = end - start
        print(f'Total time {total_time}')
        return func
    return wrapper

@calculate_time
def test_time():
    time.sleep(5)

test_time()