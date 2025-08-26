#**************** IMPORT PACKAGES ********************
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import warnings
warnings.filterwarnings("ignore")
import os

from model import Algo

#***************** FLASK *****************************
app = Flask(__name__)

# class main:
#    def __init__(self):


@app.route('/',methods=['GET'])

def about():
   return render_template('index.html')

@app.route('/Analyze',methods=['GET','GET'])
def analyze():
   return render_template('analyze.html')

@app.route('/Contact',methods=['GET','GET'])
def contact():

   return render_template('contact.html')

@app.route('/Analyze_img',methods=['GET','GET'])
def analyse():
   return render_template('analyse.html')

@app.route('/Result',methods = ['POST','GET'])
def result():
   #if request.method == 'POST':
   f = request.files['file']
   name = f.filename
   # path = 'static/'+name
   # print(path)

   obj = Algo(name)
   pred_s = obj.cnn_algo()
   print(pred_s)
   # pred_s= ["hi",69]
   return render_template('result.html',preds=pred_s)



if __name__ == '__main__':
   app.run(debug=True)
