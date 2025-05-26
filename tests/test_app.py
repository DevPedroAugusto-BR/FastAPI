from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_olaMundo(client):
    response = client.get("/Batatinha")  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Hello World"}  # Assert


def test_create_user_deve_retornar_201_e_usuario_criado(client):
    response = client.post(
        "/users/",
        json={  # Act
            "username": "Pedro",
            "email": "Pedro@gmail.com",
            "password": "123456",
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        "id": 1,
        "username": "Pedro",
        "email": "Pedro@gmail.com",
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        "user": [
            {
                "id": 1,
                "username": "Pedro",
                "email": "Pedro@gmail.com",
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "Tester",
            "email": "thisIsATest@test.com",
            "password": "123456",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        "id": 1,
        "username": "Tester",
        "email": "thisIsATest@test.com",
    }


def test_update_user_deve_retornar_404_quando_usuario_nao_existe(client):
    response = client.put(
        "/users/1000", json={"username": "Tester", "email": "test@test.com"}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert
    assert response.json() == {"detail": "User not found"}  # Assert


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.NO_CONTENT  # Assert
    assert response.json() == {
        "id": 1,
        "username": "Tester",
        "email": "test@test.com",
    }


def test_delete_user_deve_retornar_404_quando_usuario_nao_existe(client):
    response = client.delete("/users/1000")

    assert response.status_code == HTTPStatus.NOT_FOUND  # Assert
    assert response.json() == {"detail": "User not found"}  # Assert
