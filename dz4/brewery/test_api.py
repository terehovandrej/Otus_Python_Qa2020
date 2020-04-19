import pytest


@pytest.mark.parametrize('brew_id, name', [('5949', 'Stickmen Brewery'),
                                           ('44', 'Trim Tab Brewing'),
                                           ('127', 'Dragoon Brewing Co'),
                                           ('219', 'Wren House Brewing Company'),
                                           ('225', 'Brick Oven Pizza Co / Brick & Forge Brewing')
                                           ])
def test_api_get_brewery_by_id(api_client, brew_id, name):
    res = api_client.get(path = f"/{brew_id}")
    assert res['name'] == name


@pytest.mark.parametrize('city', ['Anchorage',
                                  'Lake Havasu City',
                                  'Paragould', ]
                         )
def test_api_filter_brewery_by_city(api_client, city):
    res = api_client.get(path = f"?by_city={city}")
    for brewery in res:
        assert brewery['city'] == city


@pytest.mark.parametrize('name', ['Diamond Bear Brewing Co',
                                  'SanTan Brewing Co - Uptown Chandler',
                                  'Bad Water Brewing']
                         )
def test_api_filter_brewery_by_name(api_client, name):
    res = api_client.get(path = f"?by_name={name}")
    for brewery in res:
        assert brewery['name'] == name


@pytest.mark.parametrize('state', ['Arizona',
                                   'Arkansas',
                                   'Alabama', ]
                         )
def test_api_filter_brewery_by_state(api_client, state):
    res = api_client.get(path = f"?by_state={state}")
    for brewery in res:
        assert brewery['state'] == state


@pytest.mark.parametrize('postal_code', ['35222-1932',
                                         '85382-7434',
                                         '72114-5381', ]
                         )
def test_api_filter_brewery_by_postal(api_client, postal_code):
    res = api_client.get(path = f"?by_postal={postal_code}")
    for brewery in res:
        assert brewery['postal_code'] == postal_code
