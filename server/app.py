#!/usr/bin/env python3

# Standard library imports
from flask import request, session,jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import app, db, api

from models import Video, User, Review


class Signup(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)


    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        image_url = request_json.get('image_url')

        user = User(
            username = username,
            image_url = image_url
        )
        user.password_hash = password

        print('user post ')
        try:
            print('here!')
            db.session.add(user)
            db.session.commit()

            session['user_id']= user.id
            print(user.to_dict())
            return user.to_dict(), 201

        except IntegrityError:
            print("no,here!")
            return {'error':'422 Unprocessable Entity'},422

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict(), 200

        return {'error':'401 Unauthorized'}, 401


class Login(Resource):
    def post(self):
        request_json = request.get_json()
        username = request_json.get('username')
        password = request_json.get('password')
        user = User.query.filter(User.username == username).first()


        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
        
        return {'error': '401 Unauthorized'}, 401


class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None

            return {'message':'delete successfuly'}, 204

        return {'error': '401 Unauthorized'}, 401

class VideoIndex(Resource):
    def get(self):
        
        videos = [video.to_dict() for video in Video.query.all()]
        return make_response(jsonify(videos),201)

class VideoIndexByUserID(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return [video.to_dict() for video in user.videos], 200

        return {'error':'401 Unauthorized'}, 401

    def post(self):
        if session.get('user_id'):
            request_json = request.get_json()
            title = request_json.get('title')
            video_url = request_json.get('video_url')
           
            try:
                video = Video(
                    title = title,
                    video_url = video_url,
                    user_id = session['user_id'],
                )

                db.session.add(video)
                db.session.commit()

                return video.to_dict(), 201
            except IntegrityError:
                return {'error':'422 Unprocessable Entity'}, 422

        return {'error':'401 Unauthorized'}, 401

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession,'/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(VideoIndexByUserID,'/videos_userid', endpoint='videos_userid')
api.add_resource(VideoIndex,'/videos',endpoint='videos')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

