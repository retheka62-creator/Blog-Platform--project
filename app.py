from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)


def get_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(app.config['DATABASE']):
        conn = get_db()
        with open('database.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()


@app.route('/')
def home():
    return redirect('/dashboard')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = get_db()

        conn.execute(
            'INSERT INTO users(username,email,password) VALUES(?,?,?)',
            (
                request.form['username'],
                request.form['email'],
                generate_password_hash(request.form['password'])
            )
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db()

        user = conn.execute(
            'SELECT * FROM users WHERE email=?',
            (request.form['email'],)
        ).fetchone()

        conn.close()

        if user and check_password_hash(
            user['password'],
            request.form['password']
        ):
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/dashboard')
def dashboard():
    conn = get_db()

    posts = conn.execute('''
        SELECT posts.*, users.username,
        (SELECT COUNT(*) FROM likes WHERE likes.post_id=posts.id) as like_count
        FROM posts
        JOIN users ON posts.user_id=users.id
        ORDER BY created_at DESC
    ''').fetchall()

    conn.close()

    return render_template('dashboard.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        conn = get_db()

        conn.execute('''
            INSERT INTO posts(title,content,category,user_id)
            VALUES(?,?,?,?)
        ''', (
            request.form['title'],
            request.form['content'],
            request.form['custom_category'] if request.form['category'] == 'Other' else request.form['category'],
            session['user_id']
        ))

        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template('create_post.html')


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    conn = get_db()

    if request.method == 'POST':
        conn.execute('''
            INSERT INTO comments(comment,post_id,user_id)
            VALUES(?,?,?)
        ''', (
            request.form['comment'],
            id,
            session['user_id']
        ))
        conn.commit()

    post = conn.execute('''
        SELECT posts.*, users.username
        FROM posts
        JOIN users ON posts.user_id=users.id
        WHERE posts.id=?
    ''', (id,)).fetchone()

    comments = conn.execute('''
        SELECT comments.*, users.username
        FROM comments
        JOIN users ON comments.user_id=users.id
        WHERE post_id=?
    ''', (id,)).fetchall()

    conn.close()

    return render_template(
        'view_post.html',
        post=post,
        comments=comments
    )


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()

    if request.method == 'POST':
        conn.execute(
            'UPDATE posts SET title=?, content=? WHERE id=?',
            (
                request.form['title'],
                request.form['content'],
                id
            )
        )

        conn.commit()
        conn.close()

        return redirect('/dashboard')

    post = conn.execute(
        'SELECT * FROM posts WHERE id=?',
        (id,)
    ).fetchone()

    conn.close()

    return render_template('edit_post.html', post=post)


@app.route('/like/<int:id>')
def like(id):
    conn = get_db()

    conn.execute(
        'INSERT INTO likes(user_id,post_id) VALUES(?,?)',
        (session['user_id'], id)
    )

    conn.commit()
    conn.close()

    return redirect('/dashboard')


@app.route('/profile')
def profile():
    conn = get_db()

    user = conn.execute(
        'SELECT * FROM users WHERE id=?',
        (session['user_id'],)
    ).fetchone()

    posts = conn.execute(
        'SELECT * FROM posts WHERE user_id=?',
        (session['user_id'],)
    ).fetchall()

    conn.close()

    return render_template(
        'profile.html',
        user=user,
        posts=posts
    )


if __name__ == '__main__':
    init_db()
    app.run(debug=True)