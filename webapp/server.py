from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


app = Flask(__name__)
app.config.from_object('settings')



@app.route("/")
def home():
    #return 'Hello, World!'
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
