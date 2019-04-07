from flask import Flask

app = Flask('running calculators')
app.config.from_object('config')

from app import views