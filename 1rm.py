#!/usr/bin/python3

import sys

#sys.argv = ["--weight=78", "--reps=12"]

###### subs() ###### 

def epley(weight, reps):
    return round(weight * ( 1 + reps / 30 ))
    
def brzycki(weight, reps):
    return round(weight * 36 / ( 37 - reps))
    
def mcglothin(weight, reps):
    return round(100 * weight / (101.3 - 2.67123 * reps))

def lombardi(weight, reps):
    return round(weight * (reps ** 0.1))

def mayhew(weight, reps):
    return round(100 * weight / (52.2 + 41.9 * (2.71828182846 ** (-0.055 * reps))))

def oconner(weight, reps):
    return round(weight * (1 + reps / 40 ))

def wathan(weight, reps):
    return round(100 * weight / (48.8 + 53.8 * (2.71828182846 ** (-0.075 * reps))))

###

def rev_epley(rm, reps):
    return round(rm / ( 1 + reps / 30 ))
    
def rev_brzycki(rm, reps):
    return round(rm * ( 37 - reps ) / 36)

###### __main()__ ###### 

weight = 0
reps   = 0
rm     = 0

if len(sys.argv) > 1:
    for i in sys.argv:
        if i[0:9] == "--weight=":
            weight = int(i[9:])
        elif i[0:7] == "--reps=":
            reps = int(i[7:])
        elif i[0:6] == "--1rm=":
            rm = int(i[6:])
else:
    print("Only integers are allowed")
    print("arguments are either '--weight=XX --reps=Y' or '--1rm=XX --reps=X'")
    print("--weight cannot be less than 30 in kilos, --reps cannot be more than 12")
    sys.exit(1)

if weight > 30 and rm == 0:
    if reps < 1:
        print("--reps cannot be omitted or set less than 1")
        sys.exit(2)
    elif reps > 12:
        print("--reps parameter is too high (12 reps max)")
        sys.exit(3)
elif rm == 0:
    print("--weight should be of correct value (30 or more)")
    sys.exit(4)

if rm != 0:
    if reps < 1:
        print("--reps cannot be omitted or set less than 1")
        sys.exit(5)
    elif reps > 12:
        print("--reps parameter is too high (12 reps max)")
        sys.exit(6)
    
if rm == 0:    
    print("Epley formula:", epley(weight,reps))
    print("Brzycki formula:", brzycki(weight,reps))
    print("McGlothin formula:", mcglothin(weight,reps))
    print("Lombardi formula:", lombardi(weight,reps))
    print("Mayhew formula:", mayhew(weight,reps))
    print("O'Connor formula:", oconner(weight,reps))
    print("Wathan formula:", wathan(weight,reps))
else:
    print("Reverse Epley formula:", rev_epley(rm,reps))
    print("Reverse Brzycki formula:", rev_brzycki(rm,reps))
    
