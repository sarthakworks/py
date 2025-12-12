# Python Basics Project

This is a personal python project exploring basic libraries like `pyjokes` and `pyttsx3`.

## Prerequisites

Before you begin, ensure you have **Python 3.x** installed on your system.
You can verify this by running:
```bash
python --version
# or
python3 --version
```

## 🚀 Up and Running

Follow these steps to get the project running on your local machine:

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Run the Code
Now you are ready to run the script!
```bash
python basics1.py
```

## Output
You should see:
- The terminal screen clear.
- A random joke printed in **yellow**.
- A list of files in the current directory printed in **green**.

## Troubleshooting
- If you see errors related to `pyttsx3`, ensure you have the necessary audio drivers installed for your OS.
