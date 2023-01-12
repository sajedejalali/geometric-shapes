import math
shape = input("ci for circle & re for rectangle & sq for square & rh for rhombus & tri for triangle & pa for parallelogram & tra for trapezius ?")
action = input(" p for perimeter & a for area ?")


if shape == "ci" :
    if action == "p" :
        r = float(input("enter radius = "))
        pi = math.pi
        result = 2 * r * pi
    if action == "a" :
        r = float(input("enter radius = "))
        pi = math.pi
        result = r * r * pi

if shape == "re" :
    if action == "p" :
        w = float(input("enter w = "))
        h = float(input("enter h = "))
        result = (w + h) * 2
    if action == "a" :
        w = float(input("enter w = "))
        h = float(input("enter h = "))
        result = w * h

if shape == "sq" :
    if action == "p" :
        a = float(input("enter a = "))
        result = 4 * a
    if action == "a" :
        a = float(input("enter a = "))
        result = a * a

if shape == "rh" :
    if action == "p" :
        a = float(input("enter a = "))
        result = a * 4
    if action == "a" :
        d1 = float(input("enter d1 = "))
        d2 = float(input("enter d2 = "))
        result = (d1 * d2) / 2

if shape == "tri" :
    if action == "p" :
        a = float(input("enter a = "))
        b = float(input("enter b = "))
        c = float(input("enter c = "))
        result = a + b + c
    if action == "a" :
        h = float(input("enter h = "))
        a = float(input("enter a = "))
        result = (h * a) / 2

if shape == "pa" :
    if action == "p" :
        a = float(input("enter a = "))
        b = float(input("enter b = "))
        result = (2 * a) + (2 * b)
    if action == "a" :
        h = float(input("enter h = "))
        a = float(input("enter a = "))
        result = h * a

if shape == "tra" :
    if action == "p" :
        a = float(input("enter a = "))
        b = float(input("enter b = "))
        c = float(input("enter c = "))
        d = float(input("enter d = "))
        result = a + b + c + d
    if action == "a" :
        h = float(input("enter h = "))
        a = float(input("enter a = "))
        b = float(input("enter b = "))
        result =(a + b) * h / 2


print("result = ", result)