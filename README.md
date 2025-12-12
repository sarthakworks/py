# Python MongoDB API Project

This is a Flask-based Python application that connects to a MongoDB Atlas database. It retrieves data from the `sample_mflix` database (specifically the `comments` collection) and serves it via an API.

## 1. How to Run Locally

Follow these steps to get the project up and running on your local machine if you are visiting this 10 years later!

### Prerequisites
- **Python 3.x** installed (`python --version` to check).
- **Git** installed.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/sarthakworks/py
    cd py
    ```

2.  **Create and Activate a Virtual Environment**
    It's best practice to use a virtual environment to isolate dependencies.
    
    *On macOS/Linux:*
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    
    *On Windows:*
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all required libraries listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup Environment Variables**
    Create a file named `.env` in the root directory (same level as `app.py`).
    Add your MongoDB connection string to it:
    ```bash
    MONGO_URI="mongodb+srv://sarthakbansal420_db_user:<password>@poc-cluster.4hgwesm.mongodb.net/?appName=POC-Cluster"

    ```
    replace password> with your actual password from MongoDB Atlas.
    *(See Section 2 & 4 on how to get this URI)*

5.  **Run the Application**
    Start the Flask server:
    ```bash
    python app.py
    ```
    or press cmd shift p and type select python interpreter and then select .venv python and then press run button

6.  **Verify**
    Open your browser and visit:
    -   Home: `http://localhost:5001/`
    -   Data: `http://localhost:5001/comments`

7.  **Live Demo**:
    -   [Deployed Comments API](https://sarthak-nohj.onrender.com/comments)

---

## 2. How to Access MongoDB Atlas Database

1.  **Login**: Go to [MongoDB Cloud](https://cloud.mongodb.com/) and log in.
2.  **Select Project**: Choose the project where your cluster is deployed.
3.  **Browse Collections**:
    -   Click on **Database** in the left sidebar.
    -   Click the **Browse Collections** button on your Cluster.
    -   Ensure you have the `sample_mflix` database loaded (if not, you can load sample datasets from the "..." menu on the cluster overview).
    -   Navigate to `sample_mflix` > `comments` to see your data.

---

## 3. How to Deploy (or Redeploy) on Render

To deploy this app from scratch on [Render](https://render.com/):

1.  **Dashboard**: Log in to your [Render Dashboard](https://dashboard.render.com/).
2.  **New Service**: Click **New +** and select **Web Service**.
3.  **Connect Repo**: Connect your GitHub/GitLab repository.
4.  **Configure Settings**:
    -   **Name**: Give your service a name.
    -   **Region**: Choose a region close to you (or your users).
    -   **Branch**: `main` (or your default branch).
    -   **Runtime**: **Python 3**.
    -   **Build Command**: `pip install -r requirements.txt`
    -   **Start Command**: `gunicorn app:app` (This matches the `Procfile`, but Render setup often asks for it explicitly).
5.  **Environment Variables**:
    -   Scroll down to the "Environment Variables" section.
    -   Key: `MONGO_URI`
    -   Value: Your full connection string (e.g., `mongodb+srv://user:pass@...`).
6.  **Deploy**: Click **Create Web Service**.

**Redeploying**:
-   **Manual**: Go to the service dashboard and click **Manual Deploy** > **Deploy latest commit**.
-   **Automatic**: Use the "Auto-Deploy" toggle in Settings to deploy on every git push.

---

## 4. IP Setup & Environment Variables (Credentials)

### A. How to take Username/Password from MongoDB Atlas (Credentials)
1.  **Database Access** (Left Sidebar in Atlas):
    -   Click **Database Access**.
    -   Click **+ Add New Database User**.
    -   **Username**: Enter a username (e.g., `sarthak`).
    -   **Password**: Click "Autogenerate Secure Password" (COPY THIS! You won't see it again) or type your own.
    -   **Privileges**: Select "Read and write to any database" (or specific privileges).
    -   Click **Add User**.
    -   *Use these credentials in your `MONGO_URI`.*

2.  **Get Connection String**:
    -   Go to **Database** (Cluster overview).
    -   Click **Connect**.
    -   Select **Drivers** (Python).
    -   Copy the connection string. It looks like:
        `mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`
    -   **Replace `<password>`** with the password you just created.

### B. How to Setup IP (Network Access)
**Important**: If the IP is not whitelisted, the connection will fail.

1.  **Network Access** (Left Sidebar in Atlas):
    -   Click **Network Access**.
    -   Click **+ Add IP Address**.
2.  **For Local Development**:
    -   Click **Add Current IP Address** (this adds your home/office IP).
    -   *Note: If your internet IP changes, you must update this.*
3.  **For Render Deployment**:
    -   Ideally, you should whitelist Render's IPs (which is hard as they change).
    -   **Easiest (but less secure)**: Click **Allow Access from Anywhere** (`0.0.0.0/0`). This effectively allows any IP (including Render) to try to connect (protected by your strong password).

---

## 5. Functionality of Important Files

### `.env` (Environment Variables)
-   **Purpose**: Stores secret keys and configuration locally.
-   **Why?**: You never want to commit passwords to GitHub. Use `.env` locally and `.gitignore` it.
-   **Format**: `KEY=VALUE`
-   **In Code**: We use `os.getenv('KEY')` (via `python-dotenv`) to read these.
-   **Production**: On Render/Heroku, you don't use the `.env` file; instead, you paste these values into the "Environment Variables" settings of the dashboard.

### `Procfile`
-   **Purpose**: Tells the cloud provider (Render/Heroku) how to start your app.
-   **Content**: `web: gunicorn app:app`
    -   `web`: It's a web process.
    -   `gunicorn`: A production-grade WSGI server (Python's built-in server is only for testing).
    -   `app:app`: Look in `app.py` for the object named `app`.

### `requirements.txt`
-   **Purpose**: Lists all Python libraries your project needs.
-   **Usage**: `pip install -r requirements.txt` installs them all at once.
-   **Creating**: Run `pip freeze > requirements.txt` to update it based on your current environment.

### `app.py`
-   **Purpose**: The main application file.
-   **What it does**:
    -   Connects to MongoDB using `pymongo`.
    -   Defines API routes (like `/` and `/comments`).
    -   Starts the Flask server.
