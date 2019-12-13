import os
from flask import Flask #import the Flask class from flask

app = Flask(__name__) #create an instance of this and store it in a variable called app. The first argument of the Flask class 
#is the name of the application module

@app.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__": #__name__ is the name of the default module on python. is the first one that we run
    app.run(host=os.environ.get("IP"),
            port=(os.environ.get("PORT")),
            debug=True)

            
