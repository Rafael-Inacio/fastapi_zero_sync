from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_OK_e_ola_mundo():
    client = TestClient(app)  # Arrange(organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # assert (afirmação)
    assert response.json() == {'message': 'Olá, Mundo'}
