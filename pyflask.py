#------------------------------------------------------------------
# Developer ----- Bryce Martin 
# Description --- This program will get me familiar with using
#                 python and flask for web applications. I will
#                 utilize this program for a personal portfolio
#------------------------------------------------------------------

#importing flask object from flask library
#render template will import am html file into our function
#the html files must be stored in a folder called 'templates'
from flask import Flask, render_template

# creating an instance '__name__" = "__main__"
app = Flask(__name__)

#this / means the homepage: this line is the url
@app.route('/')

#this function will map its contents to the @app.route
def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)