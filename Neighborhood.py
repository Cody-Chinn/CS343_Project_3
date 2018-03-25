from Home import Home
from Player import Player
from Observer import Observer

"""
Create the Neighborhood, which is made into a rectangle of rows and columns
using the Home class
"""
class Neighborhood(Observer):
    """
    Creat the constructor for the neighborhood class
    """
    def __init__(self):
        self.row = 0
        self.cols = 0
        self.num_monsters = 0
        self.neighborhood = []

    """
    Set up the neighborhood in rows and columns
    """
    def make_neighborhood(self, rows, cols):
        self.rows = rows
        self.cols = cols

        for row in range(0, self.rows):
            self.neighborhood.append([])
            for col in range(0,self.cols):
                home = Home()
                home.add_observer(self)
                self.neighborhood[row].append(home)

    """
    Create the getters for the instance variables
    """
    def get_num_monsters(self):
        return self.num_monsters

    def get_home(self, row, col):
        return self.neighborhood[row][col]

    """
    Override the update method from the Observer class
    """
    def update(self):
        self.num_monsters = 0
        for row in range(0, self.rows):
            for cols in range(0, self.cols):
                self.num_monsters = self.num_monsters + self.neighborhood[row][col].get_monster_count
