from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape import scrape

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        try:
            data = scrape()
            return jsonify({'data': data})
        except:
            return jsonify({'data': "error"})
    else:
        return "Hello from Scrapping API"


if __name__ == "__main__":
    app.run(debug=True)
