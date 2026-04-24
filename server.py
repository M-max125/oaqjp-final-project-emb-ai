from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the input text and returns a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')


    response = emotion_detector(text_to_analyze)


    if response is None:
        return "Invalid text! Please try again."


    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
