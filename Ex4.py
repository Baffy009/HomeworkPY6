#Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

url_list = ['https://gb.ru/lessons/284811/homework', 'https://github.com/Baffy009', 'https://www.python.org/']
url_list = [i for i in map(lambda i: i.lstrip('https://').lstrip('www.'), url_list)]
print(list(map(lambda i: i[:i.find('/')] ,url_list)))