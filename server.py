"""
Este módulo implementa una aplicación web basada en Flask para
detectar emociones en un texto, utilizando la función emotion_detector
del paquete EmotionDetection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Endpoint que recibe el texto a analizar a través del parámetro
    'textToAnalyze', invoca la función de detección de emociones y
    devuelve una respuesta formateada. Si el texto es inválido o está
    en blanco, devuelve un mensaje de error.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Renderiza la página principal de la aplicación."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
