from flask import Flask, render_template, flash, redirect, url_for
from flask_cors import CORS
from forms import FoodForm, ChoiceForm
import backend_functions

app = Flask(__name__)
CORS(app)

import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "blah-blah"
app.config.from_object(Config)


@app.route("/", methods=["GET", "POST"])
def home():
    form = FoodForm()
    # receive data
    if form.is_submitted():
        # get food choices
        food_choices = backend_functions.get_recipes(form.food.data)
        #backend_functions.printStuff(food_choices)
        #food_names = []
        #for i,c in food_choices:
        #    food_names.append(c)
        #backend_functions.printStuff(food_names)
        # load next page
        choiceForm = ChoiceForm()
        # receive data
        if choiceForm.validate_on_submit():
            # get recipe
            #backend_functions.printStuff(food_names)
            #index = int(choiceForm.choice.data)
            food_string = choiceForm.choice.data.replace(" ", "_")
            #backend_functions.printStuff(food_names)
            #backend_functions.printStuff(food_string)
            result = backend_functions.print_food(food_string)
            # load results
            return render_template("results.html", result=result)
        return render_template("choices.html", choiceForm=choiceForm, options=food_choices)
    return render_template("home.html", title="ZotYum", form=form)
