# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


fib_value=int(input('Задайте число ='))
fib_list=[0,1]
fib1=0
fib2=1
fib_revers=[1]
for i in range(1,fib_value):
    temp=fib2+fib1
    fib1=fib2
    fib2=temp
    fib_list.append(temp)
    fib_revers.append(temp)

for i in range(1,fib_value,2):
    fib_revers[i]=-fib_revers[i]
fib_revers.reverse()
print(fib_revers+fib_list)
