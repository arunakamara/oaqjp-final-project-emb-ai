import requests
import json

def emotion_detector(text_to_analyse):
    '''
    Emotion Detector method
    '''
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = header )
    formatted_response = json.loads(response.text)

    #Error Handling
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    #logic for dominant emotion
    emotions = [anger, disgust, fear, joy, sadness]
    max_value = max(emotions)
    index = emotions.index(max_value)
    
    if index == 0:
        dominant_emotion = 'anger'
    elif index == 1:
        dominant_emotion = 'disgust'
    elif index == 2:
        dominant_emotion = 'fear'
    elif index == 3:
        dominant_emotion = 'joy'
    elif index == 4:
        dominant_emotion = 'sadness'

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }