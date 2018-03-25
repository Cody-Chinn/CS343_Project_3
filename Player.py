from Weapon import *
from random import *
from Observer import Observer

"""
The player class is used as the playable character. The player will start out
with between 100 and 125 health and will have an attack ranging from 10-20 as
a base attack. The Weapon class will provide multipliers to the base attack in
game and the weapon list will be a set of 10 randomly generated weapons.
"""
class Player(Observer):

    def __init__(self):

        self.HP = randint(100, 125)
        self.attack = randint(10, 20)
        self.Weapon_list = []
        self.place = [0, 0]
        self.weapon_index = 0
        self.randomize_weapons()
        self.current_weapon = self.Weapon_list[0]

    """
    This function randomizes the list of 10 weapons that the player uses in game
    """
    def randomize_weapons(self):
        for i in range(0, 9):
            x = randint(0,3)

            if x == 0:
                # Gives the player Hersheys Kisses in the given weapon slot
                self.Weapon_list.insert(i, HersheyKisses())
                self.Weapon_list[i].add_observer(self)

            if x == 1:
                # Gives the player Sour Straws in the given weapon slot
                self.Weapon_list.insert(i, SourStraws())
                self.Weapon_list[i].add_observer(self)

            if x == 2:
                # Gives the player Chocolate Bars in the given weapon slot
                self.Weapon_list.insert(i, ChocolateBars())
                self.Weapon_list[i].add_observer(self)

            if x == 3:
                # Gives the player Nerd Bombs in the given weapon slot
                self.Weapon_list.insert(i, NerdBombs())
                self.Weapon_list[i].add_observer(self)

    """
    Create the observer for the player
    """
    def create_observer(self, observer):
        self.add_observer(observer)

    """
    Create all of the getters for the insance variables
    """
    def get_HP(self):
        return self.HP

    def get_attack(self):
        return self.attack

    def get_place(self):
        return self.place

    def get_weapon_list(self):
        return self.Weapon_list

    def get_current_weapon(self):
        return current_weapon

    """
    Create the setters for the instance variables
    """
    def set_HP(self, HP):
        self.HP = HP

    def set_place(self, row, col):
        self.place = [row, col]

    def set_current_weapon(self, i):
        self.current_weapon = self.Weapon_list[i]

    def use_weapon(self):
        self.current_weapon.use_weapon()

    """
    Update the weapon list if uses goes under 0
    """
    def update(self):
        x = randInt(0, 3)
        if x == 1:
            self.Weapon_list[self.weapon_index] = HersheyKisses()
        if x == 2:
            self.Weapon_list[self.weapon_index] = SourStraws()
        if x == 3:
            self.Weapon_list[self.weapon_index] = ChocolateBars()
        if x == 4:
            self.Weapon_list[self.weapon_index] = NerdBombs()

        self.set_current_weapon(self.current_weapon)
