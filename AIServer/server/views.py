# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template
from server import app

@app.route("/")
def strftime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.route("/words", methods=["GET"])
def similar_words():
    pass

@app.route("/key", methods=["GET"])
def extract_keyword():
    pass

@app.route("/freq", methods=["GET"])
def word_frequency():
    pass