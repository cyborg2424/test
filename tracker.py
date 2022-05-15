def func_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper

@func_counter
def test():
    print("tracker")

for i in range(0,5):
    test()

Count = test.counter
print(Count)