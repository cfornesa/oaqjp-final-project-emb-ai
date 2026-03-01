import json

def emotion_detector(text):
    # Step 1: Assign input text to text_to_analyze (per requirement)
    text_to_analyze = text
    
    # Step 2: Call the emotion analysis API/service with text_to_analyze
    # (Replace the next line with actual call to your emotion detection service)
    # For demonstration, let's simulate a JSON response string:
    
    # Simulated JSON response (in real case, replace this with actual API call)
    json_response = '''
    {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.0,
        "joy": 0.8,
        "sadness": 0.05
    }
    '''
    
    # Step 3: Convert JSON string response to dictionary
    response_dict = json.loads(json_response)
    
    # Step 4: Extract required emotions
    emotions = {
        'anger': response_dict.get('anger', 0),
        'disgust': response_dict.get('disgust', 0),
        'fear': response_dict.get('fear', 0),
        'joy': response_dict.get('joy', 0),
        'sadness': response_dict.get('sadness', 0)
    }
    
    # Step 5: Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    # Step 6: Return the dictionary as required
    return emotions