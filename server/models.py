from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-videodatabases.user","_password_hash",)
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String, unique=True, nullable=False)
    _password_hash =db.Column(db.String)
    video_url=db.Column(db.String)

    videodatabases = db.relationship("Video", backref="user")




class Video(db.Model, SerializerMixin):
    __tablename__ = "videos"

    serialize_rules = ("-user.videos")

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer)
    publish_at = db.Column(db.DataTime,server_default=db.func.now())


class Review(db.Model,SerializerMixin):
    __tablename__ = "reviews"

    id == db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DataTime, server_default=db.func.now())
    updated_at = db.Column(db.DataTime, onupdate=db.func.now())

    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Review {self.id}: {self.comment}>'
