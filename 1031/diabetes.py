from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib


app = Flask(__name__)


# 모델 로드
model = joblib.load('diabetes_model.pkl')


@app.route('/')
def index():
   # /templates 폴더 안에 diabetes.html을 사전에 넣어주기
   return render_template('diabetes.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
   if request.method == 'POST':
       data = request.get_json() # JSON으로 넘어온 데이터를 data객체로 받기
       features = np.array([[
           data['Age'],
           data['Blood_Pressure'],
           data['Cholesterol'],
           data['Gender_Encoded']
       ]])
      
       # 분류 결과 및 정확도 가져오기
       prediction = int(model.predict(features)[0])
       probability = float(model.predict_proba(features).max())


       # 추론 결과를 JSON으로 반환
       return jsonify({
           'prediction': '당뇨병' if prediction == 1 else '당뇨병 아님',
           'probability': probability
       })


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000, debug=True)
