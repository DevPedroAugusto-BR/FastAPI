from sqlalchemy import select

from learning_fastapi.models import User


def test_create_user(session):
    user = User(
        username="testuser", email="test@mail.com", password="patolino"
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == "test@mail.com")
    )  # Assert that the user was created successfully

    assert result.username == "testuser"
