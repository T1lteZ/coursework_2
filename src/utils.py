from src.vacancy import Vacancy
from typing import List


def top_sort_vac(all_vac: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Функция сортирует и выводить первые N результатов после сортировки"""
    all_vac = sorted(all_vac, reverse=True)
    return all_vac[:top_n]
