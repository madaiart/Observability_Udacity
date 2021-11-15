from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash

from prometheus_flask_exporter import PrometheusMetrics
import logging

logging.info("Setting LOGLEVEL to INFO")
logging.basicConfig(level=logging.INFO)

# Server configuration
app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")

# Home route
@app.route('/')
def homepage():
    return render_template("main.html")

# Testing Health
@app.route('/healthz')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    return response

if __name__ == "__main__":
    app.run()