# 2. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


list_arr = ["qw2e", "asd", "zxc", "qwre", "ertqwe"]
num = input("Input string: ")
count = []
for i in range(len(list_arr)):
    if str(num) in list_arr[i]:
        count.append(i)

try:
    print(count[1])
except:
    print("Второго вхождения в список нет.")


#     st = 'cnh'

# n_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

# ind = 0
# sh = 0
# m_ind = 0

# for i in n_list:

# if i == st and sh < 2:
# sh += 1
# m_ind = ind
# ind += 1

# if sh != 0:
# print(f'{n_list} - ищем: {st}, ответ {m_ind} индексе')
# else:
# print(f'{n_list} - ищем: {st}, ответ: -1')