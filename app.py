from flask import Flask

"""
Step 1: Minimal Flask setup.
This app demonstrates creating a Flask app and adding a basic home route.
"""

# Create the Flask app instance
app: Flask = Flask(__name__)

@app.route("/")
def home_page() -> str:
    """
    Render the home page with a welcome message.

    Returns:
        str: Simple HTML content for the home page.
    """
    return "<h1>Welcome to my first Flask app!</h1>"

if __name__ == "__main__":
    # debug=True - runs the Flask app in debug mode
    # default port is 5000, but here we use 5050 to avoid conflicts
    # you can also add host="0.0.0.0" to make it externally accessible
    app.run(debug=True, port=5050)
