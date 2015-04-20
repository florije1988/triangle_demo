# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_triangle import Triangle

app = Flask(__name__)
Bootstrap(app)
Triangle(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
