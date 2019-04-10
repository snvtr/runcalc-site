from flask import Flask

app = Flask('Various running calculators')
app.config.from_object('config')

from app import mainsrv