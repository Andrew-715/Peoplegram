import json


def load_data(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        posts = json.load(file)
    return posts


def load_posts(search_word=None, user_name=None):
    posts = load_data(r'data\posts.json')

    if search_word:
        posts = filter(lambda x: search_word in x['content'].lower(), posts)

    if user_name:
        posts = filter(lambda x: user_name == x['poster_name'].lower(), posts)
    return posts


def load_comments(posts_pk):
    all_comments = load_data(r'data/comments.json')
    comments = []

    for comment in all_comments:
        if comment['post_id'] == posts_pk:
            comments.append(comment)
    return comments


def get_post_by_pk(pk):
    posts = load_posts()

    for post in posts:
        if pk == post['pk']:
            return post
