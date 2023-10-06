class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    serialize_rules = ('-video.reviews', '-user.reviews',)

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Review {self.id}: {self.comment}'
