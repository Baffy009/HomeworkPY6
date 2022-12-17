#Из списка выше оставьте только те пары, где сумма кортежа кратна 5
#Пример
#[(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

numbers = [random.randint(1,100) for i in range(200)]

print(f'список пар, где сумма кортежа равна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(numbers)))}')
