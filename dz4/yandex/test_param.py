def test_url_status(api_client, url, status_code):
    response = api_client.get()
    assert response.status_code == int(status_code)

