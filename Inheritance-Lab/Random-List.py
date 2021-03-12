from random import *


class RandomList(list):

    def get_random_element(self):
        removed = random.choice(self)
        self.remove(removed)
        return removed
