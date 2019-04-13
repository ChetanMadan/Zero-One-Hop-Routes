
# importing flask module fro
from flask import Flask, render_template,request
from find_routes import check_hops
# initializing a variable of Flask
app = Flask(__name__)
import pandas as pd
import numpy as np

# decorating index function with the app.route with url as /login
@app.route('/')
def index():
   return render_template('login.html')


trips = pd.read_csv('data/trips.txt')
stops = pd.read_csv('data/stops.txt')
routes = pd.read_csv('data/routes.txt')
stop_times = pd.read_csv('data/stop_times.txt')
@app.route('/FlaskTutorial',  methods=['POST'])
def success():

    if request.method == 'POST':
       startStop = request.form['Start']
       endStop = request.form['End']
       out = check_hops(startStop, endStop)
       if out[0]==0:
           return render_template('success.html', Start=startStop,End = endStop, Out=out[1], Hops = 0)
       elif out[0]==1:
           return render_template('success.html', Start=startStop,End = endStop, Out=out[1], Hops = 1)
       elif out[0]==-1:
           return render_template('success.html', Start=startStop,End = endStop, Out=out[1], Hops = 'Not possible')
    else:
       pass
if __name__ == "__main__":
   app.run()
