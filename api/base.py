from abc import ABC, abstractmethod
from typing import List, Dict, Any


class JobAPI(ABC):
    """
    Абстрактный класс для работы с API сервисов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        pass
