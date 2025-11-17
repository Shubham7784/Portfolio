from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A 'secret_key' is needed for features like 'flashing' messages


@app.route('/')
def home():
    """Serves the Home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Serves the About Me page."""
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    """Serves the Portfolio page."""
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True) 