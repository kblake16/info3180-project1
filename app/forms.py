from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField,StringField,SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    rooms = StringField('No. of Rooms',validators=[DataRequired()])
    bath = StringField('No. of Bathrooms',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    propType = SelectField('Property Type',choices = [('House','House'),('Apartment','Apartment')],validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(["jpeg","jpg","png"], 'Images only!')])