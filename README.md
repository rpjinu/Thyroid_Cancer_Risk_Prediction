# Thyroid_Cancer_Risk_Prediction
"This project training model that can predict the risk of Thyroid cancer risk Prediction also API  using streamlit "

<img src="https://github.com/rpjinu/Thyroid_Cancer_Risk_Prediction/blob/main/project_image.png">

# Thyroid Cancer Risk Prediction

## Overview
Thyroid Cancer Risk Prediction is a machine learning-based project aimed at assessing the risk of thyroid cancer based on patient data. This project utilizes a trained model to classify patients based on risk factors and provides predictions via an API.

## Features
- **Data Preprocessing**: Handles missing values, feature encoding, and normalization.
- **Machine Learning Model**: Uses RandomForestClassifier for predictions.
- **API Integration**: A Flask API is provided for real-time predictions.
- **Deployment Ready**: Can be deployed using Streamlit or Flask.

## Dataset
The dataset consists of patient medical records with features such as:
- Age, Gender, TSH Level, T3 Level, T4 Level, Thyroid Nodules, and Family History.
- The target variable is `Thyroid_Cancer_Risk` (0: Low Risk, 1: High Risk).

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-repo/thyroid-cancer-risk-prediction.git
cd thyroid-cancer-risk-prediction
pip install -r requirements.txt
```

## Model Training
Run the training script to preprocess the data and train the model:
```bash
python train.py
```

## API Usage
Start the Flask API:
```bash
python app.py
```

### API Endpoints
#### **1. Predict Thyroid Cancer Risk**
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request Body (JSON):**
```json
{
  "age": 45,
  "gender": "Male",
  "tsh_level": 2.5,
  "t3_level": 1.8,
  "t4_level": 8.2,
  "nodules": 1,
  "family_history": 1
}
```
- **Response:**
```json
{
  "prediction": "High Risk",
  "confidence": 0.85
}
```

## Project Structure
```
├── data/                # Dataset folder
├── models/              # Saved models
├── notebooks/           # Jupyter notebooks for EDA
├── app.py               # Flask API
├── train.py             # Model training script
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

## Deployment
You can deploy this model using **Streamlit**:
```bash
streamlit run app.py
```

## Future Enhancements
- Improve model accuracy with hyperparameter tuning.
- Deploy using cloud services like AWS/GCP.
- Enhance API security and authentication.

## Contributors
- **Your Name** - Machine Learning Developer

## License
This project is licensed under the MIT License.

