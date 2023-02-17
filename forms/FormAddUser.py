from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class FormAddUser(FlaskForm):
    plus = SelectField(label='Plus Access?', validators=[DataRequired()], choices=[('true', 'Yes'), ('false', 'No')], default='false', description='Should the user have access to the Plus API?')
    userid = StringField('User ID', validators=[DataRequired()], description= "The user's ID. This is the ID that will be used to identify the user in the API. This can be any string, but it is recommended to use a unique ID such as a Discord ID or a UUID.")
    username = StringField('Username', validators=[DataRequired()], description="The user's username. This is the name that will be displayed in the API. This can be any string, but it is recommended to use the user's Discord username or some other name attached to another platform.")
    submit = SubmitField('Submit')