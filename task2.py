# Найдите сумму цифр трехзначного числа.
from os import system
system("cls")  # чистит консоль

flag = True  # повтор ввода если не число
while flag:
    try:
        x = int(input("введите число: "))
        flag = False
    except:
        print("это не число, попробуйте ещё раз")

result = 0
while x > 0:
    result += x % 10
    x //= 10
print("Сумма чисел данного числа:", result)
