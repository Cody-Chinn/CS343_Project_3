from NPC import *
from random import *
from Observable import Observable
from Observer import Observer


"""
The home class is pretty neat. You can tell it's a home because of the way it
is. It also contains anywhere from 0 to 10 monsters that it observes and updates
when attacks happen within it
"""
class Home(Observer, Observable):

    """
    Creat the constructor for the home class
    """
    def __init__(self):

        self.monster_count = randint(0, 10)
        self.monster_types = []
        self.count_people = 0

        'Put the monsters in the house'
        while len(self.monster_types) < self.monster_count:

            add_monster = randint(0,3)

            if add_monster == 0:
                z = Zombie()
                z.create_observer(self)
                self.monster_types.append(z)

            if add_monster == 1:
                v = Vampire()
                v.create_observer(self)
                self.monster_types.append(v)

            if add_monster == 2:
                g = Ghoul()
                g.create_observer(self)
                self.monster_types.append(g)

            if add_monster == 3:
                w = Werewolf()
                w.create_observer(self)
                self.monster_types.append(w)


    """
    Getters for all of the instance variables
    """
    def get_monster_count(self):
        return self.monster_count

    def get_monster_types(self):
        return self.monster_types

    def get_count_people(self):
        return self.count_people

    """
    This function uses the monsters in the house to attack the player
    """
    def attack_player(self):
        attack = 0
        for monster in self.monster_count:
            attack = attack + monster.get_attack

        return attack

    """
    This function uses the player to attack the monsters in the house
    """
    def attack_monsters(self, Weapon, attack):
        for monsters in range(0, self.monster_count):
            attack = int(self.monster_types[monsters].get_weapon_effect(Weapon.get_type))
            attack = attack * Weapon.get_mult()
            monster_HP = self.monster_count[monsters].get_HP() - (attack * attack)
            self.monster_count[monsters].set_HP(monster_HP)

            Weapon.use_weapon()
