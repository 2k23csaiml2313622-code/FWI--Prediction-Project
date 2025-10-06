import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request , jsonify , render_template
import pickle
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

#importing the pickle files
ridge_model=pickle.load(open('model/ridge.pkl','rb'))
scaler_model=pickle.load(open('model/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        print("Form data received:", request.form)

        try:
            Temperature = request.form.get('Temperature')
            RH = request.form.get('RH')
            WS = request.form.get('WS')
            Rain = request.form.get('Rain')
            FFMC = request.form.get('FFMC')
            DMC = request.form.get('DMC')
            ISI = request.form.get('ISI')
            Classes = request.form.get('Classes')
            Region = request.form.get('Region')

            # Debug: print raw values
            print("Raw form inputs:")
            print("Temperature:", Temperature)
            print("RH:", RH)
            print("WS:", WS)
            print("Rain:", Rain)
            print("FFMC:", FFMC)
            print("DMC:", DMC)
            print("ISI:", ISI) 
            print("Classes:", Classes)
            print("Region:", Region)

            # Convert to float
            input_data = [
                float(Temperature), float(RH), float(WS), float(Rain),
                float(FFMC), float(DMC), float(ISI), float(Classes), float(Region)
            ]

            new_data_scaled = scaler_model.transform([input_data])
            result = ridge_model.predict(new_data_scaled)

            return render_template('home.html', results=result[0])

        except Exception as e:
            print("Error during prediction:", e)
            return render_template('home.html', results=f"Error: {str(e)}")

    return render_template('home.html')

    
        
if __name__=="__main__":
    app.run(host="0.0.0.0")

