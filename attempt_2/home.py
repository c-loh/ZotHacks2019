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
        # load next page
        choiceForm = ChoiceForm()
        # receive data
        if choiceForm.validate_on_submit():
            # get recipe
            food_string = choiceForm.choice.data.replace(" ", "_")
            result = backend_functions.print_food(food_string)
            ### tryna add youtube stuff
            food_name = choiceForm.choice.data
            url = backend_functions.build_search_url(food_name)
            answer = backend_functions.get_result(url)
            table = backend_functions.addlist(answer)
            backend_functions.printStuff(table)
            result.append("\nYouTube Vidoes\n")
            for name,link,thumbnail in table:
                line = name + ": " + link + "\."
                result.append(line)
            ###
            # load results
            return render_template("results.html", result=result)  # maybe add a redirect to home?
        return render_template("choices.html", choiceForm=choiceForm, options=food_choices)
    return render_template("home.html", title="ZotYum", form=form)
