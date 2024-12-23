from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("src/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
