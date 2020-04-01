import os
from flask import Flask, redirect

app = Flask(__name__)

# Tutti i messaggi vengono salvati qui da add_message e poi organizzati da get_all_messages
messages = []

# Chiamata da send_message
def add_message(username, message):
    messages.append("{}: {}".format(username, message))

# Chiamata da user
def get_all_messages():
    return "<br>".join(messages)

# Appare atterrando nel sito
@app.route('/')
def index():
    return "To send a message use /USERNAME/MESSAGE"

# La funzione finale che appare sullo schermo
@app.route('/<username>') 
def user(username):
    return "<h1>Hi {0}</h1>{1}".format(username, get_all_messages())

# Prende l'input dell'utente e lo inserisce nella lista tramite add_message, poi rinfresca la pagina
@app.route('/<username>/<message>') # Il testo all'interno delle <> viene passato come argomento nella funzione decorata
def send_message(username, message): 
    add_message(username, message)
    return redirect("/" + username)

app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)