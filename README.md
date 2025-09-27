# Intro to Flask - Step 2: Static Routes

Welcome to **Step 2**

This step introduces:
- Rendering HTML templates with Flask
- Creating static pages (`/` and `/about`)
---

## File Highlights
- `app.py` contains routes for `/` (home) and `/about`.
- HTML templates are in the `templates/` folder (`index.html` and `about.html`).

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

- `render_template()` **by default looks in the `templates/` folder**, so Flask knows where to find your HTML files.
