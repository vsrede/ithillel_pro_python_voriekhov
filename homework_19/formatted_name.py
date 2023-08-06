import unittest
from faker import Faker

faker = Faker()


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):

    def test_normal_full_date(self):
        result = formatted_name("vlad", "olegov", middle_name="sergio")
        self.assertEqual(result, 'Vlad Sergio Olegov')

        result = formatted_name("anna-marie", "olegov", middle_name="sergio")
        self.assertEqual(result, 'Anna-Marie Sergio Olegov')

    def test_normal_full_corner_date(self):
        result = formatted_name("vlad", "olegov", middle_name="k")
        self.assertEqual(result, 'Vlad K Olegov')

    def test_normal_upper_full_date(self):
        result = formatted_name("VLAD", "OLEGOV", middle_name="SERGIO")
        self.assertEqual(result, 'Vlad Sergio Olegov')

    def test_normal_half_date(self):
        result = formatted_name("vlad", "olegov")
        self.assertEqual(result, "Vlad Olegov")

    def test_empty_date(self):
        result = formatted_name("", "")
        self.assertEqual(result, " ")

    def test_none_date(self):
        with self.assertRaises(TypeError):
            formatted_name("vlad", "olegov", middle_name=None)

        with self.assertRaises(TypeError):
            formatted_name("vlad", None, middle_name="olegov")

    def test_int_date(self):
        with self.assertRaises(TypeError):
            formatted_name(1, 2)

    def test_big_data(self):
        first_name = (faker.lexify(text='?' * 100)).lower().title()
        last_name = (faker.lexify(text='?' * 100)).lower().title()
        middle_name = (faker.lexify(text='?' * 100)).lower().title()

        result = formatted_name(first_name, last_name, middle_name=middle_name)
        self.assertEqual(result, f'{first_name} {middle_name} {last_name}')

    def test_space_full_date(self):
        result = formatted_name(" vlad", "olegov ", middle_name="sergio")
        self.assertEqual(result, 'Vlad Sergio Olegov')
