import random

class Enemy(object):

    #class Enemy(object) This is same as above. Every class in Python extends the object class

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True


    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives>0:
                print("{0._name} lost a life".format(self))
                self._hit_points = 3
            else:
                self._alive = False
                print("{0._name} is dead".format(self))

    def __str__(self):
        return "Name:{0._name}, Lives:{0._lives}, Hit Points:{0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self,name):

        super().__init__(name = name, lives = 1, hit_points = 23)
        #super(Troll,self).__init__(name = name, lives = 1, hit_points = 23)
        #Enemy.__init__(self,name = name, lives = 1, hit_points = 23)

    def grunt(self):
        print("{0._name} stomped you".format(self))


class Vampyre(Enemy):

    def __init__(self,name):
        super().__init__(name = name, lives  = 3, hit_points = 5)

    def dodges(self):

         if random.randint(1,5) == 2:
             print("**** {0._name} dodges ****".format(self))
             return True
         else:
             return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)



class VampyreKing(Vampyre):

    def __init__(self,name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
