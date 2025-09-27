"""
Step 2: Static pages with templates.
This app demonstrates rendering HTML templates using Flask.
"""

from flask import Flask, render_template

# Create the Flask app instance
app: Flask = Flask(__name__)

@app.route("/")
def home_page():
    """
    Render the home page using index.html template.
    """
    return render_template("index.html")


@app.route("/about")
def about_page():
    """
    Render the about page using about.html template.
    """
    return render_template("about.html")


if __name__ == "__main__":
    # Run the app in debug mode on port 5050
    app.run(debug=True, port=5050)
