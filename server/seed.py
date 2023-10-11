#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import random
# Local imports
from app import app
from models import db, Video, User, Review


fake = Faker()

with app.app_context():
    print("Delete all records...")
    Video.query.delete()
    User.query.delete()
    fake = Faker()

    print("Creating users")

    users= []
    usernames = []
    videos_url = [
        'https://www.youtube.com/watch?v=wcVnbnazVw4',
        'https://www.youtube.com/watch?v=pRpeEdMmmQ0',
        'https://www.youtube.com/watch?v=Wv2G20Yeepk',
        'https://www.youtube.com/watch?v=j6B5lj3XRPg',
        'https://www.youtube.com/watch?v=oa-88Ge0XuY',
        'https://www.youtube.com/watch?v=xojsezpWiRI',
        'https://www.youtube.com/watch?v=IawwUQP8ztI',
        'https://www.youtube.com/watch?v=9GCRa9vO4Uw',
        'https://www.youtube.com/watch?v=MGw5HgdzFS8',
        'https://www.youtube.com/watch?v=q7y4av-Dr4I',
        'https://www.youtube.com/watch?v=H8nERjGhpPk',
        'https://www.youtube.com/watch?v=IBz5Vv520KA',
        'https://www.youtube.com/watch?v=-cod185uLAg',
        'https://www.youtube.com/watch?v=Z0dD_M-WEOs',
        'https://www.youtube.com/watch?v=Pj5B1JZ3u_o',
        'https://www.youtube.com/watch?v=RX8ohg31Nek',
        'https://www.youtube.com/watch?v=adC48qZ8p5Y',
        'https://www.youtube.com/watch?v=ZP4gie6zVUA',
        'https://www.youtube.com/watch?v=kyTHWopOZ6Q',
        'https://www.youtube.com/watch?v=KrLj6nc516A',
        'https://www.youtube.com/watch?v=2O-9RmuiXog',
        'https://www.youtube.com/watch?v=3w_svY7zTQM',
        'https://www.youtube.com/watch?v=eXw54_C7AM4',
        'https://www.youtube.com/watch?v=BGzGPyUKS1Q',
        'https://www.youtube.com/watch?v=LI4uj9ulHQc',
        'https://www.youtube.com/watch?v=muUL8kOqeyE',
        'https://www.youtube.com/watch?v=NaptDLqIiU8',
        'https://www.youtube.com/watch?v=Tp9qaP4RQZE',
        'https://www.youtube.com/watch?v=79DijItQXMM',
        'https://www.youtube.com/watch?v=PLPGIknFh54',
        'https://www.youtube.com/watch?v=xpCkCBoIrnA',

    ]
    for i in range(20):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name() # create a new username
        usernames.append(username)

        user = User(
            username = username,
            image_url = fake.url(),
        )
        user.password_hash = user.username +'PASSWORD'
        users.append(user)
    db.session.add_all(users)

    print("Create videos...")
    videos = []
    for i in range(20):
        views = fake.pyint(0,100)
        video_url = videos_url[i]
        video = Video(
            title=fake.sentence(),
            video_url=video_url,
            views=views,
        )

        video.user = rc(users)
        videos.append(video)
    
    db.session.add_all(videos)

    db.session.commit()
    print("Complete.")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
