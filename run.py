import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "1234sucaremelapuoi" # Necessario per generare un ID
messages = [] # Tutti i messaggi vengono salvati qui da add_message e poi organizzati da get_all_messages

# Chiamata da send_message
def add_message(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {"timestamp": now, "from": username, "message": message}

    messages.append(message_dict)

# Appare atterrando sul sito
@app.route('/', methods = ["GET","POST"]) # Autorizza i metodi get e post in questa pagina
def index():
    if request.method == "POST": # Crea la session variable non appena viene premuto il bottone "Go to chat!"
        session["username"] = request.form["username"] # request.form ritorna una stringa dall'input di form da name = "username"
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

# La funzione finale che appare sullo schermo
@app.route('/<username>') 
def user(username):
    return render_template("chat.html", username = username, chat_messages = messages)

# Prende l'input dell'utente e lo inserisce nella lista tramite add_message, poi rinfresca la pagina
@app.route('/<username>/<message>') # Il testo all'interno delle <> viene passato come argomento nella funzione decorata
def send_message(username, message): 
    add_message(username, message)
    return redirect("/" + username)

app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)