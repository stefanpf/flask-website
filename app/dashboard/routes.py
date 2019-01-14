import os
import secrets
import json
from app import db
from app.dashboard import bp
from app.dashboard.forms import UpdateUserForm, PostForm
from app.models import User, Post
from datetime import datetime
from flask import current_app, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from PIL import Image
from slugify import slugify


@bp.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=10)
    return render_template('dashboard/dashboard.html', user=user, posts=posts)


@bp.route('/update_user', methods=['GET', 'POST'])
@login_required
def update_user():
    form = UpdateUserForm()
    if form.validate_on_submit():
        current_user.email = form.email.data.lower()
        hashed_password = generate_password_hash(form.password.data)
        current_user.password = hashed_password
        db.session.commit()
        flash('Your credentials have been updated.')
        return redirect(url_for('dashboard.dashboard'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('dashboard/update_user.html', title='Update Credentials', form=form)


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, content_type=form.post_type.data, published=form.published.data, slug=slugify(form.title.data))
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created.')
        return redirect(url_for('dashboard.dashboard'))
    return render_template('dashboard/create_post.html', title='New Post', form=form, legend='New Post')


@bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.content_type = form.post_type.data
        post.published = form.published.data
        post.slug = slugify(form.title.data)
        db.session.commit()
        flash('Your post has been updated!')
        return redirect(url_for('dashboard.dashboard'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.post_type.data = post.content_type
        form.published.data = post.published
    return render_template('dashboard/create_post.html', title='Update Post', form=form, legend='Edit Post')


@bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!')
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = secrets.token_hex(8) + extension
        with Image.open(file) as img:
            width, height = img.size
            if width > 700 or height > 500:
                maxsize = (700, 500)
                img.thumbnail(maxsize, Image.ANTIALIAS)
            img.save(os.path.join(current_app.root_path, 'static/media/img', f_name))
        return json.dumps({'filename': f_name})
