#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#Примеры
#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

#my_list, find = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"
#my_list, find = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"
#my_list, find = ["123", "234", 123, "567"], "123"

my_list, find = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"
pos = -1 if my_list.count(find) < 2 else list(filter(lambda x: x[1] == find, enumerate(my_list)))[1][0]
print(f'позиция второго вхождения "{find}" -> {pos}')