#!/usr/bin/env python3.6
from flask import Flask, jsonify

app = Flask(__name__)

#textual address request
@app.route('/address/<address>', methods=['GET'])
def getAddress(address):
    from controller.controller import get_data  # get resource from controller
    return jsonify(get_data(address))


if __name__ == "__main__":
    app.run(debug=True)  # Do not use debug in production deployment
