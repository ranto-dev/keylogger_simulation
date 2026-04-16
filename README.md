# 🛡️ Educational Keylogger Simulation

A lightweight **proof-of-concept** project designed for academic demonstrations. This project illustrates how modern web-based keyloggers function by intercepting keystrokes and storing them on a remote server.

### ⚠️ Ethical Warning & Disclaimer

**This project is for educational purposes only.** Unauthorized use of keyloggers on systems without explicit permission is illegal and unethical. This simulation is intended to help students and security professionals understand attack vectors to better build defenses.

### 🏗️ Project Architecture

The simulation is divided into two primary components:

| Component    | Technology                | Role                                                                             |
| :----------- | :------------------------ | :------------------------------------------------------------------------------- |
| **Frontend** | HTML5 / CSS3 / JavaScript | Simulates a legitimate banking login page. Contains the "hook" (event listener). |
| **Backend**  | Python / Flask            | Acts as the attacker's server, receiving and storing intercepted data.           |

### 🛠️ Features

- **Real-time Interception:** Captures keystrokes via JavaScript `keydown` events before the form is even submitted.
- **Persistent Storage:** Automatically creates a hidden log file (`.hidden_log.txt`) to save data for later analysis.
- **Asynchronous Exfiltration:** Uses the `fetch` API to send data to the server without reloading the page, making the attack invisible to the user.
- **UX Simulation:** Features a functional login modal that displays "Success" or "Error" messages to maintain the illusion of a real site.

### 🚀 Installation & Usage

#### 1. Prerequisites

Ensure you have **Python 3.x** installed. You will need the following libraries:

```bash
pip install -r requirements.txt
```

#### 2. Running the Simulation

1.  **Start the Attacker Server:**

    ```bash
    python app.py
    ```

    The server will start listening on `http://127.0.0.1:5000`.

2.  **Open the Victim Page:**
    Open `index.html` in any modern web browser (Chrome, Firefox, Edge).

3.  **Interact:**
    Type into the input fields. Observe the Python terminal to see the keystrokes appearing in real-time.

### 🔍 How it Works

1.  **The Capture:** The JavaScript `addEventListener` monitors the entire document for keyboard input.
2.  **The Exfiltration:** Every character is packaged into a `POST` request and sent to the Flask `/log` endpoint.
3.  **The Storage:** The Python backend filters special keys (like `Enter` or `Backspace`) and appends the strings to a local text file.

### 🛡️ Mitigation & Defense

To protect against this type of attack:

- **Use MFA (Multi-Factor Authentication):** Even if the password is stolen, the attacker cannot access the account without the second factor.
- **Password Managers:** Auto-filling credentials bypasses the need for physical typing, rendering most keyloggers useless.
- **CORS Policies:** Properly configured Content Security Policies (CSP) can prevent browsers from sending data to unauthorized third-party servers.
