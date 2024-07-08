import json
from typing import List
from models.vacancy import Vacancy
from storage.base import VacancyStorage

class JSONSaver(VacancyStorage):
    """
    Класс для сохранения вакансий в JSON-файл.
    """
    FILE_PATH = 'vacancies.json'

    def __init__(self):
        self.vacancies = []

    def load_vacancies(self) -> List[Vacancy]:
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Vacancy(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError):
            # Если файл не найден, поврежден или имеет неправильную кодировку, вернуть пустой список
            return []

    def save_vacancies(self) -> None:
        with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump([vac.__dict__ for vac in self.vacancies], file, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, **criteria) -> List[Vacancy]:
        return [vac for vac in self.vacancies if all(getattr(vac, key) == value for key, value in criteria.items())]

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        self.vacancies = [vac for vac in self.vacancies if vac != vacancy]
        self.save_vacancies()
