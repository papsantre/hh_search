from abc import ABC, abstractmethod
from typing import List
from models.vacancy import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный класс для хранения вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, **criteria) -> List[Vacancy]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass
