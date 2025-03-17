# VOXA - WhatsApp Messaging Virtual Assistant

VOXA is a Python-based voice assistant that automates sending WhatsApp messages on macOS. It utilizes speech recognition to take voice inputs and automates message sending using PyAutoGUI.

---

## Features

- Voice-based interaction for hands-free operation.
- Automatically sends messages to contacts from an Excel file.
- Uses fixed screen coordinates for precise automation.

---

## Requirements

- Python 3.13
- [Virtual Environment](https://docs.python.org/3/tutorial/venv.html)

---

## Python Packages:
- `pyttsx3`
- `speechrecognition`
- `pyautogui`
- `pandas`
- `pillow`

---

## Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Setting Up the Project
1. **Clone the Project:**
```bash
git clone <repo-url>
cd VOXA
```

2. **Create and Activate Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Auto-activate Virtual Environment in VSCode:**
- Ensure the `.env` file is present with:
```bash
VIRTUAL_ENV=./venv
PATH=$VIRTUAL_ENV/bin:$PATH
```
Restart VSCode for the settings to apply.

4.  **Install Requirements:**
```bash
pip install -r requirements.txt
```

5. **Configure User Details:**
Edit the `config.json` file:
```json
{
    "USERNAME": "YourName",
    "BOTNAME": "VOXA"
}
```

6. **Prepare Contact List:**
Edit `Contacts.xlsx` and add your contacts with the column name for names.

---

## Finding Screen Coordinates
1. **Run the Demo Script:**
- Execute the following command to find screen coordinates for UI elements:
```bash
python demo.py
```

2. **Hover Mouse Over Desired UI Element:**
- Within 5 seconds, move your mouse to the desired element (like the WhatsApp search bar or contact area).
- The script will print the coordinates in the terminal.

3. **Update Coordinates in Code:**
- Replace the placeholder coordinates in VOXA.py with the captured ones:
`search_bar_x`, `search_bar_y` for the search bar.
`first_contact_x`, `first_contact_y` for the contact selection.

---

## Running VOXA
1. **Activate the virtual environment (if not auto-activated):**
```bash
source venv/bin/activate
```
2. **Start the assistant with:**
```bash
python VOXA.py
```
3. **Commands:**
- Say `send message` to initiate sending a WhatsApp message.
- Say `exit` or `bye` to terminate the assistant.
- Deactivating the Virtual Environment
```bash
deactivate
```
---

## Troubleshooting
- `Module Not Found Error`: Ensure you're inside the virtual environment.
- `Pillow/Screen Errors`: Ensure Pillow is installed and properly configured.
- `Coordinate Errors`: Re-run demo.py to update coordinates if the UI layout changes.

---

## License
This project is licensed under the MIT License.
