from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FoodForm(FlaskForm):
    food = StringField("Enter a food:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ChoiceForm(FlaskForm):
    choice = StringField("Choose an option (type name):", validators=[DataRequired()])
    submit = SubmitField("Find Recipe")
