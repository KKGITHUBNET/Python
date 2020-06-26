class Wing(object):

    def __init__(self,ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard , but I am flying")
        else:
            print("I think I'll just walk")

class Duck(object):

    def __init__(self):
        self._wing = Wing(1.2)

    def walk(self):
        print("Waddle Woddle")

    def swim(self):
        print("Water is lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):

    def walk(self):
        print("I Waddle woddle too")

    def swim(self):
        print("yayyy")

    def quack(self):
        print("hahahah!!!!")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck,'fly',None)

        #if type(duck) is Duck:
        #if isinstance(duck, Duck):

        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError   # TODO Remove this before release
            #raise TypeError ("Can not add duck,are you sure it is not a " + str(type(duck).__name__))
            print("Can not add a {} to a duck flock".format(str(type(duck).__name__)))


    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One Down")
                problem = e
        if problem:
            raise problem



def test_duck(duck):
    duck.quack()
    duck.swim()
    duck.walk()


