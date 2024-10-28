from src.api_vac import HeadHunterRuAPI
from src.vacancy import Vacancy
from src.json_vac import JSONSaver
from src.utils import top_sort_vac


def main():

    a = HeadHunterRuAPI()
    user_text = input("Введите ключевые слова для поиска вакансии (может быть несколько слов):\n")
    vacancies = a.getting_vacancies(user_text)
    valid_vacancies = a.validate_data(vacancies)

    vacancies_json = JSONSaver()
    vacancies_json.add_data(valid_vacancies)

    user_vacancies = JSONSaver()
    vac_data = Vacancy.cast_to_object_list(user_vacancies.get_data())

    try:
        user_top_vac = int(input("Я покажу топ N вакансий по заплате. Сколько вакансий вывести? (число) \n\n"))
        top_n_vac = top_sort_vac(vac_data, user_top_vac)
        for w in top_n_vac:
            print(w)
    except ValueError:
        print("Необходимо ввести число ")


if __name__ == "__main__":
    main()
