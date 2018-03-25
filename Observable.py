"""
The Observable class is provided by professor Ira Woodring and is used to make
objects in the program communicate with other objects
"""
class Observable(object):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []

    def update(self):
        for observer in self.observers:
            observer.update()
