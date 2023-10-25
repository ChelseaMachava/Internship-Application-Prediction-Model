import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from keras.models import load_model

# Load the trained model
model = load_model("Trained_model.h5")

# Function to preprocess applicant data
def preprocess_data(age, gender, country, cgpa, experience, projects):
    # Preprocess the input data as needed
    # Encode categorical variables
    gender_encoder = LabelEncoder()
    country_encoder = LabelEncoder()
    gender_encoded = gender_encoder.fit_transform([gender])
    country_encoded = country_encoder.fit_transform([country])

    # One-hot encode the categorical variables
    encoder = OneHotEncoder(sparse=False)
    gender_country_encoded = encoder.fit_transform([[gender_encoded[0], country_encoded[0]]])

    # Concatenate the encoded features with other numerical features
    input_data = np.array([[age, cgpa, experience, projects]])
    input_data_encoded = np.concatenate((input_data, gender_country_encoded), axis=1)

    return input_data_encoded

# Function to predict applicant performance
def predict_performance(applicant_data):
    # Make a prediction using the model
    prediction = model.predict(applicant_data)

    # Return the prediction result
    return prediction[0][0]

# Example usage
age = 25
gender = "Male"
country = "Suriname"
cgpa = 6.36
experience = 6
projects = 15

# Preprocess the input data
applicant_data = preprocess_data(age, gender, country, cgpa, experience, projects)

# Predict the performance
prediction = predict_performance(applicant_data)

# Print the prediction result
print("Prediction: ", "Pass" if prediction >= 0.5 else "Fail")
