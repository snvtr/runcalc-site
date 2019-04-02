#!C:/Python37/python3.exe

# тест Купер: расчёт МПК из дистанции покрытой бегом за 12 минут

import math, fileinput

def cooper(distance):

    if (distance < 0):
        return -2

    if (distance > 5000):
        return -1

    vo2max = (distance - 504.9)/44.73

    return '%2.2f' % vo2max

# end of cooper()

def cooper_indian_mod(distance):

    if (distance < 0):
        return -2

    if (distance > 5000):
        return -1

    vo2max = 21.01*distance/1000 - 11.04
 
    return '%2.2f' % vo2max

# end of cooper_indian_mod()

def reverse_cooper(vo2max):

    if (vo2max < 0):
        return -2

    if (vo2max > 100):
        return -1

    distance = vo2max*44.73 + 504.9

    return '%4d' % distance

# end of reverse_cooper()

def reverse_cooper_indian_mod(vo2max):

    if (vo2max < 0):
        return -2

    if (vo2max > 100):
        return -1

    distance = (vo2max + 11.04)/0.02101

    return '%4d' % distance

# end of reverse_cooper_indian_mod()

#### ---- main () -----

dist = int(raw_input("Enter distance run in 12 minutes:"))

print cooper(dist)
print cooper_indian_mod(dist)

vo2m = float(raw_input("Enter VDOT (float):"))

print reverse_cooper(float(vo2m))
print reverse_cooper_indian_mod(float(vo2m))
