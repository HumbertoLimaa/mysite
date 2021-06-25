#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import requests
import json
from pandas import DataFrame
import pandas as pd
import utils


def sensor():
    utils.getJson()


sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor, 'interval', minutes=0.2)
sched.start()

app = Flask(__name__)


@app.route("/")
def home():
    """ Function for test purposes. """
    sensor()
    return "Welcome Home :) !"


if __name__ == "__main__":
    app.run()
    #app.run(debug=True, use_reloader=True, port=5000, host='0.0.0.0')
