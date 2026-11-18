 Weight Prediction System        

A web application that predicts a person's weight from their height using a Simple Linear Regression model. The app is built with Python and Flask.

## Features

- Accepts height in centimeters
- Predicts weight in kilograms
- Uses a trained Scikit-learn model
- Provides a simple web interface

## Project Structure



├── app.py
├── Procfile
├── requiredment.txt
├── SLR_MODEL.pkl
└── templates/
    └── index.html


## Requirements

- Python 3
- Dependencies listed in `requiredment.txt`

## Run Locally


1. Create and activate a virtual environment:

   
   python -m venv venv


   Windows:

   
   venv\Scripts\activate
   

   macOS or Linux:

   
   source venv/bin/activate
   

2. Install the dependencies:

   
   pip install -r requiredment.txt
   

3. Start the app:

   
   python app.py
   
4. Open `http://127.0.0.1:5000` in your browser.

## How to Use

Enter a height in centimeters and select **Predict Weight**. The app displays the model's estimated weight in kilograms.

## Deployment

The included `Procfile` starts the app with Gunicorn:


web:gunicorn app:app


Configure your hosting platform to install dependencies with:


pip install -r requiredment.txt

## Model

The trained model is loaded from `SLR_MODEL.pkl` when the Flask app starts. Keep this file in the project root when running or deploying the app.

## Note

This project is for demonstration and educational purposes. Predictions are estimates and should not be used as medical advice.


Your dependency file is named `requiredment.txt`. You can keep that name and use the commands above, or rename it to `requirements.txt` and update the README and deployment settings to match.
