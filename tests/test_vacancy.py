import unittest
from models.vacancy import Vacancy


class TestVacancyMethods(unittest.TestCase):

    def setUp(self):
        self.vacancy1 = Vacancy("Python Developer", "http://example.com", "100000-150000 руб.",
                                "Требования: опыт работы от 3 лет...")
        self.vacancy2 = Vacancy("Java Developer", "http://example.com", "150000-200000 руб.",
                                "Требования: опыт работы от 3 лет...")
        self.vacancy_no_salary = Vacancy("No Salary Developer", "http://example.com", "",
                                         "Требования: опыт работы от 3 лет...")

    def test_salary_comparison(self):
        self.assertTrue(self.vacancy1 < self.vacancy2)
        self.assertTrue(self.vacancy2 > self.vacancy1)
        self.assertEqual(self.vacancy_no_salary.get_salary_value(), 0)

    def test_salary_range(self):
        self.assertEqual(self.vacancy1.get_salary_range(), (100000, 150000))
        self.assertEqual(self.vacancy2.get_salary_range(), (150000, 200000))
        self.assertEqual(self.vacancy_no_salary.get_salary_range(), (None, None))

    def test_cast_to_object_list(self):
        vacancies_data = [
            {"name": "Python Developer", "alternate_url": "http://example.com",
             "salary": {"from": 100000, "to": 150000},
             "snippet": {"requirement": "Требования: опыт работы от 3 лет..."}},
            {"name": "Java Developer", "alternate_url": "http://example.com", "salary": {"from": 150000, "to": 200000},
             "snippet": {"requirement": "Требования: опыт работы от 3 лет..."}},
            {"name": "No Salary Developer", "alternate_url": "http://example.com", "salary": None,
             "snippet": {"requirement": "Требования: опыт работы от 3 лет..."}}
        ]
        vacancies = Vacancy.cast_to_object_list(vacancies_data)
        self.assertEqual(len(vacancies), 3)
        self.assertEqual(vacancies[0].title, "Python Developer")
        self.assertEqual(vacancies[2].salary, "Зарплата не указана")


if __name__ == "__main__":
    unittest.main()
