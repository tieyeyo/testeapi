from flask import Flask, jsonify
import jwt


app = Flask(__name__)
app.config['DEBUG'] = True


login_v = input("Login:")
password_v = input("Password:")


def users():

   login = 'joana@gmail.com'
   password = '123456'


@app.route('/', methods=['GET'])
def home():
    encoded_jwt = jwt.encode({"só":"teste"}),
    if login_v == login and password_v == password:
        print


app.run()
