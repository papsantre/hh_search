import unittest
from unittest.mock import patch, Mock
from api.hh import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch('api.hh.requests.get')
    def test_get_vacancies(self, mock_get):
        # Создаем фейковый ответ от API
        mock_response = Mock()
        expected_data = {
            'items': [
                {'name': 'Python Developer', 'alternate_url': 'http://example.com',
                 'salary': {'from': 100000, 'to': 150000},
                 'snippet': {'requirement': 'Требования: опыт работы от 3 лет...'}}
            ]
        }
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies('Python')
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['name'], 'Python Developer')


if __name__ == "__main__":
    unittest.main()
