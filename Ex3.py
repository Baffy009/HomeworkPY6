#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

print(list((-3)**i for i in range(int(input('N: ')))))

print(list(map(lambda i: (-3)**i, [i for i in range(int(input('N: ')))])))