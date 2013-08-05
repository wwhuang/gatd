from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import json
import miner

app = Flask(__name__)
app.config.from_object('fl_config')

@app.route('/miner')
def mineData():
    mq = request.args.get('mongo_query')
    data = miner.mineData(mq)
    return json.dumps(data)
