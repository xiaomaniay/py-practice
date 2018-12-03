def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    print(helper.__name__, func.__name__)
    helper.__name__ = func.__name__
    return helper


@call_counter
def f():
    pass


print(f.calls)
for _ in range(10):
    f()
print(f.calls)
