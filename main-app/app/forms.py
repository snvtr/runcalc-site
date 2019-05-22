from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required

class VDOTForm(FlaskForm):
    distance  = TextField('distance',  validators = [Required()])
    time_hour = TextField('time_hour', validators = [Required()])
    time_mins = TextField('time_mins', validators = [Required()])
    time_secs = TextField('time_mins', validators = [Required()])

class ReverseVDOTForm(FlaskForm):
    vdot  = TextField('VDOT', validators = [Required()])

class CooperFormDist(FlaskForm):
    distance  = TextField('distance', validators = [Required()])

class CooperFormTime(FlaskForm):
    # this field needs to be split into min:sec
    str_time  = TextField('str_time', validators = [Required()])

class BalkeForm(FlaskForm):
    distance  = TextField('distance', validators = [Required()])
