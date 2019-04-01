#!C:/Python37/python3.exe

# тест Балке: расчёт МПК на основе дистанции покрытой бегом за 15 мин

import math, fileinput

def balke(distance):

    if (distance < 0):
        return -2

    if (distance > 6000):
        return -1 

    vo2max = 0.172 * (distance / 15 - 133) + 33.3

    return vo2max 

# end of balke()

def reverse_balke(vo2max):

    if (vo2max < 0):
        return -2

    if (vo2max > 100):
        return -1 

    distance = (( vo2max -  33.3 ) / 0.172 + 133) * 15

    return distance

# end of reverse_balke()


#### ---- main () -----

dist = int(raw_input("Enter distance completed in 15 minutes:"))

print(balke(dist))

vo2m = float(raw_input("Enter VDOT (float):"))

print(reverse_balke(float(vo2m)))
