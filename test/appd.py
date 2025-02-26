from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的请求

@app.route('/images.json')
def get_json():
    return send_from_directory('.', 'images.json')

if __name__ == '__main__':
    app.run(debug=True)