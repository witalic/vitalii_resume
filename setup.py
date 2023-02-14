# -*- coding: cp1251 -*-
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")

port = int(os.environ.get('PORT'))
app.run(host='0.0.0.0', port=33507)
