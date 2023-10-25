import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model("Trained_model.h5")

# Load the test data from "answer.csv"
test_data = np.loadtxt("applicant_details.csv", delimiter=",", skiprows=1)

# Extract the input features from the test data
x_test = test_data[:, 0:6]  # Exclude the name column
y_test = test_data[:, 6]

# Make predictions using the trained model
predictions = model.predict(x_test)

# Print the predictions
for i in range(len(predictions)):
    print("Applicant", i+1, "Prediction:", predictions[i])

# Convert predictions to binary values (0 or 1) based on a threshold
threshold = 0.5
binary_predictions = [1 if prediction > threshold else 0 for prediction in predictions]

# Calculate accuracy
total_samples = len(y_test)
correct_predictions = sum(binary_predictions == y_test)
accuracy = correct_predictions / total_samples

print("Accuracy: ", accuracy)