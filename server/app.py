#!/usr/bin/env python3

# Standard library imports
from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
# Remote library imports
# from flask import request
# from flask_restful import Resource
# from models import db
# Local imports
# from config import app, db, api
# Add your model imports

from config import app, db, api
from models import Video, User, Review

# Views go here!
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# migrate = Migrate(app, db)

# db.init_app(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

