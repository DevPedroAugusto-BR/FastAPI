from http import HTTPStatus

from fastapi.testclient import TestClient

from learning_fastapi.app import app


def test_read_root_deve_retornar_ok_e_olaMundo():
    client = TestClient(app)  # Arrange
    response = client.get('/Batatinha')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Hello World"}  # Assert
