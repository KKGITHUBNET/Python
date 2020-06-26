import os


a = 2
b =3
print("a = {}, b= {}".format(a, b))

a, b = b, a
print("a = {}, b= {}".format(a, b))

def fib(): # This is generator code
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous , current

fib = fib()

for i in range(20):
    print(next(fib), end = ' ')
print("*" * 50)

root="music"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    print(directories)
    print(files)
    #input()
    # for f in files:
    #     print("\t{}".format(f))

entries = [1, 2, 3, 4]
print("all : {}".format(all(entries)))
print("any : {}".format(any(entries)))

entries1 = [0, 1, 2, 3, 4]
print("all : {}".format(all(entries1)))
print("any : {}".format(any(entries1)))