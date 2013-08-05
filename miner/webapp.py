from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, Response
import json
import miner


app = Flask(__name__)
app.config.from_object('fl_config')


@app.route('/miner')
def mineData():
    mq = request.args.get('mongo_query')
    data = miner.mineData(mq)
    r = Response(response=data, status=200,  mimetype="application/json")
    return r


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
