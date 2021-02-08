    def time_call_any(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            start = time()
            res = func(*args, **kwargs)
            end = time()
            print("res", func, " = ", res)
            time_taken = end - start
            print(f"time taken: {time_taken:.13f}")
            return res

        # wrapper.__wrapped__ = func
        # wrapper.__name__ = func.__name__
        return wrapper


    @time_call_any
    def add(a, b):
        return a + b

    add(17576547654654665, 1757654765465466517576547654654665)

    @time_call_any
    def hello_again(name="World"):
        return "Hello " + name

    print("d", hello_again())
    print("d", hello_again("John"))
    print("d", hello_again(name="Sam"))

