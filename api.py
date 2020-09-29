from flask import Flask

from lightpi.hardware import strip, chain1, chain2


app = Flask(__name__)


@app.route("/")
def home():
    return 'Hello, World!'


@app.route("/api/on")
def light_on():
    strip.orange()
    chain1.on()
    chain2.on()
    return "ON"


@app.route("/api/off")
def light_off():
    strip.off()
    chain1.off()
    chain2.off()
    return 'OFF'


@app.route("/api/dim")
def light_dim():
    strip.off()
    chain1.on()
    chain2.off()
    return 'DIM'


@app.route("/api/RED")
def light_off():
    strip.red()
    chain1.off()
    chain2.off()
    return 'RED'


if __name__ == "__main__":
    app.run(host='lightpi.local')
