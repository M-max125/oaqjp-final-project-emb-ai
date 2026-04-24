import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }


    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        # 1. Extract the emotion dictionary from the JSON response
        formatted_response = response.json()

        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # 2. Assign scores to specific variables
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # 3. Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # 4. Return the rsults
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    return None