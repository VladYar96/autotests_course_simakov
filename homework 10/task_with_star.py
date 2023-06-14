# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest

@pytest.fixture(autouse=True)
def test2(request):
    """Выводим переданные в маркер аргументы на консоль"""
    marker = request.node.get_closest_marker("id_check")
    argum = ', '.join([str(i) for i in marker.args])
    print(f"Переданы аргументы {argum} в маркер {marker.name}\n")

@pytest.mark.id_check(1, 2, 3)
def test():
    """Тест с маркером"""
    pass
