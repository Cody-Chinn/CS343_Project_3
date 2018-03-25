from abc import ABCMeta, abstractmethod
"""
The Observer class is provided by professor Ira Woodring and is used to make
objects in the program communicate with other observable objects
"""
class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass
