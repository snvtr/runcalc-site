#!/usr/bin/python3

"""
 vdot сервер должен получать дистанцию+время, либо VDOT и в ответ отдавать
 либо VDOT либо список дистанций-времен
"""

from flask import Flask, request, Response
import os, sys

### subs() ####

def make_json():

    jsontext = ''

    return jsontext

### __main__() ###

app = Flask('vdot json app')

@app.route('/vdot.app', methods=['GET'])
def vdot_app():
    """ отдает результаты в виде json основному серверу """

    # если есть distance - тогда считаем VDOT
    # если есть vdot - тогда считаем набор дистанций

    json_text = '{ "VDOT": "29.35" }'
    # либо:
    #json_text = '{ "3000": "12:00:00" }'

    response = Response(response=json_text,
                        status=200,
                        mimetype="application/json")

    return response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
