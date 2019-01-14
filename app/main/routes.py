from flask import render_template, request
from app.models import Post
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')


@bp.route('/about')
def about():
    return render_template('about.html', title='About Me')


@bp.route('/manifest')
def manifest():
    return render_template('manifest.html', title='Manifesto and Privacy Policy')


@bp.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(content_type=2).filter_by(published=True).order_by(Post.timestamp.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', title='Blog', posts=posts)


@bp.route('/projects')
def projects():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(content_type=1).filter_by(published=True).paginate(page=page, per_page=5)
    return render_template('projects.html', title='Projects', posts=posts)


@bp.route('/post/<int:post_id>/<slug>')
def post(post_id, slug):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
