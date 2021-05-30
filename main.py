# This is a sample Python script.

from measure_similarity import *

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/display/<name>')
def display(name):
   return ('The similarity is  %s' % name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      text1 = request.form['nm1']
      text2 = request.form['nm2']


      val = similarity(text1, text2)
      #print (val)
      return redirect(url_for('display',name = val))


if __name__ == '__main__':
   app.run(debug = True)