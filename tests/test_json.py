import json
import os
import pytest
from src.json_vac import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def json_saver():
    file_path = "test.json"

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', encoding='utf-8'):
        pass

    saver = JSONSaver(file_path)
    yield saver
    os.remove(file_path)


def test_saver(json_saver):
    vac = Vacancy(
        name="Водитель погрузчика (без опыта)",
        salary_from=70000,
        salary_to=0,
        currency="RUR",
        url="https://hh.ru/vacancy/109471443",
        responsibility="Погрузо-разгрузочные работы на погрузчике. Следить за состоянием погрузчика (мелкий ремонт)."
    )

    json_saver.add_data([vac])
    with open("test.json", encoding="utf-8") as f:
        data = json.load(f)

    expected_data = [
        {
            "name": "Водитель погрузчика (без опыта)",
            "salary_from": 70000,
            "salary_to": 0,
            "currency": "RUR",
            "url": "https://hh.ru/vacancy/109471443",
            "responsibility": "Погрузо-разгрузочные работы на погрузчике. Следить за состоянием погрузчика (мелкий ремонт)."
        }
    ]

    assert data == expected_data

