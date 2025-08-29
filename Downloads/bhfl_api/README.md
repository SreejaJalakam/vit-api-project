# BFHL API Application

This repository contains a full-stack application with a Python Flask backend and a simple HTML/CSS/JavaScript frontend. The backend exposes a REST API at `/bfhl` that processes an array of mixed data types and returns categorized and manipulated data.

## Project Structure

- `backend/`: Contains the Flask API.
    - `app.py`: The main Flask application file.
    - `requirements.txt`: Python dependencies for the Flask app.
- `frontend/`: Contains the static files for the web interface.
    - `index.html`: The main HTML file with the input form and response display.
    - `script.js`: JavaScript logic to interact with the API.
    - `style.css`: Custom CSS (currently empty, Tailwind CSS CDN is used).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file.

## Features

The API (POST `/bfhl`) takes a JSON body with a `data` array and returns:
- `is_success`: Boolean indicating operation status.
- `user_id`: Formatted as `{full_name_ddmmyyyy}`.
- `email`: A hardcoded email address.
- `roll_number`: A hardcoded roll number.
- `odd_numbers`: Array of odd numbers (as strings).
- `even_numbers`: Array of even numbers (as strings).
- `alphabets`: Array of alphabetical characters (converted to uppercase).
- `special_characters`: Array of special characters.
- `sum`: Sum of all numbers (as a string).
- `concat_string`: Concatenation of all alphabetical characters in reverse order with alternating caps.

## Setup and Local Development

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Node.js and npm (optional, for frontend development if not using CDN for Tailwind or more complex JS)

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The API will be available at `http://127.0.0.1:5000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2.  **Open `index.html` in your web browser.** You can simply double-click the file or open it via your browser's file menu. The JavaScript will interact with the backend API running on `http://127.0.0.1:5000`.

## Deployment

This application can be deployed to platforms like Render, Railway, or Vercel (for frontend if desired). Here's a general guide:

### Backend (Flask API) Deployment

For platforms like Render or Railway, you typically need to:

1.  **Push your code to a GitHub repository.** (See "Pushing to GitHub" section below).
2.  **Create a new web service** on your chosen platform.
3.  **Connect your GitHub repository.**
4.  **Configure the build command:** `pip install -r requirements.txt`.
5.  **Configure the start command:** `gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:$PORT app:app` (for Gunicorn, which is common for Flask deployments. You would need to add `gunicorn` to `requirements.txt`). Alternatively, if the platform supports a `Procfile`, you can use that.
6.  **Set environment variables** if needed (e.g., `FLASK_ENV=production`).

*Note: For `gunicorn` to work, add `gunicorn` to your `backend/requirements.txt` file and run `pip install -r requirements.txt` again locally.*

### Frontend Deployment

For a simple static frontend like this, you can:

-   **Host it alongside your backend** if the platform supports serving static files.
-   **Use a dedicated static site hosting service** like Vercel, Netlify, or GitHub Pages. You would typically point these services to your `frontend/` directory.

## Pushing to GitHub

1.  **Initialize a Git repository (if not already done):**
    ```bash
    git init
    ```
2.  **Add your files to the staging area:**
    ```bash
    git add .
    ```
3.  **Commit your changes:**
    ```bash
    git commit -m "Initial commit: BFHL API and Frontend"
    ```
4.  **Create a new public repository on GitHub.**
5.  **Link your local repository to the GitHub repository:**
    ```bash
    git remote add origin <YOUR_GITHUB_REPO_URL>
    ```
6.  **Push your code to GitHub:**
    ```bash
    git push -u origin main
    ```
    (Or `master` instead of `main` depending on your GitHub default branch setting).
