from datetime import datetime

def deco_foo(func):
    def wrap():
        time_start = datetime.now()
        func()
        time_stop = datetime.now()
        return f'Время выполнения составило {time_stop - time_start}'
    return wrap


@deco_foo
def test_func_2():
    return [i ** 1500 for i in range(1, 950)]


print(test_func_2())


@deco_foo
def test_func_2():
    return [i ** 1500 for i in range(1, 950)]

print(test_func_2())