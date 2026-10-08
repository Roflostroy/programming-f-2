#1
print('Задание 1')
a,b = int(input("Введите a: ")), int(input("Введите b: "))
if a >= b:
    a = 0
    print(a,b)
else:
    print(a**2,b**2)
#2
print('Задание 2')
print("Данные первого треугольника")
a1,b1, f1 = int(input('Введите первую сторону: ')), int(input('Введите воторую сторону: ')), int(input('Введите угол: '))
print("Данные второго треугольника")
a2,b2, f2 = int(input('Введите первую сторону: ')), int(input('Введите воторую сторону: ')), int(input('Введите угол: '))
if f1 == f2 and ((a1 == a2 and b1 == b2) or (a1 == b2 and b1 == a2)):
    print('Треугольники равны')
else:
    print('Треугольники не равны')
#3
print('Задание 3')
x,y,z = int(input("Введите x: ")), int(input("Введите y: ")), int(input("Введите z: "))
if x+y>z and x+z>y and y+z>x:
    print('Треугольник есть')
    if x==y==z:
        print("Треугольник равносторонний")
    elif x == y or x == z or y == z:
        print("Треугольник равнобедренный")
    elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        print("Треугольник прямоугольный")
else:
    print('Треугольника нет')