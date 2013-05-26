#!/usr/bin/env python

import json
import os
from flask import Flask, abort, redirect
app = Flask(__name__)

urls = 'urls/'


def short_to_full(short):
    with open(os.path.join(urls, short)) as f:
        return json.load(f)['url']


@app.route("/")
def index():
    return "tinyurl service"


@app.route("/<short>")
def go(short):
    try:
        url = short_to_full(short)
    except IOError as e:
        print e
        abort(404)
    print url
    return redirect(url)


@app.route("/admin/")
def admin():
    return "admin page"

if __name__ == "__main__":
    app.run(debug=True)
