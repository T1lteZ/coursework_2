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
    """ Класс для записи в json-файл по пути data/vacancies.json (файл config)"""

    def __init__(self, filepath: str = os.path.abspath("data/vacancies.json"), mode='w', encoding='utf-8'):
        self.__filepath = filepath
        self._mode = mode
        self._encoding = encoding

    def add_data(self, vacancy):
        """Сохранить все вакансии в файл"""

        if os.stat(self.__filepath).st_size == 0:
            with open(self.__filepath, self._mode, encoding=self._encoding) as file:
                json.dump(vacancy, file, ensure_ascii=False, indent=4)

            print(f'\nЯ нашел {len(vacancy)} подходящих вакансий и сохранил в файл {self.__filepath}\n\n')

        else:
            existing_vacancies = self.get_data()

            for i in vacancy:
                if i in existing_vacancies:
                    continue
                else:
                    existing_vacancies.append(i)

            with open(self.__filepath, self._mode, encoding=self._encoding) as file:
                json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)

            print(f'\nЯ нашел {len(vacancy)} подходящих вакансий и сохранил в файл {self.__filepath}\n\n'
                  f'В файле записано {len(existing_vacancies)} вакансий\n\n')

    def get_data(self):
        """ Получение данных json из файла"""

        with open(self.__filepath, encoding=self._encoding) as file:
            return json.loads(file.read())

    def del_data(self):
        """ Удаление данных из файла """
        pass
