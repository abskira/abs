from flask import Flask, render_template_string
from prometheus_flask_exporter import PrometheusMetrics
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Compteur de visites simple
visits = 0

# Liste de messages créatifs
messages = [
    "Hello, je suis l'app d'Alioune !",
    "Bienvenue dans mon univers DevOps !",
    "Ici, on construit des pipelines en rêvant.",
    "Le code, c'est de la poésie.",
    "Jenkins, Docker, Grafana : la trilogie du cloud."
]

@app.route('/')
def home():
    global visits
    visits += 1
    msg = random.choice(messages)
    html = f"""
    <html>
    <head><title>Alioune's App</title></head>
    <body style="font-family: Arial; text-align: center; margin-top: 50px; background: #f0f0f0;">
        <h1 style="color: #ff6b6b;">✨ {msg} ✨</h1>
        <p>Cette page a été visitée <strong>{visits}</strong> fois.</p>
        <p>
            <a href="/about" style="margin-right: 15px;">À propos</a> |
            <a href="/metrics" style="margin-left: 15px; margin-right: 15px;">Métriques</a> |
            <a href="/health" style="margin-left: 15px;">Health</a>
        </p>
    </body>
    </html>
    """
    return html

@app.route('/about')
def about():
    return """
    <html>
    <body style="font-family: Arial; text-align: center; background: #f0f0f0;">
        <h2>À propos de cette application</h2>
        <p>Cette application a été créée dans le cadre d'un projet DevOps.</p>
        <p>Elle expose des métriques Prometheus pour être supervisée par Grafana.</p>
        <p>Le code est versionné sur GitHub et déployé automatiquement par Jenkins.</p>
        <p><a href="/">Retour</a></p>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "OK", "timestamp": time.time()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
