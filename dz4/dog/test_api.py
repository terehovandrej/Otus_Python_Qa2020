import pytest


@pytest.mark.parametrize('breed, subbreed', [('boxer', []),
                                             ('bullterrier', ['staffordshire']),
                                             ('corgi', ['cardigan']),
                                             ('collie', ['border']),
                                             ('frise', ['bichon'])
                                             ])
def test_api_get_subbred_by_breed(api_client, breed, subbreed):
    res = api_client.get(path = f"/breed/{breed}/list")
    assert res['message'] == subbreed


@pytest.mark.parametrize('breed', ['boxer',
                                   'bullterrier',
                                   'corgi',
                                   'collie'])
def test_api_get_random_image_from_breed(api_client, breed):
    res = api_client.get(path = f"/breed/{breed}/images/random")
    assert f"https://images.dog.ceo/breeds/{breed}" in res['message']


def test_api_get_random_image(api_client):
    res = api_client.get(path = "/breeds/image/random")
    assert "https://images.dog.ceo/breeds/" in res['message']


@pytest.mark.parametrize('breed', ['boxer',
                                   'bullterrier',
                                   'corgi',
                                   'collie'])
def test_api_get_random_multiply_image_from_breed(api_client, breed):
    res = api_client.get(path = f"/breed/{breed}/images/random/3")
    assert len(res['message']) == 3


@pytest.mark.parametrize('breed, subbreed', [
    ('bullterrier', 'staffordshire'),
    ('corgi', 'cardigan'),
    ('collie', 'border'),
    ('frise', 'bichon')])
def test_api_get_single_random_image_from_subbreed(api_client, breed, subbreed):
    res = api_client.get(path = f"/breed/{breed}/{subbreed}/images/random")
    assert f"https://images.dog.ceo/breeds/{breed}-{subbreed}/" in res['message']
