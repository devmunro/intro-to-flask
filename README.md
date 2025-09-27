# Intro to Flask - Step 3: Dynamic Routes

Welcome to **Step 3**

This step introduces:
- Dynamic routes with URL variables (`/blog/<post_id>`)
---

## File Highlights
- `app.py` contains routes for `/` (home), `/about`, and `/blog/<post_id>`.
- HTML templates are in the `templates/` folder (`index.html`, `about.html`, `blog.html`).
- Users can now type dynamic blog URLs directly in the browser.

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
- Dynamic routes allow you to pass variables from the URL into templates, e.g., /blog/<post_id> lets us show different posts based on post_id.