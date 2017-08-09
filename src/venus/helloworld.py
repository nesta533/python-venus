from memory_profiler import profile


def hello(*args):
    print(args)


hello(1, 2, 4, 5, 'nihao')


def helloWorld(**args):
    print(args)


helloWorld(a=1, b=2)


class Foobar(object):
    def __init__(self, x):
        self.x = x

    def hellp(self):
        print(self.x)


def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    bar = Foobar(x=12)
    bar.hellp()
    print(bar.__dict__)
    return a


if __name__ == '__main__':
    my_func() 
