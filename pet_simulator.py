from abc import ABC, abstractmethod
import random


class Pet(ABC):
    def __init__(self, hunger=50, happiness=50, energy=50, name=str):
        self._hunger = hunger
        self._happiness = happiness
        self._energy = energy
        self.name = name

    @abstractmethod
    def special_ability(self):
        pass

    @property
    def min_hunger(self):
        return self.__min_hunger

    @min_hunger.setter
    def min_hunger(self, hunger):
        if hunger < 0:
            raise ValueError(f"hunger cannot be less than 0")
        self.__min_hunger = hunger

    @property
    def max_hunger(self):
        return self.__max_hunger

    @max_hunger.setter
    def max_hunger(self, hunger):
        if hunger > 100:
            raise ValueError(f"hunger cannot be greater than 100")
        self.__max_hunger = hunger

    @property
    def min_happiness(self):
        return self.__min_happiness

    @min_happiness.setter
    def min_happiness(self, happiness):
        if happiness < 0:
            raise ValueError(f"happiness cannot be less than 0")
        self.__min_happiness = happiness

    @property
    def max_happiness(self):
        return self.__max_happiness

    @max_happiness.setter
    def max_happiness(self, happiness):
        if happiness > 100:
            raise ValueError(f"happiness cannot be greater than 100")
        self.__max_happiness = happiness

    @property
    def min_energy(self):
        return self.__min_energy

    @min_energy.setter
    def min_energy(self, energy):
        if energy < 0:
            raise ValueError(f"energy cannot be less than 0")
        self.__min_energy = energy

    @property
    def max_energy(self):
        return self.__max_energy

    @max_energy.setter
    def max_energy(self, energy):
        if energy > 100:
            raise ValueError(f"energy cannot be greater than 100")
        self.__max_energy = energy

    def feed(self):
        self._hunger -= 20
        self._energy += 10

    def play(self):
        self._happiness += 15
        self._energy -= 10

    def sleep(self):
        self._energy += 20
        self._hunger += 10

    def show_status(self):
        print(f" 🐾{self.name}'s Status:")
        print(f"    Hunger: {self._hunger}/100")
        print(f"    Happiness: {self._happiness}/100")
        print(f"    Energy: {self._energy}/100")

    def random_event(self):
        num = random.randint(1, 10)
        if num == 1:
            print(
                f"Random Event: {self.name} found a snack! Hunger decreases!")
            self._hunger -= 10
        elif num == 2:
            print(
                f"Random Event: {self.name} had a bad dream... Energy decreases!")
            self._energy -= 10
        elif num == 3:
            print(
                f"Random Event: {self.name} found a toy! Happiness increases!")
            self._happiness += 10
        else:
            return None


class Dog(Pet):
    def play(self):
        self._happiness += 20
        self._energy -= 10

    def special_ability(self):
        if self._happiness >= 80:
            print(f"{self.name}'s Loyalty: Being happy reduces hunger")
            self._hunger -= 10
        else:
            print(
                f"{self.name}'s happiness is not high enough for this ability (must be >= 80)")


class Cat(Pet):
    def sleep(self):
        self._energy += 30
        self._hunger += 5

    def special_ability(self):
        if self._energy <= 20:
            print(f"{self.name}'s Meow: Super meow increases happiness")
            self._happiness += 15
        else:
            print(
                f"{self.name}'s energy is not low enough for this ability (must be <= 20)")


class Dragon(Pet):
    def feed(self):
        self._hunger -= 30
        self._energy += 15
        self._happiness += 10

    def play(self):
        self._happiness += 25
        self._hunger += 10
        self._energy -= 5

    def special_ability(self):
        if self._happiness >= 70:
            print(f"{self.name}'s Flight: Increases happiness and energy.")
            self._hunger -= 5
            self._energy += 5
        else:
            print(
                f"{self.name}'s happiness is not high enough for this ability (must be >= 70)")
