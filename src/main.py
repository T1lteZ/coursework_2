import os
import sys
sys.path.append(os.getcwd())
from src.api_vac import HH
from src.vacancy import Vacancy
from src.json_vac import HHVacancy
from src.utils import top_vacancy, filter_vacancy


def user_interaction():
    """Функция для взаимодействия с клиентом"""
    search_query = input("Введите поисковый запрос: ")
    hh = HH()
    city_search = input("Введите город для поиска вакансии: ")
    hh.load_vacancies(search_query)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary = int(input("Введите желаемую зарплату: "))
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    vacancy = Vacancy(search_query, city_search, salary)
    vacancy.reform_file(hh.vacancies)
    res_city = vacancy.filter_city()
    res_salary = vacancy.__le__(salary, res_city)
    result_fil_words = filter_vacancy(res_salary, filter_words)
    sd = HHVacancy()
    sd.safe_vacancy(result_fil_words)
    result_of_top = top_vacancy(top_n, result_fil_words)
    return result_of_top


print(user_interaction())
