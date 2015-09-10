from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = "super_secret"

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()