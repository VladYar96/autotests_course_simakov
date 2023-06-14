# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


with open("test_file/task1_data.txt", encoding='utf-8') as text_origin:
    text_finish = '\n'.join([
        ''.join([char for char in line if not char.isnumeric()]).strip()
        for line in text_origin
    ])

with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as ethalon_file:
    ethalon_file.write(text_finish)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
