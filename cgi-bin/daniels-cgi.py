#!/usr/bin/python

import os
import math, fileinput

########################

def daniels(distance, time):

    time_parts = time.split(':')

# in minutes
    duration = float(time_parts[0]) * 60 + float(time_parts[1]) + (float(time_parts[2]) / 60)

# metres per minute
    velocity = distance / duration

    vo2max = (-4.60 + 0.182258 * velocity + 0.000104 * math.pow(velocity,2)) / (0.8 + 0.1894393 * math.exp(-0.012778 * duration) + 0.2989558 * math.exp(-0.1932605 * duration)) 
       
    return vo2max

# end of daniels()

def get_function(race_d,race_t,race_VDOT):

    upper = 0.000104 * race_d**2 * race_t**-2 + 0.182258 * race_d * race_t**-1 - 4.6
    lower = 0.2989558 * math.exp(-0.1932605*race_t) + 0.1894393 * math.exp(-0.012778*race_t) + 0.8

    return (upper/lower - race_VDOT)

# end of get_function()

def get_derivative(race_d,race_t,race_VDOT):

    upper = ((((0.2989558*math.exp(-0.1932605*race_t))+(0.1894393*math.exp(-0.012778*race_t))+0.8)*((-0.000208)*(race_d**2)*(race_t**-3))-((0.182258)*race_d*(race_t**-2)))-(race_VDOT*((0.2989558)*(math.exp(-0.1932605*race_t))+(0.1894393)*(math.exp(-0.012778*race_t)))))
    lower = (0.2989558 * math.exp(-0.1932605 * race_t) + 0.1894393 * math.exp(-0.012778 * race_t) + 0.8)**2
    return (upper/lower)

# end of get_derivative()

def reverse (d, VDOT):

    t = 60

    if t <= 42200:
        t = 220

    if t <= 21100:
        t = 110

    if t <= 10000:
        t = 50

    if t <= 5000:
        t = 25

    if t <= 3000:
        t = 12

    function   = get_function (d, t, VDOT)
    derivative = get_derivative (d, t, VDOT) 

    i = 0

    while abs(function/derivative) > 0.000001:
   
        i = i + 1

        if i > 100:
            break

#        print function
#        print derivative
#        print t,"-"

        t = t - function/derivative

        function   = get_function (d, t, VDOT)
        derivative = get_derivative (d, t, VDOT)

#    print "final:",t,"(iterations:",i,")"
    return t        

# end of reverse_vo2()

#### ---- main () -----

url = os.environ['QUERY_STRING']
params = url.split('&')

token = {}
for i in params:
    x = i.split('=')
    token.update({x[0]: x[1]})

print "Content-Type: text/html"
print ""
print "<HTML><BODY>"

print token['TYPE'],"<BR>\n"

if token['TYPE'] == 'RESULT':
    dist = int(token['DISTANCE'])
    time = token['HOUR']+':'+token['MINS']+':'+token['SECS']
    print "VDOT =", daniels(dist, time)

if token['TYPE'] == 'VDOT':
    vo2m = float(token['VO2MAX'])
    dist = 10000 # token['DISTANCE'] 
    print "Time = ", reverse(int(dist), float(vo2m))


print "</BODY></HTML>"

