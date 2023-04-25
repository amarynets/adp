import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_main(client):
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ping(client):
    url = reverse('ping')
    response = client.get(url)
    assert response.json() == {'ping': 'pong'}
