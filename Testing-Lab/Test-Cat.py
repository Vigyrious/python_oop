class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False



import unittest


class CatTests(unittest.TestCase):

    def test_catEat_shouldIncreaseSizeBy1(self):
        name = 'Tom'
        cat = Cat(name)

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_catEat_shouldSetFedToTrue(self):
        name = 'Tom'
        cat = Cat(name)

        cat.eat()
        self.assertTrue(cat.fed)

    def test_catEat_whenFed_shouldRaiseException(self):
        name = 'Tom'
        cat = Cat(name)
        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)

    def test_catSleep_whenNotFed_shouldRaiseException(self):
        name = 'Tom'
        cat = Cat(name)

        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_catSleep_shouldSetSleepyToFalse(self):
        name = 'Tom'
        cat = Cat(name)

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()
