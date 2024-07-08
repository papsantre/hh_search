from typing import List, Dict, Any, Optional, Tuple


class Vacancy:
    """
    Класс для представления вакансии.
    """

    def __init__(self, title: str, url: str, salary: str, description: str):
        self.title = title
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description

    def __lt__(self, other) -> bool:
        return self.get_salary_value() < other.get_salary_value()

    def __eq__(self, other) -> bool:
        return self.get_salary_value() == other.get_salary_value()

    def get_salary_value(self) -> int:
        """
        Преобразование зарплаты в числовое значение для сравнения.
        """
        if "руб" in self.salary:
            try:
                salary = self.salary.replace('руб.', '').replace(' ', '').split('-')
                if len(salary) == 2:
                    return (int(salary[0]) + int(salary[1])) // 2
                return int(salary[0])
            except ValueError:
                return 0
        return 0

    def get_salary_range(self) -> Tuple[Optional[int], Optional[int]]:
        """
        Преобразование зарплаты в диапазон значений для фильтрации.
        """
        if "руб" in self.salary:
            try:
                salary = self.salary.replace('руб.', '').replace(' ', '').split('-')
                if len(salary) == 2:
                    return int(salary[0]), int(salary[1])
                return int(salary[0]), None
            except ValueError:
                return None, None
        return None, None

    @staticmethod
    def cast_to_object_list(vacancies: List[Dict[str, Any]]) -> List['Vacancy']:
        vacancy_objects = []
        for vac in vacancies:
            title = vac.get('name', 'Без названия')
            url = vac.get('alternate_url', '')
            salary_info = vac.get('salary')
            salary = 'Зарплата не указана'
            if salary_info:
                salary_from = salary_info.get('from')
                salary_to = salary_info.get('to')
                if salary_from and salary_to:
                    salary = f"{salary_from}-{salary_to} руб."
                elif salary_from:
                    salary = f"от {salary_from} руб."
                elif salary_to:
                    salary = f"до {salary_to} руб."
            description = vac.get('snippet', {}).get('requirement', 'Описание не указано')
            vacancy_objects.append(Vacancy(title, url, salary, description))
        return vacancy_objects
