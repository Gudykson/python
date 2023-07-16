# This is a comment
import math


def miejsca_zerowe():
    a = float(input("Podaj a:"))
    b = float(input("Podaj b:"))
    c = float(input("Podaj c:"))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Tożsamość")
            else:
                print("Sprzeczność")
        else:
            x = -c / b
            print("x = " + str(x))
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)

            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
        elif delta < 0:
            Re = -b / (2 * a)
            Im = math.sqrt(-delta) / (2 * a)
            print("x1 = " + str(Re) + " + " + str(Im))
            print("x2 = " + str(Re) + " - " + str(Im))
        else:
            x = -b / (2 * a)
            print("x = " + str(x))

while 1:
    s = int(input("Wybierz funkcje: \n0.Exit\n1.Miejsca zerowe\n "))
    if s == 1: miejsca_zerowe()
    elif s==0:exit()
