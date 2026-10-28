from unittest.mock import Mock, patch

import pytest
import requests

from emotion_detection import EmotionDetectionError, emotion_detector

# A sample response in the same shape that Watson NLP returns.
SAMPLE_RESPONSE = {
    "emotionPredictions": [
        {
            "emotion": {
                "anger": 0.01,
                "disgust": 0.02,
                "fear": 0.03,
                "joy": 0.90,
                "sadness": 0.04,
            }
        }
    ]
}


def make_response(status_code=200, json_data=None):
    response = Mock()
    response.status_code = status_code
    response.json.return_value = json_data
    return response


@patch("emotion_detection.requests.post")
def test_result_format(mock_post):
    mock_post.return_value = make_response(200, SAMPLE_RESPONSE)
    result = emotion_detector("I am so happy today")
    assert set(result) == {
        "anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"
    }


@patch("emotion_detection.requests.post")
def test_dominant_emotion(mock_post):
    mock_post.return_value = make_response(200, SAMPLE_RESPONSE)
    result = emotion_detector("I am so happy today")
    assert result["joy"] == 0.90
    assert result["dominant_emotion"] == "joy"


@patch("emotion_detection.requests.post")
def test_http_error(mock_post):
    mock_post.return_value = make_response(500)
    with pytest.raises(EmotionDetectionError):
        emotion_detector("Some text")


@patch("emotion_detection.requests.post")
def test_http_400_error(mock_post):
    mock_post.return_value = make_response(400)
    with pytest.raises(EmotionDetectionError, match="HTTP 400"):
        emotion_detector("Some text")


@patch("emotion_detection.requests.post")
def test_request_exception(mock_post):
    mock_post.side_effect = requests.exceptions.ConnectionError("no network")
    with pytest.raises(EmotionDetectionError):
        emotion_detector("Some text")


@patch("emotion_detection.requests.post")
def test_empty_input(mock_post):
    with pytest.raises(EmotionDetectionError):
        emotion_detector("   ")
    mock_post.assert_not_called()
