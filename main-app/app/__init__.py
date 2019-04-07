from flask import Flask

app = Flask('running and weightlifting calculators')
app.config.from_object('config')

from app import views