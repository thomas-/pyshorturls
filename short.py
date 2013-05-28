#!/usr/bin/env python

import json
import os
from shortuuid import uuid
from flask import Flask, abort, redirect, render_template, request, escape
app = Flask(__name__)

urls = 'urls/'


def short_to_full(short):
    with open(os.path.join(urls, short)) as f:
        return f.readline()


def generate_short_url():
    short = uuid()
    return short


@app.route("/")
def index():
    return render_template('index.htm')


@app.route("/<short>")
def go(short):
    try:
        url = short_to_full(short)
    except IOError as e:
        abort(404)
    print url
    return redirect(url)


@app.route('/new/', methods=['POST'])
def new():
    url = escape(request.form['url'])
    short = escape(request.form['short'])
    print short
    if not short:
        short = generate_short_url()
    path = os.path.join(urls, short)
    if os.path.isfile(path):
        return "shorturl already exists"
    try:
        with open(path, 'w+') as f:
            f.write(url)
    except:
        abort(503)
    return "ok\n" + short


@app.route("/admin/")
def admin():
    return "admin page"

if __name__ == "__main__":
    app.run(debug=True)
