from app import app, db
from flask import render_template, request, redirect, url_for

from flask_app.app.models import User, Post, Comment


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.timestamp.desc()).all()
    return render_template('profile.html', user=user, posts=posts)

@app.route('/feed')
def feed():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('feed.html', posts=posts)

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return redirect(url_for('feed'))
    users = User.query.filter(User.username.like('%' + query + '%')).all()
    return render_template('search.html', users=users)

@app.route('/post', methods=['POST'])
def post():
    author = request.form['author']
    body = request.form['body']
    post = Post(author=author, body=body)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('feed'))

@app.route('/comment', methods=['POST'])
def comment():
    author = request.form['author']
    body = request.form['body']
    post_id = request.form['post_id']
    post = Post.query.get(post_id)
    comment = Comment(author=author, body=body, post=post)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('feed'))
