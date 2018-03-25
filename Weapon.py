from random import *
from Observable import Observable
from Observer import Observer
from abc import ABCMeta


"""
The weapon class is an abstract class used for all of the weapons in the
game. The weapons have a variable number of uses and multipliers
"""
class Weapon(Observable):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.uses = 0
        self.multiplier = 0
        self.type = ""

    """
    This function attackes the monsters import Observer, Player, Homin the house. If the number of uses
    for the given weapon falls below 0 then nothing happens
    """
    def use_weapon(self):
        if self.uses >= 1:
            #attack the enemycreate_observer
            self.uses = self.uses - 1

            if self.uses <= 0:
                self.update()


    """
    Define all of the getters for the weapon class
    """
    def get_uses(self):
        if self.uses <= 0:
            self.update

        return self.uses

    def get_type(self):
        return self.type

    def get_mult(self):
        return self.multiplier

    """
    Create the observer for the weapon
    """
    def create_observer(self, obs):
        self.add_observer(obs)

"""
The Hersheys Kiss class is a weapon with a multiplier of 1 and unlimited uses
"""
class HersheyKisses(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.type = "HersheyKisses"
        self.uses = 999999
        self.multiplier = 1

"""
The Sour Straws class is a weapon with a multiplier between 1 and 1.75 and can
only be used twice.
"""
class SourStraws(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.type = "SourStraws"
        self.uses = 2
        self.multiplier = uniform(1, 1.75)


"""
The Chocolate Bar class is a weapon with a multiplier between 2 and 2.4 and can
be used 4 times
"""
class ChocolateBars(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.type = "ChocolateBars"
        self.uses = 4
        self.multiplier = uniform(2, 2.4)


"""
Ther nerd bombs class is the danks with a multiplier between 3.5 and 5. It can
only be used once.
"""
class NerdBombs(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.type = "NerdBombs"
        self.uses = 1
        self.multiplier = uniform(3.5, 5)
