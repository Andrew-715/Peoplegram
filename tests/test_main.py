from main import app
from pytest import fixture


@fixture()
def posts_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


@fixture()
def client():
    return app.test_client()


def test_index(client):
    response = client.get('/api/post')

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_posts(client, posts_keys):
    response = client.get('/api/post/1')

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == posts_keys
