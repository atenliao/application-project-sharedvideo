
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from flask import Flask
from sqlalchemy import MetaData
# from app import bcrypt
# Local imports

# Instantiate app, set attributes


# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

# migrate = Migrate(app, db)
# db.init_app(app)

# Instantiate REST API




class Video(db.Model, SerializerMixin):
    __tablename__ = "videos"

    serialize_rules = ("-reviews.video",)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer)
    publish_at = db.Column(db.DateTime,server_default=db.func.now())

    # users = db.relationship('User',secondary=video_user,back_populates='videos')
    reviews = db.relationship('Review',backref='video')
    def __repr__(self):
        return f'video {self.id}: {self.title}'

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    # __table_args__= (db.CheckConstraint('LENGTH(review) >= 25'),)
    serialize_rules = ('-video.reviews','-user.reviews',)
    id = db.Column(db.Integer(), primary_key=True)
    comment = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'),)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),)

    def __repr__(self):
        return f'Review {self.id}: {self.comment}'


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-reviews.user",)
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String, unique=True, nullable=False)
    _password_hash =db.Column(db.String)
    video_url=db.Column(db.String)
    reviews = db.relationship('Review', backref='user')
    # videos = db.relationship('Video',secondary=video_user,back_populates='users')
    

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'