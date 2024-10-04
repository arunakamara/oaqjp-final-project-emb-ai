'''
Importing Flask and other important libraries
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detector():
    '''
    The detector function
    '''

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    #Error Handling
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': \
     {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': \
     {joy} and 'sadness': {sadness}. The dominant emotion is \
     {dominant_emotion}."

@app.route("/")
def index():
    '''
    The index render method
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
