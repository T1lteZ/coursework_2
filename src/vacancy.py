from typing import List


class Vacancy:
    """ Класс для работы с вакансиями """

    def __init__(self, name, salary_from, salary_to, currency, url, responsibility):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url
        self.responsibility = responsibility

    def __lt__(self, other):
        """Метод сравнения вакансий между собой по зарплате по зарплате"""

        if self.salary_from != 0:
            return self.salary_from <= other.salary_from
        elif self.salary_from == 0:
            return self.salary_to <= other.salary_from

    def __str__(self):
        """Метод для представляния вакансий при печати"""
        a = (f'Название вакансии: {self.name}\n'
             f'Ссылка на вакансию: {self.url}\n'
             f'Описание вакансии: {self.responsibility}\n')
        if self.salary_from == 0 and self.salary_to == 0:
            return (f'{a}'
                    f'ЗП не указана\n')
        elif self.salary_from == 0:
            return (f'{a}'
                    f'ЗП до {self.salary_to} {self.currency}\n')
        elif self.salary_to == 0:
            return (f'{a}'
                    f'ЗП от {self.salary_from} {self.currency}\n')
        else:
            return (f'{a}'
                    f'ЗП от {self.salary_from} до {self.salary_to} {self.currency}\n')

    @classmethod
    def cast_to_object_list(cls, data: List[dict]) -> List['Vacancy']:
        """Преобразует список словарей, содержащих данные о вакансиях, в список объектов класса Vacancy"""

        vacancies = []
        for item in data:
            name = item['name']
            url = item['alternate_url']
            salary_from = item['salary']['from']
            salary_to = item['salary']['to']
            currency = item['salary']['currency']
            responsibility = item['snippet']['responsibility']
            vacancy = cls(
                name=name,
                url=url,
                salary_from=salary_from,
                salary_to=salary_to,
                currency=currency,
                responsibility=responsibility
            )
            vacancies.append(vacancy)
        return vacancies
