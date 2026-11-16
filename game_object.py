# This class establish the fundemantal rules for all of the the class that I will create. Meaning this will be the parent class of every other class I created.
# The rules are: Every class must know how to update and draw themselve.

from abc import ABC, abstractmethod

class GameObject(ABC):
    
    @abstractmethod
    def update(self, keys):
        pass

    @abstractmethod
    def draw(self, screen):
        pass