from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


app = Flask(__name__)
app.config.from_object('settings')


@app.route("/")
def home():
    cam_url = app.config['WEBCAM_URL']
    return render_template('home.html', cam_url=cam_url)


if __name__ == "__main__":
    app.run()
