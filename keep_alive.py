from flask import Flask, render_template
from threading import Thread

@app.route('/')
def index():
    text = get_text()
    return render_template('index.html', text=text)
def get_text():
    return "Hello, world!"

def keep_alive():
  t = Thread(target=run)
  t.start()
