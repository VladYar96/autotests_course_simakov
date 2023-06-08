# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_string(leng):
    """
    Генерирую строку
    :param leng: длина строки
    :return: сгенерированная строка
    """
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(leng))

    return random_string


def generate_random_name():
    """
    Соединяю 2 сгенерированных слова, длиной от 1 до 15 символов
    :return: Строка из двух сгенерированных слов, разделенная пробелом
    """
    while True:
        string_1 = generate_random_string(random.randint(1, 15))
        string_2 = generate_random_string(random.randint(1, 15))
        yield f'{string_1} {string_2}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
