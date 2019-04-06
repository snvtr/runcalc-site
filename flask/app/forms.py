from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class MainForm(FlaskForm):
    distance  = TextField('distance', validators = [Required()])
    time_hour = TextField('time_hour', validators = [Required()])
    time_mins = TextField('time_mins', validators = [Required()])
    time_secs = TextField('time_mins', validators = [Required()])
