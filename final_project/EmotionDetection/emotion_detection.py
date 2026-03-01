import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
        emotions_list = list(emotions_dict.keys())
        anger_score = emotions_dict['anger']
        disgust_score = emotions_dict['disgust']
        fear_score = emotions_dict['fear']
        joy_score = emotions_dict['joy']
        sadness_score = emotions_dict['sadness']
        emotions = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        max_value = max(emotions)
        dominant_emotion = emotions_list[emotions.index(max_value)]
        emotions_dict['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotions_dict = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    return emotions_dict