# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from task_2 import all_division


class TestClass:
    """Класс с тестами"""

    @pytest.mark.usefixtures('start_time')
    @pytest.mark.parametrize('args, result', [pytest.param([15], 15, marks=pytest.mark.smoke),
                                              pytest.param([2, 8], 0.25)])
    def test1(self, args, result):
        assert all_division(*args) == result

    @pytest.mark.usefixtures('run_time')
    @pytest.mark.parametrize('args, result', [pytest.param([56, 2, 7, 4], 1.0),
                                              pytest.param([4, 2], 0, marks=pytest.mark.skip('bad test!!'))])
    def test2(self, args, result):
        assert all_division(*args) == result