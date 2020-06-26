import sys


def my_range(n: int):
    start=0
    while start<n:
        yield start
        start += 1

big_range = my_range(5)
# big_range = range(5)

print("Big Range is {} bytes".format(sys.getsizeof(big_range)))

# creating a list containing all the values in big_range
big_list=[]

for val in big_range:
    big_list.append(val)

print("Big List is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)