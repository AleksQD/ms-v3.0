from flask import Flask, render_template, url_for
from datetime import datetime
from API_res import ms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = ms)


if __name__ == '__main__':
    app.run(debug=True)
