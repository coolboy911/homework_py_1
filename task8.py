# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
from os import system
system("cls")

flag = True
while flag:
    try:
        n = int(input("введите число n: "))
        m = int(input("введите число m: "))
        k = int(input("введите число k: "))
        flag = False
    except:
        print("это не число, попробуйте ещё раз")

if (k % n == 0 and k // n <= m) or (k % m == 0 and k // m <= n):
    print("yes")
else:
    print("no")