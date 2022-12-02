from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit

from model.etat import Etat

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

@app.route('/start')
def start():
    return "coucou"

@app.route('/new_view')
def new_view():
    return render_template('new_view.html')

@socketio.on('connect')
def connect():
    print("conexion établie")

@socketio.on('newStory')
def newStory():
    emit("Story", {
        "base": 1,
        "cards": [
            {"etat": Etat.BASE, "texte": "texte de base", "previewGauche": "à gauche","previewDroite": "à Droite", "gauche": 2, "droite": 3, "explicGauche": 4, "explicDroite": 4},
            {"etat": Etat.FIN, "texte": "good", "previewGauche": "à gauche","previewDroite": "à Droite", "gauche": None, "droite": None, "explicGauche": None, "explicDroite": None},
            {"etat": Etat.FIN, "texte": "bad", "previewGauche": "à gauche","previewDroite": "à Droite", "gauche": None, "droite": None, "explicGauche": None, "explicDroite": None}
        ]
    })


if __name__ == "__main__":
    # socketio.run(app, host='127.0.0.1', port=8080)
    socketio.run(app, host="127.0.0.1", port=5000, debug= True)