#!/usr/bin/python3

from flask import Flask, request, Response
import requests
import os, sys

### subs() ####

def header():
    return '<HTML>\n\t<HEAD>\n\t</HEAD>\n<BODY>\n'

def footer():
    return '</BODY>\n</HTML>'

def body():

    bodytext = 'This is the body<BR>'
    r = requests.get('http://localhost:8080/json.app')
    bodytext += r.text # json returns dict

    return bodytext

### __main__() ###

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
def index_html():

    ret_text = ''.join([header(), body(), footer()])

    response = Response(response=ret_text,
                        status=200,
                        mimetype="text/html")

    return response

@app.route('/json.app', methods=['GET'])
def json_app():

    ret_text = '{ "Key": "Value" }'

    response = Response(response=ret_text,
                        status=200,
                        mimetype="application/json")

    return response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
