from abc import ABCMeta, abstractmethod
from random import *
from Player import Player
from Observable import Observable
from Observer import Observer


"""
This NPC parent class is a generic class to be used as a parent class to the
non playable character classes (Person, Zombie, Vampire, Ghoul, Werewolf)

@param HP_low - the lowest value of health that the NPC can have
@param HP_high - the highest value of health that the NPC can have
@param attack_low - the lowest value of attack that the NPC can have
@param attack_high - the highest value of attack that the NPC can have
"""
class NPC(Observable):

    __metaclass__ = ABCMeta



    def __init__(self, HP_low, HP_high, attack_low, attack_high):
        self.HP_low = HP_low # Lowest possible health for the NPC
        self.HP_high = HP_high # Highest possible health for the NPC
        self.attack_low = attack_low # Lowest possible attack for the NPC
        self.attack_high = attack_high  # Highest possible attack for the NPC
        self.HP = 0 # All NPC's initiated with 0 health
        self.attack = 0 # All NPC's initiated with 0 attack
        self.weapon_effect = {"HersheyKisses" : 0, #This list is for the
                                "SourStraws" : 0,  #effectiveness of the
                                "ChocolateBars" : 0, # of each specific weapon
                                "NerdBombs" : 0 } # on each monster

    """
    This function finds the HP for the given NPC. It uses the lowest health
    variable and the highest health variable as maximums and minimums and then
    find a random whole number between the two variables
    """
    def HP_calc(self, HP_low, HP_high):
        self.HP = randint(HP_low, HP_high)

    """
    This function calculates the attack for the given NPC using the lowest
    """
    def attack_calc(self, attack_low, attack_high):
        self.attack = randint(attack_low, attack_high)

    """
    Attack function to be used when the NPC's hit the Player
    """
    def attack(self, Player):
        Player.HP = Player.HP-self.attack

    """
    Create the observer for the NPC
    """
    def create_observer(self, observer):
        self.add_observer(observer)

    """
    Create all getters for the instance variables
    """
    def get_HP(self):
        return self.HP

    def get_attack(self):
        return self.attack

    def get_weapon_effect_list(self):
        return self.weapon_effect

    def get_weapon_effect(self, type):
        return self.weapon_effect.get(name)

    """
    Setters for health and attack of the NPC
    """
    def set_HP(self, HP):
        self.HP = HP
        if HP <= 0:
            self.update()

    def set_attack(self, attack):
        self.attack = attack

    """
    Using the abstract method idea from Jeff Knupp, URL is
    https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

    Return a string to define the monster type
    """
    @abstractmethod
    def monster_type(self):
        pass


"""
The Person class is an NPC that gives the player back one health for each 'hit'.
It is always initiated with 100 health
"""
class Person(NPC):
    def __init__(self):
        super().__init__(100, 100, -1, -1)
        self.HP = 100
        self.attack = -1
        self.weapon_effect = {"HersheyKisses" : 0,
                                "SourStraws" : 0,
                                "ChocolateBars" : 0,
                                "NerdBombs" : 0 }

    def monster_type(self):
        return 'Person'

"""
The Zombie class is a monster that is initiated with variable attack and health
The lowest health the Zombie can start with between 50 and 100 health and has
an attack ranging from 0 to 10
"""
class Zombie(NPC):
    def __init__(self):
        super().__init__(50, 100, 0, 10)
        self.HP_calc(50, 100)
        self.attack_calc(0, 10)
        self.weapon_effect = {"HersheyKisses" : 1,
                                "SourStraws" : 2,
                                "ChocolateBars" : 1,
                                "NerdBombs" : 1 }

    def monster_type(self):
        return 'Zombie'


"""
The Vampire class is a monster that is initiated with variable attack and health
The lowest health the Vampire can start with between 100 and 200 health and has
an attack ranging from 10 to 20
"""
class Vampire(NPC):
    def __init__(self):
        super().__init__(100, 200, 10, 20)
        self.HP_calc(100, 200)
        self.attack_calc(10, 20)
        self.weapon_effect = {"HersheyKisses" : 1,
                                "SourStraws" : 1,
                                "ChocolateBars" : 0,
                                "NerdBombs" : 1 }

    def monster_type(self):
        return 'Vampire'

"""
The Ghoul class is a monster that is initiated with variable attack and health
The lowest health the Ghoul can start with between 40 and 80 health and has
an attack ranging from 15 to 30
"""
class Ghoul(NPC):
    def __init__(self):
        super().__init__(40, 80, 15, 30)
        self.HP_calc(40, 80)
        self.attack_calc(15, 30)
        self.weapon_effect = {"HersheyKisses" : 1,
                                "SourStraws" : 1,
                                "ChocolateBars" : 1,
                                "NerdBombs" : 5 }

    def monster_type(self):
        return 'Ghoul'

"""
The Werewolf class is a monster that is initiated with variable attack and
constant health. The health is always 200 to start for a werewolf and the attack
ranges from 0 to 40
"""
class Werewolf(NPC):
    def __init__(self):
        super().__init__(200, 200, 0, 40)
        self.HP = 200
        self.attack_calc(0, 40)
        self.weapon_effect = {"HersheyKisses" : 1,
                                "SourStraws" : 0,
                                "ChocolateBars" : 0,
                                "NerdBombs" : 1 }

    def monster_type(self):
        return 'Werewolf'
