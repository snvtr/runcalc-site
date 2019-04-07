#!/usr/bin/python3

"""
vdot json server gets either:
- distance+time or 
- VDOT as input 
and returns:
- a json with VDOT for a given distance+time
- a list of times for a bunch of distances for a given VDOT
"""

from flask import Flask, request, Response
import os, sys, math

## __subs__() ###

def daniels(distance, time):
    """ the main function, converts distance+time to VDOT """

#    time_parts = time.split(':')
# in minutes
#    duration = float(time_parts[0]) * 60 + float(time_parts[1]) + (float(time_parts[2]) / 60)
# metres per minute
    duration = float(str_to_time(time))
    velocity = float(distance) / duration

# returns vo2max for given distance in meters and time in minutes      
    return round((-4.60 + 0.182258 * velocity + 0.000104 * math.pow(velocity,2)) / (0.8 + 0.1894393 * math.exp(-0.012778 * duration) + 0.2989558 * math.exp(-0.1932605 * duration)),2)

def get_function(race_d,race_t,race_VDOT):
    """ a helper funtion for newton approximation """

    upper = 0.000104 * race_d**2 * race_t**-2 + 0.182258 * race_d * race_t**-1 - 4.6
    lower = 0.2989558 * math.exp(-0.1932605*race_t) + 0.1894393 * math.exp(-0.012778*race_t) + 0.8

    return (upper/lower - float(race_VDOT))

def get_derivative(race_d,race_t,race_VDOT):
    """ a helper funtion for newton approximation """

    upper = ((((0.2989558*math.exp(-0.1932605*race_t))+(0.1894393*math.exp(-0.012778*race_t))+0.8)*((-0.000208)*(race_d**2)*(race_t**-3))-((0.182258)*race_d*(race_t**-2)))-(race_VDOT*((0.2989558)*(math.exp(-0.1932605*race_t))+(0.1894393)*(math.exp(-0.012778*race_t)))))
    lower = (0.2989558 * math.exp(-0.1932605 * race_t) + 0.1894393 * math.exp(-0.012778 * race_t) + 0.8)**2
    return (upper/lower)

def reverse(distance, VDOT):
    """
    Reverse function for daniels(), gets time based on VDOT and distance.
    It approximates the output based on Newton approximation
    
    >>> reverse(5000, 30)
    30.68
    """

    time = 60

    if time <= 50000:
        time = 250

    if time <= 42200:
        time = 220

    if time <= 21100:
        time = 110

    if time <= 10000:
        time = 50

    if time <= 5000:
        time = 25

    if time <= 3000:
        time = 12

    function   = get_function (float(distance), float(time), float(VDOT))
    derivative = get_derivative (float(distance), float(time), float(VDOT)) 

    i = 0

    while abs(function/derivative) > 0.000001:
   
        i = i + 1

        if i > 100:
            break

        time = time - function/derivative

        function   = get_function (float(distance), float(time), float(VDOT))
        derivative = get_derivative (float(distance), float(time), float(VDOT))
# returns time in minutes for given distance and VO2max
    return round(time, 2)

# end of reverse_vo2()

def time_to_str(time):
    """
    >>> time_to_str(123.45)
    02:03:27
    """

    hours = time // 60
    secs, mins  = math.modf(time - hours*60)
    secs = round(secs*60)
# returns formatted string built from minutes
    return '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs))

def str_to_time(time_str):
    """
    >>> str_to_time('02:03:27')
    123.45
    """

    time_parts = time_str.split(':')

# returns duration in minutes
    return round(float(time_parts[0]) * 60 + float(time_parts[1]) + (float(time_parts[2]) / 60), 2)


def build_json_vdot(distances, vdot):

    json_parts = []
    
    for dist in distances.keys():
        json_parts.append('"'+str(distances[dist])+'": "'+time_to_str(reverse(dist, vdot))+'"')
    
    return '{' + ','.join(json_parts) + '}'

def build_json_dist_time(dist, dist_time):

    return '{ "VDOT" : "' + str(daniels(dist, dist_time)) + '"}'

### __main__() ###

app = Flask('vdot json app')

@app.route('/vdot.app', methods=['GET'])
def vdot_app():
    """ returns json to the main server
    
    for distance/time returns json_text = '{ "VDOT": "29.35" }'
    for VDOT returns json_text = '{ "3000": "12:00:00", "5000": "20:00:00" }' etc
    """
    distances = [800, 1000, 1500, 1609.34, 2000, 2414.02, 
                 3000, 3218.69, 4828.03, 5000,
                 8046.72, 10000, 15000, 20000, 21097, 30000, 42195]

    distances = {
                 '800' :     '800m',
                 '1000' :    '1000m',
                 '1500' :    '1500m',
                 '1609.34' : '1 mile',
                 '2000' :    '2000m',
                 '2414.02' : '1.5 miles',
                 '3000' :    '3000m',
                 '3218.69' : '2 miles',
                 '4828.03' : '3 miles',
                 '5000' :    '5 km',
                 '8046.72' : '5 miles',
                 '10000' :   '10 km',
                 '15000' :   '15 km',
                 '20000' :   '20 km',
                 '21097' :   'Half-marathon',
                 '30000' :   '30 km',
                 '42195' :   'Marathon'
                }

    if request.args.get('distance') is not None:
        json_text = build_json_dist_time(request.args.get('distance'), request.args.get('time_hour')+':'+request.args.get('time_mins')+':'+request.args.get('time_secs'))

    if request.args.get('VDOT') is not None:
        json_text = build_json_vdot(distances, request.args.get('VDOT'))

    response = Response(response=json_text,
                        status=200,
                        mimetype="application/json")

    return response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)
