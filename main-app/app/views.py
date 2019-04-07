#!/usr/bin/python3

from flask import render_template, request, redirect
from app import app
from app.forms import VDOTForm, ReverseVDOTForm
import requests
import os, sys

### __subs__() ###


### __main__() ###

@app.route('/', methods=['GET','POST'])
@app.route('/index.html', methods=['GET','POST'])
@app.route('/vdot.html', methods=['GET','POST'])
def vdot():

    mainform = VDOTForm()

    if mainform.validate_on_submit():
        req_str = ('http://localhost:7070/vdot.app?distance=' + mainform.distance.data 
                 + '&time_hour=' + mainform.time_hour.data
                 + '&time_mins=' + mainform.time_mins.data
                 + '&time_secs=' + mainform.time_secs.data
                  )
        req = requests.get(req_str)
        return render_template('vdotform.html', title='VDOT from results', vdotjson='Here is the VDOT: '+req.text, form=mainform)

    return render_template('vdotform.html', title='Home', vdotjson='', form=mainform)

@app.route('/reverse.html', methods=['GET','POST'])
def reverse():

    mainform = ReverseVDOTForm()
    
    if mainform.validate_on_submit():
        req_str = 'http://localhost:7070/vdot.app?VDOT=' + mainform.vdot.data
        req = requests.get(req_str)
        return render_template('reversevdotform.html', title='results from VDOT', vdotjson='Here are the results: '+req.text, form=mainform)
            
    return render_template('reversevdotform.html', title='results from VDOT', vdotjson='', form=mainform)
