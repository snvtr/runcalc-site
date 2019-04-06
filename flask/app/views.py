#!/usr/bin/python3

from flask import render_template, request, redirect
from app import app
from app.forms import MainForm
import requests
import os, sys

### __subs__() ####


### __main__() ###

@app.route('/', methods=['GET','POST'])
def index_html():

    mainform = MainForm()

#    req = requests.get('http://localhost:7070/vdot.app')

    if mainform.validate_on_submit():
        vdotjson = 'Distance:' + mainform.distance.data + 'm, time:' + mainform.time_hour.data + ':' + mainform.time_mins.data + ':' + mainform.time_secs.data
        return render_template('index.html', title='Home', vdotjson=vdotjson, form=mainform)

    return render_template('index.html', title='Home', vdotjson=vdotjson, form=mainform)
