import ducks

if __name__ == '__main__':
    #donald = ducks.Duck()
    #donald.fly()
    # test_duck(donald)
    # print("*"*5)
    # pug = Penguin()
    # test_duck(pug)
    flock = ducks.Flock()

    donald = ducks.Duck()
    daisy = ducks.Duck()
    casey = ducks.Duck()
    jaisy = ducks.Duck()
    paisy = ducks.Duck()

    peng = ducks.Penguin()
    mal = ducks.Mallard()



    flock.add_duck(donald)
    flock.add_duck(daisy)
    flock.add_duck(casey)
    flock.add_duck(jaisy)
    flock.add_duck(paisy)

    flock.add_duck(mal)
    flock.add_duck(peng)






    flock.migrate()

