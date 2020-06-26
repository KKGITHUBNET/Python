# from __future__ import print_function
# from __future__ import division     '''These two imports from __future__ are for python2 to support python3 modules'''

# print("Hello","World")
# print("Hello","World","!")


def average(*args):
    print(type(args))
    print("args is {}".format(args))
    print("*args is:", *args)  # *args is unpacking of tuple
    print(args[0])
    print(type(args[0]))
    mean = 0
    for arg in args:
        mean += arg
    return mean/len(args)


def build_tuple(*args) -> tuple:
    return args


# def print_backwards(*args,file = None):
def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


if __name__ == '__main__':
    print(average(2, 3, 4, 6))
    tuple_t1 = build_tuple("A", "B", "C")
    tuple_t2 = build_tuple("A", "B", "C")
    print(type(tuple_t1))
    print(tuple_t1)
    print(type(tuple_t2))
    print(tuple_t2)

    with open("kwargs.txt",'w') as kw:
        print_backwards("Hello", "Planet", "Earth", file=kw)
