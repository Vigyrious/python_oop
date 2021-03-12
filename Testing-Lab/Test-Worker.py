

class Worker:

  def __init__(self, name, salary, energy):
    self.name = name
    self.salary = salary
    self.energy = energy
    self.money = 0

  def work(self):
    if self.energy <= 0:
        raise Exception('Not enough energy.')

    self.money += self.salary
    self.energy -= 1

  def rest(self):
    self.energy += 1

  def get_info(self):
    return (f'{self.name} has saved {self.money} money.')



import unittest


class WorkerTests(unittest.TestCase):
    def test_correct_name_salary_and_energy(self):
        name = "Valio"
        salary = 3000
        energy = 110
        p = Worker(name, salary, energy)
        self.assertEqual(name,p.name)
        self.assertEqual(salary,p.salary)
        self.assertEqual(energy,p.energy)

    def test_is_rest_working(self):
        name = "Valio"
        salary = 3000
        energy = 110
        p = Worker(name, salary, energy)
        p.rest()
        self.assertEqual(energy+1,p.energy)

    def test_error_raised_when_no_energy(self):
        name = "Valio"
        salary = 3000
        energy = 0
        p = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            p.work()
        self.assertEqual('Not enough energy.', context.exception.args[0])
        # try:
        #     p.work()
        # except Exception as e:
        #     self.assertIsNotNone(e)

    def test_money_increase_after_work(self):
        name = "Valio"
        salary = 150
        energy = 100
        p = Worker(name, salary, energy)
        p.work()
        self.assertEqual(salary, p.money)

    def test_if_energy_decreases_after_working(self):
        name = "Valio"
        salary = 150
        energy = 100
        p = Worker(name, salary, energy)
        p.work()
        self.assertEqual(energy-1,p.energy)

    def test_if_get_info_is_working_properly(self):
        name = "Valio"
        salary = 150
        energy = 100
        p = Worker(name, salary, energy)
        self.assertEqual(f'{name} has saved 0 money.',p.get_info())

if __name__ == '__main__':
    unittest.main()