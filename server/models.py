
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt


class Video(db.Model, SerializerMixin):
    __tablename__ = "videos"

    serialize_rules = ("-reviews.video","-user.videos",)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    video_url=db.Column(db.String)
    views = db.Column(db.Integer)
    publish_at = db.Column(db.DateTime,server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
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

    serialize_rules = ("-reviews.user","-videos.user","-_password_hash",)
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String, unique=True, nullable=False)
    _password_hash =db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    videos =  db.relationship('Video',backref='user')
    
    reviews = db.relationship('Review', backref='user')
    # videos = db.relationship('Video',secondary=video_user,back_populates='users')
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('password hash encry password and cannot be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authentcate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.enocde('utf-8'))


    def __repr__(self):
        return f'<user {self.id}: {self.username}>'