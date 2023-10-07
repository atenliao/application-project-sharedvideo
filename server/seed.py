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
        'https://www.youtube.com/watch?v=xc6vJ6T1N3o&list=RDxc6vJ6T1N3o&start_radio=1',
        'https://www.youtube.com/watch?v=Wv2G20Yeepk',
        'https://www.youtube.com/watch?v=j6B5lj3XRPg',
        'https://www.youtube.com/watch?v=oa-88Ge0XuY',
        'https://www.youtube.com/watch?v=xojsezpWiRI',
        'https://www.youtube.com/watch?v=IawwUQP8ztI',
        'https://www.youtube.com/shorts/7bnOIOFvNs4',
        'https://www.youtube.com/watch?v=MGw5HgdzFS8',
        'https://www.youtube.com/watch?v=q7y4av-Dr4I',
        'https://www.youtube.com/watch?v=H8nERjGhpPk',
        'https://www.youtube.com/watch?v=IBz5Vv520KA',
        'https://www.youtube.com/watch?v=-cod185uLAg',
        'https://www.youtube.com/watch?v=Z0dD_M-WEOs',
        'https://www.youtube.com/watch?v=Pj5B1JZ3u_o',
        'https://www.youtube.com/watch?v=RX8ohg31Nek',
        'https://www.youtube.com/watch?v=adC48qZ8p5Y'

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
        video_url = random.choice(videos_url)
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
