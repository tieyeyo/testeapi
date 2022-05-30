from flask import Flask, jsonify, request, make_response, abort

from database import db
from users import USERS, usersEncoder

app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = usersEncoder


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'Status': 404, 'Error': 'Resource not found'}), 404)


@app.route('/home', methods=['GET'])
def home():
    return "<h1>API com Flask</h1>"


@app.route('/usuarios', methods=['GET'])
def lists():
    return jsonify({'USERS': db})

app.run()
