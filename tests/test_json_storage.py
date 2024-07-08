import unittest
import os
from models.vacancy import Vacancy
from storage.json_storage import JSONSaver


class TestJSONSaverMethods(unittest.TestCase):

    def setUp(self):
        self.saver = JSONSaver()
        self.saver.vacancies = []  # Очистка списка вакансий перед каждым тестом
        self.vacancy = Vacancy("Python Developer", "http://example.com", "100000-150000 руб.",
                               "Требования: опыт работы от 3 лет...")
        self.vacancy2 = Vacancy("Java Developer", "http://example.com", "150000-200000 руб.",
                                "Требования: опыт работы от 3 лет...")
        if os.path.exists(JSONSaver.FILE_PATH):
            os.remove(JSONSaver.FILE_PATH)

    def tearDown(self):
        if os.path.exists(JSONSaver.FILE_PATH):
            os.remove(JSONSaver.FILE_PATH)

    def test_add_vacancy(self):
        self.saver.add_vacancy(self.vacancy)
        self.assertIn(self.vacancy, self.saver.vacancies)

    def test_get_vacancies(self):
        self.saver.add_vacancy(self.vacancy)
        self.saver.add_vacancy(self.vacancy2)
        result = self.saver.get_vacancies(title="Python Developer")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Python Developer")

    def test_delete_vacancy(self):
        self.saver.add_vacancy(self.vacancy)
        self.saver.delete_vacancy(self.vacancy)
        self.assertNotIn(self.vacancy, self.saver.vacancies)

    def test_save_and_load_vacancies(self):
        self.saver.add_vacancy(self.vacancy)
        self.saver.save_vacancies()
        loaded_saver = JSONSaver()
        loaded_saver.vacancies = loaded_saver.load_vacancies()
        self.assertEqual(len(loaded_saver.vacancies), 1)
        self.assertEqual(loaded_saver.vacancies[0].title, "Python Developer")


if __name__ == "__main__":
    unittest.main()
