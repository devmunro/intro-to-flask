# Intro to Flask - Step 1: Minimal Flask Setup

Welcome to **Step 1** of our beginner-friendly Flask lesson.

This step introduces:
- Creating a Flask app
- Running a minimal Flask server
- Adding a basic route (`/`) with a welcome message

---

## File Highlights
- `app.py` contains a single home route (`/`) that renders a welcome message.

## Run the App

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the Flask app:
    - *Option 1*
      - python app.py # use python3 on Mac/Linux if needed
    - *Option 2*
      - flask --app app run --port 5050



3. Open your browser and visit:
http://localhost:5050/

You should see a welcome message:
"Welcome to my first Flask app!"


## Notes for Students
- debug=True allows Flask to automatically reload the server when you save changes.
- The default Flask port is 5000, but here we use 5050 to avoid conflicts.
- You can optionally add host="0.0.0.0" to make the app accessible externally.