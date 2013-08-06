from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, Response
import json
import miner

import pymongo
import time
from bson.json_util import dumps


app = Flask(__name__)
app.config.from_object('fl_config')


@app.route('/miner')
def mineData():
    if request.get_json(silent=True):
        mq = json.loads(request.get_json())
        data = miner.mineData(mq)
    else:
        data = miner.mineData()

    r = Response(response=data, status=200,  mimetype="application/json")
    return r

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['localhost:6000'] = True
    app.run()
