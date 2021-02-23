from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/adress/<adress>', methods=['GET'])
def getAdress(adress):
    from controller.controller import get_data # get ressources from conroller
    return jsonify(get_data(adress))

if __name__ == "__main__":
    app.run(debug=True) #Do not use debug in production deployment

