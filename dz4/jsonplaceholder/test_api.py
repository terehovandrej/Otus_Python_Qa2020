import pytest


@pytest.mark.parametrize('photo_id, photo_url', [(1, 'https://via.placeholder.com/600/92c952'),
                                                 (2, 'https://via.placeholder.com/600/771796'),
                                                 (3, 'https://via.placeholder.com/600/24f355'),
                                                 (4, 'https://via.placeholder.com/600/d32776'),
                                                 (5, 'https://via.placeholder.com/600/f66b97')])
def test_api_get_photo_by_id(api_client, photo_id, photo_url):
    response = api_client.get(path = f"/photos/{photo_id}")
    assert response['url'] == photo_url


@pytest.mark.parametrize('post_id, title',
                         [(1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'),
                          (2, 'qui est esse'),
                          (3, 'ea molestias quasi exercitationem repellat qui ipsa sit aut'),
                          (4, 'eum et est occaecati'),
                          (5, 'nesciunt quas odio')])
def test_api_get_post_title_by_id(api_client, post_id, title):
    response = api_client.get(path = f"/posts/{post_id}")
    assert response['title'] == title


def test_api_create_post(api_client):
    res = api_client.post(
        path = "/posts",
        data = {'title': 'privet', 'body': 'lorem ipsum', 'userId': 228})
    assert res['title'] == 'privet'
    assert res['body'] == 'lorem ipsum'


def test_check_user_id_in_posts(api_client):
    res = api_client.get(
        path = "/posts?userId=5",
       )
    for post in res:
        assert post['userId'] == 5


@pytest.mark.parametrize('todo_id, status',
                         [(1, False),
                          (2, False),
                          (3, False),
                          (4, True),
                          (5, False)])
def test_api_check_todo_status_by_id(api_client, todo_id, status):
    response = api_client.get(path = f"/todos/{todo_id}")
    assert response['completed'] == status