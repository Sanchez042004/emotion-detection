"""
Este módulo contiene la función emotion_detector, que envía un texto
al servicio Watson NLP EmotionPredict y devuelve las puntuaciones de
emoción junto con la emoción dominante.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analiza el texto proporcionado y devuelve un diccionario con las
    puntuaciones de las emociones (anger, disgust, fear, joy, sadness)
    y la emoción dominante.

    Nota: la función devuelve la respuesta ya parseada y formateada
    como un diccionario de Python (no el texto crudo de
    response.text). El texto crudo del servicio Watson NLP se
    convierte internamente con json.loads(response.text) y luego se
    reestructura en el diccionario de salida.

    Si el texto de entrada no es válido (el servicio responde con
    código de estado 400), todos los valores se devuelven como None.
    
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers, timeout=10)

    # Manejo de errores: texto en blanco o inválido -> código 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    formatted_output = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

    return formatted_output