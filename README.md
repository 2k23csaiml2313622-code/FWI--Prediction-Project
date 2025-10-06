🔥 Forest Fire Weather Index (FWI) Prediction Web App
This project delivers a machine learning solution to predict the Fire Weather Index (FWI), a key metric for assessing the danger of forest fires. The model is deployed as a user-friendly web application using the Flask micro-framework, and the interface is built with simple HTML and CSS.

✨ Features
Real-time FWI Prediction: Provides an immediate prediction of the FWI value based on current or forecasted meteorological inputs.

Machine Learning Core: Uses a trained Regression Model (e.g., Random Forest Regressor) to calculate the FWI from weather data.

Simple Interface: Features a clean, straightforward web form (HTML/CSS) for easy data input.

Python Backend: The entire application logic, from handling the web request to running the prediction, is managed efficiently by Python and the Flask framework.

Kaggle Data Source: The predictive model was developed using the well-known Forest Fire Dataset from Kaggle (often linked to the UCI ML Repository).

💾 Dataset and Target Variable
The model predicts the Fire Weather Index (FWI), which is an internationally recognized standard for calculating the daily forest fire hazard. The input variables are derived from the dataset and include core meteorological readings:

Input Feature	Description	Example Value
FFMC-	Fine Fuel Moisture Code	Flammability of light fuels.
DMC-	Duff Moisture Code	Moisture content of organic layers.
DC-	Drought Code	Effect of long-term drought.
ISI-	Initial Spread Index	Expected rate of fire spread.
Temp-	Ambient Temperature ($^{\circ}$C)	22.5
RH-	Relative Humidity (%)	45.0
Wind-	Wind Speed (km/h)	4.0
Rain	Outside- Rain (mm/m$^2$)	0.0
FWI (Output)-	Fire Weather Index	The predicted fire intensity.


🛠️ Technology Stack

Backend Framework-	Flask	Lightweight web server for routing, request handling, and rendering.
Programming-	Python 3.x	Core language for the model and application logic.
Machine Learning-	Scikit-learn / NumPy / Pandas	Data preprocessing, model training, and prediction pipeline.
Interface-	HTML / CSS	Simple, static frontend for user interaction.
Model Persistence-	pickle	Serialization library used to save and load the trained ML model.

Navigate to the local URL (http://127.0.0.1:5000/) in your web browser.

You will be greeted by the simple HTML form.

Enter the required meteorological parameters (FFMC, DMC, DC, ISI, Temp, RH, Wind, Rain).

Click the "Predict FWI" button.

The Flask backend will capture the inputs, scale/transform the data (as per model training), run the prediction, and display the predicted FWI value and the corresponding risk level (e.g., Low, Moderate, High) back on the webpage.

🌐 Explanation of Flask
Flask is a powerful yet minimalist Python web framework, often referred to as a "micro-framework" because it is designed to keep the core simple while making it easy to integrate with specialized libraries.

Why Flask for FWI Prediction?
Direct Integration with ML: Flask's simplicity makes it the perfect "wrapper" for a machine learning model. It allows the developer to focus on the core logic: loading the model, processing the input data, and calling the model.predict() function.

Routing: Flask handles the routing—mapping the URL (/ or /predict) to a specific Python function (def home(): or def predict():). When the user submits the HTML form, Flask catches the data and passes it to your prediction function.

Templating: It uses Jinja2 templating (which works well with basic HTML) to dynamically inject the prediction results (the calculated FWI) back into the final HTML page presented to the user.

Lightweight: Since the project uses simple HTML/CSS and doesn't require a complex database (like MongoDB in your previous project, though it could be added here), Flask ensures the application is fast, has a small footprint, and is very easy to deploy on platforms like Heroku or other cloud services.
