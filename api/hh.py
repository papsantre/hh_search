import requests
from typing import List, Dict, Any
from api.base import JobAPI


class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru.
    """
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str) -> List[Dict[str, Any]]:
        params = {
            'text': search_query,
            'area': 113,  # Россия
            'per_page': 100
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()['items']
