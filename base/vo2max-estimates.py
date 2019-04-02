#C:/Python37/python3.exe

# приблизительный расчет МПК из: 
# данных о весе, возрасте и пульсе покоя (vo2maxWAHR)
# данных о поле, обхвате талии, возрасте, пульсе покоя, уровне активности, интенсивности тренировок и их частоты
#

import math, fileinput

def vo2maxWAHR(weight,age,rhr):

    if (weight < 0):
        return -2

    if (weight > 500):
        return -1

    if (age < 0):
        return -2

    if (age > 120):
        return -1

    if (rhr < 0):
        return -2

    if (rhr > 100):
        return -1

    vo2max = 1000*(3.542-0.014*age+0.015*weight-0.011*rhr)/weight
    return '%2.2f' % vo2max

# end of vo2maxWAHR()

def vo2maxActIAWHR(waist,age,rhr,activity,intensity,freq,gender):

    if (waist < 0):
        return -2

    if (waist > 200):
        return -1

    if (age < 0):
        return -2

    if (age > 120):
        return -1

    if (rhr < 0):
        return -2

    if (rhr > 100):
        return -1

    if (activity < 1):
        return -2

    if (activity > 1.5):
        return -1

    if (intensity < 0):
        return -2

    if (intensity > 10):
        return -1

    if (freq < 0):
        return -2

    if (freq > 3):
        return -1

    if (gender < 0):
        return -2

    if (gender > 1):
        return -1

    if (gender == 0):
        vo2max = 100.27 + 0.226 * activity * intensity * freq - 0.296 * age - 0.369 * waist - 0.155 * rhr
    else:
        vo2max = 74.74 + 0.198 * activity * intensity * freq - 0.247 * age - 0.259 * waist - 0.114 * rhr

    return '%2.2f' % vo2max

# end of vo2maxActIAWHR()

#### ---- main () -----


age_value = int(input("Enter your age (full years):"))
rhr_value = int(input("Enter your resting heart rate (beats):"))
waist_value = int(input("Enter your waist (cm):"))
weight_value = int(input("Enter your weight (kg):"))
gender_value = int(input("Enter your gender (m - 0 /f - 1):"))
freq_value = int(input("How often do you exercise times/week (0 (<1)-1 (1)- 2 (2-3)-3 (3+)):"))
intens_value = int(input("How intense do you exercise (light - 0/moderate - 5/to exhaustion - 10):"))
activ_value = float(input("How long are your exercise (less then 30 min - 1/more than 30 min - 1.5):"))

print(vo2maxWAHR(weight_value,age_value,rhr_value))
print(vo2maxActIAWHR(waist_value,age_value,rhr_value,activ_value,intens_value,freq_value,gender_value))

