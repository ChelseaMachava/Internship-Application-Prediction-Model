import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the combined results from the applicants' test
dirty_data = pd.read_csv('answer1.txt', delimiter=':')

clean_data = dirty_data.drop_duplicates()
clean_data.Name.fillna(clean_data.Name.mode().iloc[0], inplace=True)
clean_data.Gender.fillna(clean_data.Gender.mode().iloc[0], inplace=True)
clean_data.Country.fillna(clean_data.Country.mode().iloc[0], inplace=True)
clean_data.Status.fillna(clean_data.Status.mode().iloc[0], inplace=True)

missing_mask = np.isnan(clean_data['Age'])
mean_value = np.nanmean(clean_data['Age'])
clean_data['Age'][missing_mask] = mean_value

missing_mask = np.isnan(clean_data['CGPA'])
mean_value = np.nanmean(clean_data['CGPA'])
clean_data['CGPA'][missing_mask] = mean_value

missing_mask = np.isnan(clean_data['Experience'])
median_value = np.nanmedian(clean_data['Experience'])
clean_data['Experience'][missing_mask] = median_value

missing_mask = np.isnan(clean_data['Projects'])
median_value = np.nanmedian(clean_data['Projects'])
clean_data['Projects'][missing_mask] = median_value


label_encoder = LabelEncoder()
clean_data.Name = label_encoder.fit_transform(clean_data.Name)
clean_data.Gender = label_encoder.fit_transform(clean_data.Gender)
clean_data.Country = label_encoder.fit_transform(clean_data.Country)
clean_data.Status = label_encoder.fit_transform(clean_data.Status)

clean_data = clean_data.drop(clean_data.columns[0], axis=1)
clean_data.to_csv('CleanData.csv', index=False)

# Tem a ver com os 5 que usei na parte 1, acho que vou apagar
testing_data = pd.read_csv('Testing.csv', delimiter=';')
testing_data.Name = label_encoder.fit_transform(testing_data.Name)
testing_data.Gender = label_encoder.fit_transform(testing_data.Gender)
testing_data.Country = label_encoder.fit_transform(testing_data.Country)
testing_data = testing_data.drop(testing_data.columns[0], axis=1)
testing_data.to_csv('TestingData.csv', index=False)

# Tem a ver com respostas do primeiro questionario
Testing_answers_data = pd.read_csv('applicant_details.txt', delimiter=',')
Testing_answers_data = Testing_answers_data.drop(Testing_answers_data.columns[0], axis=1)
Testing_answers_data.Gender = label_encoder.fit_transform(Testing_answers_data.Gender)
Testing_answers_data.Country = label_encoder.fit_transform(Testing_answers_data.Country)
Testing_answers_data.Status = label_encoder.fit_transform(Testing_answers_data.Status)
Testing_answers_data.to_csv('applicant_details.csv', index=False)

print(clean_data)

