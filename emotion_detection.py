"""Emotion detection using the IBM Watson NLP EmotionPredict service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]


class EmotionDetectionError(Exception):
    """Raised whenever emotion detection cannot be completed."""


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and the dominant emotion for the text.

    Raises EmotionDetectionError if the input is empty or the service
    call fails or returns unexpected data.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        raise EmotionDetectionError("Input text must not be empty.")

    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
    except requests.exceptions.RequestException as error:
        raise EmotionDetectionError(f"Request to Watson NLP failed: {error}") from error

    if response.status_code == 400:
        raise EmotionDetectionError(
            "Watson NLP rejected the input (HTTP 400). Please provide valid text."
        )

    if response.status_code != 200:
        raise EmotionDetectionError(
            f"Watson NLP returned HTTP status {response.status_code}."
        )

    try:
        scores = response.json()["emotionPredictions"][0]["emotion"]
        result = {name: float(scores[name]) for name in EMOTIONS}
    except (ValueError, KeyError, IndexError, TypeError) as error:
        raise EmotionDetectionError("Unexpected response from Watson NLP.") from error

    # The dominant emotion is the one with the highest score.
    result["dominant_emotion"] = max(EMOTIONS, key=lambda name: result[name])
    return result
