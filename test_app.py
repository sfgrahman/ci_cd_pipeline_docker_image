from app import app


def test_home():
    response=app.test_client.get("/")

    assert response.status_code==2000
    assert response.data == b"Hellow World"