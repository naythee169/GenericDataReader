import webbrowser
import threading
from time import sleep
from flask import Flask, render_template_string
from app.api_handler import api, unified_data
from app.visualization import render_dashboard

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def index():
    # Render a simple dashboard page with both table and bar chart
    html = render_dashboard(unified_data)
    return render_template_string(html)

def open_browser():
    """Wait for Flask to start, then open the default web browser."""
    sleep(1)  # Give Flask time to start
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()  # Open browser in a background thread
    app.run(debug=True, use_reloader=False)  # Disable auto-reloader to prevent double opening