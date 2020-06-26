import timeit

def trial():
    #print(__file__)
    numbers = [1, 2, 3, 4, 5]
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    #print(squares)


print(timeit.timeit(trial,number=100000))