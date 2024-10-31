from src.vacancy import Vacancy
from src.utils import top_sort_vac

vacancy1 = Vacancy(name='водитель1',
                   url='https://hh.ru/vacancy/1"',
                   currency='RUR',
                   responsibility='возить',
                   salary_from=100000,
                   salary_to=150000)
vacancy2 = Vacancy(name='водитель2',
                   url='https://hh.ru/vacancy/2"',
                   currency='RUR',
                   responsibility='возить',
                   salary_from=80000,
                   salary_to=100000)
vacancy3 = Vacancy(name='водитель3',
                   url='https://hh.ru/vacancy/3"',
                   currency='RUR',
                   responsibility='возить',
                   salary_from=250000,
                   salary_to=300000)
vacancy4 = Vacancy(name='водитель4',
                   url='https://hh.ru/vacancy/4"',
                   currency='RUR',
                   responsibility='возить',
                   salary_from=0,
                   salary_to=70000)

vacancies = [vacancy1, vacancy2, vacancy3, vacancy4]


def test_top_sort_vac():
    top = top_sort_vac(vacancies, 2)
    assert len(top) == 2
    assert vacancy1 in top
    assert vacancy3 in top
