from flask import Flask, render_template, request, jsonify
from textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
    
predictor = PredictionPipeline()

# Your prediction function
def predict_function(input_text):
    output = predictor.predict(input_text)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    result = predict_function(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
