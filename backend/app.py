from flask import Flask, request, jsonify
from weather_service import get_weather

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'London')
    data = get_weather(city)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
