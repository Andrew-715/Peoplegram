from flask import Flask, render_template, jsonify, request

import logger
import utils

log = logger.get_logger()
app = Flask(__name__)


@app.route('/')
def page_index():
    posts = utils.load_posts()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:pk>')
def page_posts(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.load_comments(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/api/post')
def api_index():
    posts = utils.load_posts()
    log.info(f'api_index - > {len(posts)}')
    return jsonify(posts)


@app.route('/api/post/<int:pk>')
def api_posts(pk):
    post = utils.get_post_by_pk(pk)
    log.info(f'api_posts - > {pk}')
    return jsonify(post)


@app.route('/search/')
def post_search():
    word = request.args.get('s', '').lower()
    posts = utils.load_posts(search_word=word)
    return render_template('index.html', posts=posts)


@app.route('/user/<user_name>')
def post_search_user_name(user_name):
    posts = utils.load_posts(user_name=user_name)
    return render_template('index.html', posts=posts)


@app.errorhandler(500)
def server_error(e):
    return '500 не волнуйся'


@app.errorhandler(404)
def not_found(e):
    return '404 не волнуйся'


if __name__ == '__main__':
    app.run()
