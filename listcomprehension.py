print(__file__)

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]  # list comprehension
squares_range = [number ** 2 for number in range(1,6)] # list comprehension
squares_1 = {number ** 2 for number in numbers} # set comprehension
squares_2 = (number ** 2 for number in numbers) # tuple does not work
print(squares)
print(squares_range)
print(squares_1)
print(squares_2)

print("*" * 40)
text = "This is real"
print(text)
words = [word.upper() for word in text.split(' ')]
words1 = [word.upper() for word in text.split('\n')]
lc_words = text.split(' ')
print(words)
print(lc_words)
print(words1)

print("*" * 50)
print("*" * 50)


burgers = ["Ham","Beef","Chicken"]
toppings=["Cheese","Eggs","Guac"]

# meals = [ (burgers,toppings) for burger in burgers for topping in toppings]
for meals in [ (burger,topping) for burger in burgers for topping in toppings]:
    print(meals)
print()
for burger in burgers:
    for topping in toppings:
        print((burger,topping))