from abc import ABC, abstractmethod
import os
import json


class Saver(ABC):
    """ Абстрактный класс для записи в файл """

    @abstractmethod
    def add_data(self, vacancy):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONSaver(Saver):
    """ Класс для записи в json-файл по пути data/vacancies.json"""

    def __init__(self, filepath: str = os.path.abspath("data/vacancies.json"), mode='w', encoding='utf-8'):
        self.__filepath = filepath
        self._mode = mode
        self._encoding = encoding

    def add_data(self, vacancies):
        if os.stat(self.__filepath).st_size == 0:
            all_vacancies = []

            for job in vacancies:
                job_data = {
                    'name': job.name,
                    'salary_from': job.salary_from,
                    'salary_to': job.salary_to,
                    'currency': job.currency,
                    "url": job.url,
                    "responsibility": job.responsibility
                }
                all_vacancies.append(job_data)

            with open(self.__filepath, self._mode, encoding=self._encoding) as file:
                json.dump(all_vacancies, file, ensure_ascii=False, indent=4)

            print(f'\nЯ нашел {len(vacancies)} подходящих вакансий и сохранил в файл {self.__filepath}\n\n')

        else:
            existing_vacancies = self.get_data()

            for job in vacancies:
                job_data = {
                    'name': job.name,
                    'salary_from': job.salary_from,
                    'salary_to': job.salary_to,
                    'currency': job.currency,
                    "url": job.url,
                    "responsibility": job.responsibility
                }
                existing_vacancies.get(job_data)

            with open(self.__filepath, self._mode, encoding=self._encoding) as file:
                json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)

            print(f'\nЯ нашел {len(vacancies)} подходящих вакансий и сохранил в файл {self.__filepath}\n\n'
                  f'В файле записано {len(existing_vacancies)} вакансий\n\n')

    def get_data(self):
        """ Получение данных json из файла"""

        with open(self.__filepath, 'r', encoding=self._encoding) as file:
            return json.load(file)

    def del_data(self):
        pass
