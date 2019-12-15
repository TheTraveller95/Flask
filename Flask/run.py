import os
from flask import Flask, render_template #import the Flask class from flask

app = Flask(__name__) #create an instance of this and store it in a variable called app. The first argument of the Flask class 
#is the name of the application module

@app.route('/') #every time we click on home (in the html file in the <a href="/">) the function will be called
def index():
    return render_template("index.html")

@app.route('/about') #every time we click on about (in the html file in the <a href="/about">) the function will be called
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__": #__name__ is the name of the default module on python. is the first one that we run
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True) # debug = True can be put only during the test period. When we need to submit the project debug has to be = False

            
