# test_solution.py

import unittest
import os
import csv
from solution import get_animals_count

class TestGetAnimals(unittest.TestCase):
    def setUp(self):
        # Удаляем файл перед каждым тестом, если он существует
        if os.path.exists('beasts.csv'):
            os.remove('beasts.csv')

    def test_get_animals(self):
        try:
            get_animals_count()
        except Exception as e:
            self.fail(f"get_animals raised Exception unexpectedly: {e}")

        self.assertTrue(os.path.exists('beasts.csv'))

        with open('beasts.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        # Проверяем, что файл не пустой
        self.assertGreater(len(data), 0, "The CSV file is empty")

        # Проверяем, что каждая строка содержит ровно два элемента
        for row in data:
            self.assertEqual(len(row), 2, f"Row {row} does not contain exactly 2 elements")
            self.assertTrue(row[0].isalpha(), f"First element {row[0]} is not a letter")
            self.assertTrue(row[1].isdigit(), f"Second element {row[1]} is not a digit")

    def tearDown(self):
        # Удаляем файл после каждого теста
        if os.path.exists('beasts.csv'):
            os.remove('beasts.csv')

if __name__ == "__main__":
    unittest.main()
