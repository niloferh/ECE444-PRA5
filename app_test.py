import pytest
import json
from pathlib import Path

from application import application

news_samples = ["Aliens have been found living in Antarctica",
                "Justin Trudeau steps down as prime minister",
                "A category 3 hurricane hit Florida on October 9 2024",
                "Geoffrey Hinton won the nobel prize in physics"]

@pytest.fixture
def client():
    with application.app_context():
        yield application.test_client()  # tests run here


def test_fake_news_1(client):
    """Test that a news input is correctly identified as fake."""
    response = client.get(f"/fake-news?query={news_samples[0]}", content_type="html/text")

    assert response.status_code == 200
    assert b"This news is fake." in response.data

def test_fake_news_2(client):
    """Test that a news input is correctly identified as fake."""
    response = client.get(f"/fake-news?query={news_samples[1]}", content_type="html/text")

    assert response.status_code == 200
    assert b"This news is fake." in response.data

def test_real_news_1(client):
    """Test that a news input is correctly identified as real."""
    response = client.get(f"/fake-news?query={news_samples[2]}", content_type="html/text")

    assert response.status_code == 200
    assert b"This news is real." in response.data

def test_real_news_2(client):
    """Test that a news input is correctly identified as real."""
    response = client.get(f"/fake-news?query={news_samples[3]}", content_type="html/text")

    assert response.status_code == 200
    assert b"This news is real." in response.data