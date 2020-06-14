from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired


class Edit(FlaskForm):
    access=PasswordField('Access Code',validators=[DataRequired()])
    information_block = StringField('Information Block',validators=[DataRequired()])
    attribute = StringField('Attribute', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Delete(FlaskForm):
    access=PasswordField('Access Code',validators=[DataRequired()])
    information_block = StringField('Information Block',validators=[DataRequired()])
    attribute = StringField('Attribute', validators=[DataRequired()])
    submit = SubmitField('Submit')

