from abc import ABC, abstractmethod
import os
import json
import requests


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
            all_vacancies = [vac.to_dict() for vac in vacancies]
        else:
            existing_vacancies = self.get_data()
            new_vacancies = [vac.to_dict() for vac in vacancies]
            all_vacancies = existing_vacancies + new_vacancies

        with open(self.__filepath, self._mode, encoding=self._encoding) as file:
            json.dump(all_vacancies, file, ensure_ascii=False, indent=4)

        print(f'\nЯ нашел {len(vacancies)} подходящих вакансий и сохранил в файл {self.__filepath}\n'
              f'В файле записано {len(all_vacancies)} вакансий\n\n')

    def get_data(self):
        """ Получение данных json из файла"""

        with open(self.__filepath, 'r', encoding=self._encoding) as file:
            return json.load(file)

    def del_data(self, url: str):
        vacancies = self.get_data()

        updated_vacancies = [vac for vac in vacancies if vac['url'] != url]

        with open(self.__filepath, 'w', encoding=self._encoding) as file:
            json.dump(updated_vacancies, file, ensure_ascii=False, indent=4)
