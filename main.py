from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

vking = VampyreKing("Vking")
print(vking)
vking.take_damage(12)
print(vking)

# # random_monster =  Enemy("Basic Enemy",12,1)
# # print(random_monster)
# #
# # random_monster.take_damage(8)
# # print(random_monster)
# #
# '''
# pug = Troll("Pug")
# print("pug - {} ".format(pug))
#
# another_troll = Troll("Ug")
# another_troll.take_damage(18)
# print("Ug - {} ".format(another_troll))
#
# bro = Troll("Urg")  #brother = Enemy("Urg",23) -< This statment will also give the same result
# print("bro - {} ".format(bro), end = " ")
# print(bro)
#
# pug.grunt() '''
# #
# vamp = Vampyre("Vlad")
# # #print(vamp)
# # #vamp.take_damage(3)
# #
# #
# while vamp._alive:
#     if not vamp.dodges():
#         vamp.take_damage(1)
#     print(vamp)
#
# print("-" *  20)

