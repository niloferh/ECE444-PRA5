import pytest
import json
from pathlib import Path

from application import application

news_samples = ["Aliens have been found living in Antarctica",
                "Justin Trudeau steps down as prime minister",
                "A category 3 hurricane hit Florida on October 9 2024",
                "Geoffrey Hinton won the nobel prize in physics"]

base_url = "http://serve-sentiment-env.eba-xw6junau.us-east-2.elasticbeanstalk.com"

@pytest.fixture
def client():
    with application.app_context():
        yield application.test_client()  # tests run here

def fake_news_1(client):
    """Helper function for test_fake_news_1"""
    return client.get(f"{base_url}/fake-news?query={news_samples[0]}", content_type="html/text")

def fake_news_2(client):
    """Helper function for test_fake_news_2"""
    return client.get(f"{base_url}/fake-news?query={news_samples[1]}", content_type="html/text")

def real_news_1(client):
    """Helper function for test_real_news_1"""
    return client.get(f"{base_url}/fake-news?query={news_samples[2]}", content_type="html/text")

def real_news_2(client):
    """Helper function for test_real_news_2"""
    return client.get(f"{base_url}/fake-news?query={news_samples[3]}", content_type="html/text")

@pytest.mark.fake_news_1
def test_fake_news_1(client, benchmark):
    """Test that a news input is correctly identified as fake."""
    response = benchmark.pedantic(fake_news_1, args=(client,), iterations=1, rounds=100)

    assert response.status_code == 200
    assert b"This news is fake." in response.data

@pytest.mark.fake_news_2
def test_fake_news_2(client, benchmark):
    """Test that a news input is correctly identified as fake."""
    response = benchmark.pedantic(fake_news_2, args=(client,), iterations=1, rounds=100)

    assert response.status_code == 200
    assert b"This news is fake." in response.data

@pytest.mark.real_news_1
def test_real_news_1(client, benchmark):
    """Test that a news input is correctly identified as real."""
    response = benchmark.pedantic(real_news_1, args=(client,), iterations=1, rounds=100)

    assert response.status_code == 200
    assert b"This news is real." in response.data

@pytest.mark.real_news_2
def test_real_news_2(client, benchmark):
    """Test that a news input is correctly identified as real."""
    response = benchmark.pedantic(real_news_2, args=(client,), iterations=1, rounds=100)

    assert response.status_code == 200
    assert b"This news is real." in response.data