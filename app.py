from importlib.resources import path
import os
from flask import Flask, render_template, request
import os, pickle
import numpy as np
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
