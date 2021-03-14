# Tests using pytest-flask lib

def test_app_is_created(app):
    assert app.name == 'app'


def test_config_is_loaded(config):
    assert config['DEBUG'] == False


def test_request_return_200(client):
    assert client.get('/').status_code == 200
