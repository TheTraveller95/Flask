import os
import json
from flask import Flask, render_template #import the Flask class from flask

app = Flask(__name__) #create an instance of this and store it in a variable called app. The first argument of the Flask class 
#is the name of the application module

@app.route('/') #every time we click on home (in the html file in the <a href="/">) the function will be called
def index():
    return render_template("index.html")

@app.route('/about') #every time we click on about (in the html file in the <a href="/about">) the function will be called. 
#The /about is the part at the end of the URL https://5000-b6f190f4-42e4-44aa-af61-84dae5b4a63a.ws-eu01.gitpod.io/about
def about():
    data = []
    with open('data/company.json', 'r') as json_data # 'r' stays for 'reading'
    data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) #in order to creat a for loop put this code inside the return() company=data list_of_number = [1, 2, 3]

@app.route('/contact')  #every time we click on about (in the html file in the <a href="/contact">) the function will be called. 
#The /about is the part at the end of the URL https://5000-b6f190f4-42e4-44aa-af61-84dae5b4a63a.ws-eu01.gitpod.io/contact
def contact():
    return render_template('contact.html', page_title="Contact")

@app.route('/career')  #every time we click on about (in the html file in the <a href="/career">) the function will be called. 
#The /about is the part at the end of the URL https://5000-b6f190f4-42e4-44aa-af61-84dae5b4a63a.ws-eu01.gitpod.io/career
def career():
    return render_template('career.html', page_title="Careers")

if __name__ == "__main__": #__name__ is the name of the default module on python. is the first one that we run
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True) # debug = True can be put only during the test period. When we need to submit the project debug has to be = False

            
