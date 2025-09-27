# Intro to Flask 

Welcome to the **Intro to Flask**  repository!  

This repo is based on the live session - Intro to Flask

About creating your first flask app to adding dynamic routes and templates.

---

## Overview

The repository is split into **branches for each step**:

| Step | Branch | Content                                                |
|------|--------|--------------------------------------------------------|
| Step 1 | `step-1-setup` | Minimal Flask app with a basic home route              |
| Step 2 | `step-2-static-pages` | Static routes and HTML templates (`/` and `/about`)    |
| Step 3 | `step-3-dynamic-routes` | Dynamic routes using URL variables (`/blog/<post_id>`) |

---

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/devmunro/intro-to-flask.git
cd intro-to-flask
pip install -r requirements.txt #pip3 for mac
```

2. Switch to the branch you want to explore

```bash
git checkout step-1-setup
# or step-2-static-pages
# or step-3-dynamic-routes
```

3. Run the Flask app
```bash
python app.py
#visit - http://localhost:5050/
```


## Notes for Students

- debug=True lets Flask reload the server automatically when you save changes.
- Default Flask port is 5000; here we use 5050.
- render_template() looks in the templates/ folder by default.
- Official Flask documentation: https://flask.palletsprojects.com/en/stable/quickstart/
