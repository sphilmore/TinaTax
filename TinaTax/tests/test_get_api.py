
def test_get_api(web_api):
    response = web_api.get_website()
    assert response.status_code == 200
    print(response.text)

