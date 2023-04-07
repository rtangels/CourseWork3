import unittest

import functions

from functions import *


class TestFunctions(unittest.TestCase):
    def test_born_list(self):
        """
        Тест функции формирования списка
        """
        self.assertIsInstance(functions.born_list('operations.json'), list)

    def test_filter_by_state(self):
        """
        Тест функции, которая
        выделяет данный
        по операциям с пометкой Выполнена
        """
        new_list = born_list('operations.json')
        new_list = filter_by_state(new_list)
        for i in range(len(new_list)):
            self.assertIn('state', new_list[i])

    def test_get_date(self):
        """
        Тест функции,
        которая возвращает дату
        из словаря
        """
        d = {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041"
        }
        self.assertEqual(get_date(d), "2019-08-26T10:50:58.294041")

    def test_sort_by_date(self):
        """
        Тест функции,которая
        сортирует по дате
        """
        date_list = ['2019-12-07T06:17:14.634890',
                     '2019-11-19T09:22:25.899614',
                     '2019-11-13T17:38:04.800051',
                     '2019-10-30T01:49:52.939296',
                     '2019-09-29T14:25:28.588059']

        new_list = born_list('input.json')
        new_list = filter_by_state(new_list)
        new_list = sort_by_date(new_list)

        for i in range(len(new_list)):
            self.assertEqual(new_list[i]['date'], date_list[i])

    def test_formated_output(self):
        new_list = [{
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }]
        etalon_list = [
            '04.04.2018 Перевод организации\n'
            'Visa Gold 5999 41** **** 6353 ->'
            ' Счет  **4472\n40701.91 USD'
        ]
        second_list = [{
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 72731966109147704472"
        }]
        second_etalon_list = [
            '04.04.2018 Перевод организации\n'
            'Счёт неизвестен -> Счет  **4472\n'
            '40701.91 USD\n']
        new_list = formated_output(new_list)
        second_list = formated_output(second_list)
        self.assertEqual(new_list, etalon_list)
        self.assertEqual(second_list, second_etalon_list)

if __name__ == '__main__':
    unittest.main()
