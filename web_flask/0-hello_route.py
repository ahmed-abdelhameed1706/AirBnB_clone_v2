from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return '<p>Hello HBNB!</p>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")