from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from scores.models import Score


@pytest.mark.django_db
def test_leaderboard_endpoint():
    user = User.objects.create_user(username="testuser", password="pass")

    Score.objects.create(user=user, game="chess", score=100)

    client = APIClient()
    client.login(username="testuser", password="pass")

    response = client.get("/api/analytics/leaderboard/")
    assert response.status_code == 200


# Create your tests here.
