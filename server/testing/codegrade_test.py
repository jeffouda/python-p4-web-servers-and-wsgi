from werkzeug.test import Client
from server.werkzeug_app import application


def test_wsgi_response():
    client = Client(application)
    response = client.get("/")
    assert response.status_code == 200
    assert b"A WSGI generated this response!" in response.data
