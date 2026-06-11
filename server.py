from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    return str(response)

@app.route("/")
def render_index_page():
    return "Emotion Detection Application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
