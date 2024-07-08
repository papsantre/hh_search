from api.hh import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_storage import JSONSaver
from typing import List
import os


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем.
    """
    # Удаляем файл, если он существует
    if os.path.exists(JSONSaver.FILE_PATH):
        os.remove(JSONSaver.FILE_PATH)

    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query)
    print(f"Найдено вакансий: {len(vacancies)}")  # Отладочный вывод

    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    print(f"Количество объектов вакансий: {len(vacancies_list)}")  # Отладочный вывод

    # Создаем JSONSaver для сохранения новых данных
    json_saver = JSONSaver()

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            break
        except ValueError:
            print("Пожалуйста, введите число.")

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (например, 100000-150000): ")

    def filter_vacancies(vacancies: List[Vacancy], words: List[str]) -> List[Vacancy]:
        filtered = [vac for vac in vacancies if all(word.lower() in (vac.description or "").lower() for word in words)]
        print(f"Количество вакансий после фильтрации: {len(filtered)}")  # Отладочный вывод
        return filtered

    def get_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
        if '-' in salary_range:
            min_salary, max_salary = map(int, salary_range.split('-'))
            ranged = []
            for vac in vacancies:
                if vac.salary == "Зарплата не указана":
                    ranged.append(vac)
                else:
                    salary_from, salary_to = vac.get_salary_range()
                    if salary_from is not None and (min_salary <= salary_from <= max_salary):
                        ranged.append(vac)
                    elif salary_to is not None and (min_salary <= salary_to <= max_salary):
                        ranged.append(vac)
            print(f"Количество вакансий после фильтрации по зарплате: {len(ranged)}")  # Отладочный вывод
            return ranged
        return vacancies

    def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
        sorted_list = sorted(vacancies, reverse=True)
        print(f"Количество вакансий после сортировки: {len(sorted_list)}")  # Отладочный вывод
        return sorted_list

    def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
        top_list = vacancies[:top_n]
        print(f"Количество топ вакансий: {len(top_list)}")  # Отладочный вывод
        return top_list

    def print_vacancies(vacancies: List[Vacancy]) -> None:
        if not vacancies:
            print("Нет вакансий для отображения")
        for vac in vacancies:
            print(f"Название: {vac.title}")
            print(f"Зарплата: {vac.salary}")
            print(f"URL: {vac.url}")
            print(f"Описание: {vac.description}")
            print("-" * 40)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
