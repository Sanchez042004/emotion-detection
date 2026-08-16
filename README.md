# Emotion Detection Application

Este proyecto implementa una aplicación web que detecta emociones (ira, disgusto,
miedo, alegría y tristeza) en un texto de entrada, utilizando la biblioteca
Watson NLP de IBM. La aplicación está desplegada como un servicio web con Flask.

## Estructura del proyecto

- `EmotionDetection/` — Paquete Python con la lógica de detección de emociones.
  - `emotion_detection.py` — Función principal `emotion_detector`.
  - `__init__.py` — Convierte la carpeta en un paquete importable.
- `templates/index.html` — Interfaz web de la aplicación.
- `server.py` — Servidor Flask que expone la aplicación como servicio web.
- `test_emotion_detection.py` — Pruebas unitarias del paquete.
- `requirements.txt` — Dependencias del proyecto.

## Cómo ejecutar

```bash
pip install -r requirements.txt
python server.py
```

Luego visita `http://localhost:5000` en tu navegador.

## Cómo ejecutar las pruebas

```bash
python -m unittest discover -s . -p "test_*.py"
```

## Análisis estático de código

```bash
pylint server.py
```
