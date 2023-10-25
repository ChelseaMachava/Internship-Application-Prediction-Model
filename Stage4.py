import tkinter as tk
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from keras.models import load_model

# Load the trained model
model = load_model("Trained_model.h5")

# Create the GUI window
window = tk.Tk()
window.title("Applicant Prediction")
window.geometry("300x400")

# Create GUI elements (labels, entry fields, buttons)
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar(window)
gender_var.set("Male")
gender_option = tk.OptionMenu(window, gender_var, "Male", "Female")
gender_option.pack()

country_label = tk.Label(window, text="Country:")
country_label.pack()
country_entry = tk.Entry(window)
country_entry.pack()

cgpa_label = tk.Label(window, text="CGPA:")
cgpa_label.pack()
cgpa_entry = tk.Entry(window)
cgpa_entry.pack()

experience_label = tk.Label(window, text="Experience (in years):")
experience_label.pack()
experience_entry = tk.Entry(window)
experience_entry.pack()

projects_label = tk.Label(window, text="Projects:")
projects_label.pack()
projects_entry = tk.Entry(window)
projects_entry.pack()

# Create a StringVar for the prediction result
prediction_var = tk.StringVar()

# Function to process applicant data and make a prediction
def predict_application():
    # Get the input values from the GUI fields
    age = float(age_entry.get())
    gender = gender_var.get()
    country = country_entry.get()
    cgpa = float(cgpa_entry.get())
    experience = float(experience_entry.get())
    projects = float(projects_entry.get())

    # Preprocess the input data as needed (e.g., encoding categorical variables)
    encoder = OneHotEncoder(sparse_output=False)

    # Encode 'gender' and 'country' variables together
    input_data_encoded = encoder.fit_transform([[gender, country]])

    # Concatenate the encoded features with other numerical features
    input_data = np.array([[age, cgpa, experience, projects]])
    input_data_encoded = np.concatenate((input_data, input_data_encoded), axis=1)

    # Make a prediction using the model
    prediction = model.predict(input_data_encoded)

    # Determine pass or fail based on the prediction threshold (0.5)
    if prediction >= 0.5:
        prediction_text = "Accepted"
    else:
        prediction_text = "Rejected"

    # Update the prediction result
    prediction_var.set("Prediction: " + str(prediction[0][0]) + " (" + prediction_text + ")")

predict_button = tk.Button(window, text="Predict", command=predict_application)
predict_button.pack()

result_label = tk.Label(window, textvariable=prediction_var)
result_label.pack()

# Start the GUI event loop
window.mainloop()
