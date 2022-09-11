# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
spisok=[1.1, 1.2, 3.1, 5, 10.01]
spisok1=[]
for i in range(len(spisok)):
    temp=spisok[i]%1
    if temp!=0:
        spisok1.append(temp)
max_number=max(spisok1)
min_number=min(spisok1)
result=max_number-min_number
print(spisok,'=>',result)

       
    
