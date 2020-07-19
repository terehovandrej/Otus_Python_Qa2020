def test_main_page(browser, base_url):
    browser.get(base_url)
    assert browser.title == 'Your Store'
