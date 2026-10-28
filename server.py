"""Flask web service for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from emotion_detection import EmotionDetectionError, emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Show the web page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect():
    """Analyze the submitted text and return the emotion scores as JSON."""
    data = request.get_json(silent=True) or {}
    text = data.get("text")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Please provide some text to analyze."}), 400

    try:
        return jsonify(emotion_detector(text))
    except EmotionDetectionError as error:
        return jsonify({"error": str(error)}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
