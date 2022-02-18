from os import link
from flask import Flask, render_template, request, redirect, session
from dojo import Dojo

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/process', methods=['POST'])
# def process():
#     session['your_name'] = request.form['your_name']
#     session['location'] = request.form['location']
#     session['language'] = request.form['language']
#     session['comment'] = request.form['comment']
#     return redirect('/result')

@app.route('/result/<int:dojo_id>')
def result(dojo_id):
    return render_template("results.html", dojo=Dojo.get_one({'id':dojo_id}))


@app.route('/create', methods=['POST'])
def create_dojo():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    dojo_id = Dojo.save(request.form)
    return redirect(f"/result/{dojo_id}")

if __name__ == "__main__" :
    app.run(debug=True)