from Animals.animals.animal import Bird
from Animals.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable) or isinstance(food, Fruit) or isinstance(food, Seed):
            self.weight += food.quantity * 0.35
            self.food_eaten += food.quantity
            return
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
