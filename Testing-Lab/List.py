class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)



import unittest
class TestIntegerList(unittest.TestCase):
    def test_if_constructor_is_working_when_not_only_ints(self):
        ints = IntegerList(1,2,3,"a")
        self.assertEqual([1,2,3], ints.get_data())

    def test_if_constructor_stores_correctly_when_only_ints_are_passed(self):
        ints = IntegerList(1,2,3,4)
        self.assertEqual([1,2,3,4], ints.get_data())

    def test_if_add_method_is_working_when_adding_int(self):
        ints = IntegerList(1)
        ints.add(2)
        self.assertListEqual([1,2],ints.get_data())

    def test_if_add_method_raises_exception_when_passed_non_int(self):
        ints = IntegerList(1)
        with self.assertRaises(ValueError) as error:
            ints.add("a")
        self.assertIsNotNone(error.exception)

    def test_if_remove_method_works_with_right_arguments(self):
        ints = IntegerList(1,2,3,4)
        removed = ints.remove_index(2)
        self.assertEqual(3,removed)
        self.assertListEqual([1,2,4],ints.get_data())

    def test_if_remove_method_raises_exception_when_needed(self):
        ints = IntegerList(1,2,3,4)
        with self.assertRaises(IndexError) as error:
            ints.remove_index(9)
        self.assertIsNotNone(error.exception)

    def test_get_method_working_with_correct_data(self):
        ints = IntegerList(1,2,3,4)
        self.assertEqual(4,ints.get(3))

    def test_get_method_raise_exception(self):
        ints = IntegerList(1,2,3)
        with self.assertRaises(IndexError) as error:
            ints.get(4)
        self.assertIsNotNone(error.exception)

    def test_insert_method_works_with_proper_data(self):
        ints = IntegerList(1,2)
        ints.insert(1,3)
        self.assertEqual([1,3,2],ints.get_data())

    def test_if_insert_method_raises_value_error_when_passed_not_int(self):
        ints = IntegerList(1,2,3)
        with self.assertRaises(ValueError) as error:
            ints.insert(1,"b")
        self.assertIsNotNone(error.exception)

    def test_if_insert_method_raises_when_passedOutOfRange_index(self):
        ints = IntegerList(1,2,3)
        with self.assertRaises(IndexError) as error:
            ints.insert(3,4)
        self.assertIsNotNone(error.exception)

    def test_if_get_index_returns_correct_data(self):
        ints = IntegerList(1,2,3,4)
        self.assertEqual(3, ints.get_index(4))

    def test_if_get_biggest_works_correctly(self):
        ints = IntegerList(1,2,3,4,5)
        self.assertEqual(5, ints.get_biggest())

    def test_if_get_index_throws_an_exception(self):
        ints = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError) as error:
            ints.get_index(5)
        self.assertIsNotNone(error.exception)


if __name__ == '__main__':
    unittest.main()