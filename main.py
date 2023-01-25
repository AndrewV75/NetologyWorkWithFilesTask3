''' Задача №3
В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее
известны. Необходимо объединить их в один по следующим правилам:

1) Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству
строк в них (то есть первым нужно записать файл с наименьшим количеством строк,
а последним - с наибольшим)
2) Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и
оличество строк в нем '''

import operator

# Функция объединения словарей
def mergeDict(dict1, dict2):
    for k, v in dict2.items():
        if dict1.get(k):
            dict1[k] = [dict1[k], v]
        else:
            dict1[k] = v
    return dict1


dict_lines = {} # словарь {имя файла : кол-во строк в файле}
dict_text = {} # словарь {имя файла : текст из файла}

with open('1.txt', encoding='utf-8') as f:
    name = '1.txt'
    count_lines = 0
    text = []

    for lines in f:
        count_lines += 1
        text.append(lines)
        dict_lines[name] = count_lines
        dict_text[name] = text

with open('2.txt', encoding='utf-8') as f:
    name = '2.txt'
    count_lines = 0
    text = []

    for lines in f:
        count_lines += 1
        text.append(lines)
        dict_lines[name] = count_lines
        dict_text[name] = text

with open('3.txt', encoding='utf-8') as f:
    name = '3.txt'
    count_lines = 0
    text = []

    for lines in f:
        count_lines += 1
        text.append(lines)
        dict_lines[name] = count_lines
        dict_text[name] = text

# print(dict_lines)
# print(dict_text)

#  сортировка словаря с кол-вом строк по возрастанию
sorted_lines = sorted(dict_lines.items(), key=operator.itemgetter(1))
sorted_dict_lines = {k: v for k, v in sorted_lines}

# print(sorted_dict_lines)

# Объединяем словари: {{имя файла : [кол-во строк в файле [текст]]}
dict_to_write = mergeDict(sorted_dict_lines, dict_text)
# print(dict_to_write)

# запись словаря в файл

with open('text.txt', 'w', encoding='utf-8') as file:
    for key, value in dict_to_write.items():
        file.write(f'{key}\n {value[0]}\n {" ".join(map(str, value[1]))}\n')



