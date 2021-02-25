# !/usr/local/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

# textual address request
@app.route('/address/<address>', methods=['GET'])
def networkCoverage(address):
    # get resource from controller
    from controllers.controller import get_data
    return jsonify(get_data(address))

if __name__ == "__main__":
    # Do not use debug in production deployment
    app.run(debug=True)
