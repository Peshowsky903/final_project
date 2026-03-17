"""
Flask server for Emotion Detection application.
Handles routing and integrates with emotion detection module.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles emotion detection requests from user input.
    Returns formatted emotion analysis or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    # Handle blank input case
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

