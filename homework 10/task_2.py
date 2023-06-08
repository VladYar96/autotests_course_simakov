# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1_mark():
    assert all_division(15) == 15

@pytest.mark.function
def test2_mark():
    assert all_division(2, 8) == 0.25


@pytest.mark.smoke
def test3_mark():
    assert all_division(56, 2, 7, 4) == 1.0


def test4():
    assert all_division(2.5, 25) == 0.1


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(4, 2, 0)

