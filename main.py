from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hey Dadji! Lets go to America! (This is not a question this is a threat!)</h1>"

if __name__ == '__main__':
    app.run()
