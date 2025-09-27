"""
Step 3: Dynamic Routes
This builds on Step 2 and introduces dynamic routing concepts.

"""

from flask import Flask, render_template

# Create the Flask app instance
app: Flask = Flask(__name__)

@app.route("/")
def home_page():
    """
    Render the home page using index.html template.

    Returns:
        Rendered HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/about")
def about_page():
    """
    Render the about page using about.html template.

    Returns:
        Rendered HTML template for the about page.
    """
    return render_template("about.html")


@app.route("/blog/<int:post_id>")
def blog_post(post_id: int):
    """
    Render a blog post dynamically based on post_id.

    Args:
        post_id (int): The ID of the blog post from the URL.

    Returns:
        Rendered blog template with the post number.
    """
    return render_template("blog.html", post_id=post_id)


if __name__ == "__main__":
    # Run the app in debug mode on port 5050
    app.run(debug=True, port=5050)
