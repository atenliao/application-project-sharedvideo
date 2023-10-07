#!/usr/bin/env python3

# Standard library imports
from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
# from flask import Flask, request, make_response
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask import Flask
# from flask_cors import CORS
# from flask_bcrypt import Bcrypt
# from flask_restful import Api
# Remote library imports
# from flask import request
# from flask_restful import Resource
# from models import db
# Local imports
from config import app, db, api
# Add your model imports

# from config import app, db, api
from models import Video, User, Review

# Views go here!
# app = Flask(__name__)
# app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False


# migrate = Migrate(app, db)

# api = Api(app)

# bcrypt = Bcrypt(app)
# # Instantiate CORS
# CORS(app)
# db.init_app(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

