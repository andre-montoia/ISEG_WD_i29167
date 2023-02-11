from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    header_img = db.Column(db.String(100), nullable=False, default='default_header.jpg')
    background_color = db.Column(db.String(7), nullable=False, default='#FFFFFF')
    font_style = db.Column(db.String(20), nullable=False, default='Arial')

    def __repr__(self):
        return f'User({self.username})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Post({self.content})'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    upvotes = db.Column(db.Integer, nullable=False, default=0)
    downvotes = db.Column(db.Integer, nullable=False, default=0)
    emoji_reactions = db.Column(db.String(20), nullable=False, default='')

    def __repr__(self):
        return f'Comment({self.content})'
