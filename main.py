def Corners(a,b,c):
    if c*c==(a*a+b*b):
        print("Треугольник прямоугольный")
    elif c*c<(a*a+b*b):
        print("Треугольник остроугольный")
    else:
        print("Треугольник тупоугольный")
def Types(a,b,c):
    if (a==b==c):
        print("Треугольник равносторонний")
    elif a==b or a==c or c==b:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")


print("Введите  стороны треугольника")
a=int(input())
b=int(input())
c=int(input())
if a>0 and b>0 and c>0:
    if ((c < a + b) and (a < b + c) and (b < a + c)):
        Corners(a, b, c)
        Types(a, b, c)
    else:
        print("Такого треугольника не существует")
else:
    print("Такого треугольника не существует")


