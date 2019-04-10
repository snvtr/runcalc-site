#!/usr/bin/python3

from flask import render_template, request, redirect
from app import app
from app.forms import VDOTForm, ReverseVDOTForm, CooperForm, BalkeForm
import requests
import os

### __subs__() ###


### __main__() ###

json_srv_host = os.environ.get('JSON_SRV_HOST', default='localhost')
json_srv_port = os.environ.get('JSON_SRV_PORT', default='7070')

@app.route('/', methods=['GET','POST'])
@app.route('/index.html', methods=['GET','POST'])
@app.route('/vdot.html', methods=['GET','POST'])
def vdot():

    mainform = VDOTForm()

    if mainform.validate_on_submit():
        req_str = (''.join(['http://',json_srv_host,':',json_srv_port,
                   '/vdot.app?distance=',mainform.distance.data,
                   '&time_hour=',mainform.time_hour.data,
                   '&time_mins=',mainform.time_mins.data,
                   '&time_secs=',mainform.time_secs.data
                  ]))
        req = requests.get(req_str)
        return render_template('vdotform.html', title='VDOT from results', vdotjson=req.json(), form=mainform)

    return render_template('vdotform.html', title='Home', vdotjson='', form=mainform)

@app.route('/reverse.html', methods=['GET','POST'])
def reverse():

    mainform = ReverseVDOTForm()

    if mainform.validate_on_submit():
        req_str = ''.join(['http://',json_srv_host,':',json_srv_port,'/vdot.app?VDOT=',mainform.vdot.data])
        req = requests.get(req_str).json()

        TempList = []
        for i in req.keys():
            TempDict = { 'distance': i, 'time': req[i] }
            TempList.append(TempDict)

        return render_template('reversevdotform.html', title='results from VDOT', vdotjson=TempList, form=mainform)

    return render_template('reversevdotform.html', title='results from VDOT', vdotjson='', form=mainform)

@app.route('/cooper.html', methods=['GET','POST'])
def cooper():

    mainform = CooperForm()

    if mainform.validate_on_submit():
        req_str = ''.join(['http://',json_srv_host,':',json_srv_port,'/cooper.app?distance=',mainform.distance.data])
        req = requests.get(req_str).json()

        cooper = req['VO2max Cooper']
        cooper_indian_mod = req['VO2max Cooper Indian Mod']

        return render_template('cooperform.html',
                                title='Cooper 12 min VO2max test',
                                cooper=cooper,
                                cooper_indian_mod=cooper_indian_mod,
                                form=mainform)

    return render_template('cooperform.html',
                           title='Cooper 12 min VO2max test',
                           cooper='',
                           cooper_indian_mod='',
                           form=mainform)

@app.route('/balke.html', methods=['GET','POST'])
def balke():

    mainform = BalkeForm()

    if mainform.validate_on_submit():
        req_str = ''.join(['http://',json_srv_host,':',json_srv_port,'/balke.app?distance=',mainform.distance.data])
        req = requests.get(req_str).json()

        balke = req['VO2max Balke']

        return render_template('balkeform.html',
                                title='Balke 15 min VO2max test',
                                balke=balke,
                                form=mainform)

    return render_template('balkeform.html',
                           title='Balke 15 min VO2max test',
                           balke='',
                           form=mainform)
