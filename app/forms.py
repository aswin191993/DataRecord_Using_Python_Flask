from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,TextField,PasswordField,IntegerField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class EnteryForm(Form):
    student = StringField('student', validators=[DataRequired()])
    mark = IntegerField('mark', validators=[DataRequired()])
