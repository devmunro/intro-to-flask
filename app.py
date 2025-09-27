"""
Step 2: Static pages with templates.
This app demonstrates rendering HTML templates using Flask.
"""

from flask import Flask, render_template

# Create the Flask app instance
app: Flask = Flask(__name__)

@app.route("/")
def home_page() -> str:
    """
    Render the home page using index.html template.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")

@app.route("/about")
def about_page() -> str:
    """
    Render the about page using about.html template.

    Returns:
        str: Rendered HTML template for the about page.
    """
    return render_template("about.html")

if __name__ == "__main__":
    # Run the app in debug mode on port 5050
    app.run(debug=True, port=5050)
