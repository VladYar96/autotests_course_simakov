import pytest
import time
import datetime


@pytest.fixture(autouse=True)
def start_time():
    """Выводим время начала выполнения и завершения теста """
    start = datetime.datetime.now()
    print(f'\t Тест запустился в {start.strftime("%d.%m %H:%M:%S")}')
    yield
    end = datetime.datetime.now()
    print(f'\n\t Тест завершился в {end.strftime("%d.%m %H:%M:%S")}')


@pytest.fixture(autouse=True)
def run_time():
    """Выводим время выполнения теста"""
    start = time.time()
    yield
    end = time.time()
    print(f'\t Время выполнения теста: {end - start}')
