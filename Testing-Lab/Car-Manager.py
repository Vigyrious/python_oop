class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


import unittest

class CarTest(unittest.TestCase):
    def test_constructor(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(make,car.make)
        self.assertEqual(model, car.model)
        self.assertEqual(fuel_consumption, car.fuel_consumption)
        self.assertEqual(fuel_capacity, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_method(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual("make",car.make)

    def test_make_method_with_empty_arg(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.make = None
        self.assertIsNotNone(error.exception)

    def test_make_method_with_correctData(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        new_make = "new_make"
        car.make = new_make
        self.assertEqual(new_make,car.make)

    def test_model_method(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(model,car.model)

    def test_model_with_empty_arg(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.model = None
        self.assertIsNotNone(error.exception)

    def test_model_with_correctData(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        new_model = "new_model"
        car.model = new_model
        self.assertEqual(new_model,car.model)

    def test_fuel_consumption_get_method(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(5,car.fuel_consumption)

    def test_fuel_consumption_with_less_than0(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.fuel_consumption = 0
        self.assertIsNotNone(error.exception)

    def test_fuel_consumption_with_correctData(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.fuel_consumption = 12
        self.assertEqual(12,car.fuel_consumption)

    def test_fuel_capacity_get_method(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(6,car.fuel_capacity)

    def test_fuel_capacity_with_less_than0(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.fuel_capacity = 0
        self.assertIsNotNone(error.exception)

    def test_fuel_capacity_with_correctData(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.fuel_capacity = 12
        self.assertEqual(12,car.fuel_capacity)

    def test_fuel_amount_get_method(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(0,car.fuel_amount)

    def test_fuel_amount_setter_with_incorrect_data(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.fuel_amount = -2
        self.assertIsNotNone(error.exception)

    def test_fuel_amount_with_correctData(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.fuel_amount = 12
        self.assertEqual(12,car.fuel_amount)

    def test_refuel_with_negative_data(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.refuel(-5)
        self.assertIsNotNone(error.exception)

    def test_refuel_with_less_than_fuel_capacity_data(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.refuel(5)
        self.assertEqual(5,car.fuel_amount)

    def test_refuel_with_greater_than_fuel_capacity_data(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.refuel(7)
        self.assertEqual(6,car.fuel_capacity)

    def test_drive_with_longer_distance_than_possible(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 2, 1
        car = Car(make, model, fuel_consumption, fuel_capacity)
        with self.assertRaises(Exception) as error:
            car.drive(100)
        self.assertIsNotNone(error.exception)

    def test_drive_with_correct_distance(self):
        make, model, fuel_consumption, fuel_capacity = "make", "supra", 5, 6
        car = Car(make, model, fuel_consumption, fuel_capacity)
        car.fuel_amount = 6
        car.drive(100)
        self.assertEqual(1,car.fuel_amount)
if __name__ == '__main__':
    unittest.main()