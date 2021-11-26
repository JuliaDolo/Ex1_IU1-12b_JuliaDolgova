print("Введите  стороны треугольника")
a=int(input())
b=int(input())
c=int(input())
if ((c<a+b) and (a<b+c) and (b<a+c)):
    if c*c==(a*a+b*b):
        print("Треугольник прямоугольный")
    elif c*c<(a*a+b*b):
        print("Треугольник остроугольный")
    else:
        print("Треугольник тупоугольный")
else:
    print("Такого треугольника не существует")
