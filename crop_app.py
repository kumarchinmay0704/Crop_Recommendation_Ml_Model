import joblib
from flask import Flask, render_template, request, redirect
import webview
import threading
import os
# python "C:\Users\harsh\Desktop\ML PROJECTS\CROP_RECOMENDATION3\crop_app3\crop_app.py"
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'crop_app')
app = Flask(__name__)

def start_server():
    app.run(host='0.0.0.0')


@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        joblib.load(MODEL_PATH,'r')
        model = joblib.load(open(MODEL_PATH,'rb'))
        arr = [values]
        acc = model.predict(arr)
        prediction = str(acc[0]) 
        return render_template('prediction.html', prediction=prediction)                                                                                                                                        
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"
    
    



if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()


    webview.create_window('Crop Recommendation System','http://127.0.0.1:5000/')
    webview.start()
