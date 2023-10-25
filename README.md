# Internship-Application-Prediction-Model
# Internship Application Preliminary Approval System

## Table of Contents


[Stage 1 - Gathering and Analyzing Data](#stage-1---gathering-and-analyzing-data)

[Stage 2 - Cleaning of Data](#stage-2---cleaning-of-data)

[Stage 3 - Developing Prediction Model (Model Training)](#stage-3---developing-prediction-model-model-training)

[Stage 4 - Applying Prediction Model to New Applicants](#stage-4---applying-prediction-model-to-new-applicants)

## Introduction

This project aims to automate the preliminary approval process for internship applications in a multinational company. The company will predict the probability of applicants passing this preliminary approval based on their age, gender, country of origin, and university CGPA. The system will have four main activities, including developing a prediction model, applying the model to new applicants, gathering and analyzing data, and cleaning the data.

## Project Stages

The project is divided into four main stages:

## Stage 1 - Gathering and Analyzing Data

- Historical data is collected by testing new applicants using an automated MCQ Generation, Assessment, and Analysis System.
- Variables such as age, gender, country of origin, and university CGPA are collected as input for the prediction model.
- The test is developed using Python with a graphical user interface.
- Each test consists of ten questions, including text-based and image-based questions.
- The passing percentage for the test is set at 80%.
- The application system saves applicants' answers in an external output file along with their identifications.
- Basic statistical analysis is performed on the results, including maximum, average, and mode scores.
- At least four statistical charts are created using Matplotlib.

## Stage 2 - Cleaning of Data

- Thirty additional applicants' hypothetical results with various types of dirty data are added.
- Two different types of data cleaning operations are performed using NumPy and Pandas.

## Stage 3 - Developing Prediction Model (Model Training)

- The cleaned data becomes the input for machine learning prediction analysis using KERAS.
- Data is formatted to ensure data validity and integrity using Numpy and Pandas.
- The prediction neural model is developed and tested for accuracy using the previous twenty applicants' results.

## Stage 4 - Applying Prediction Model to New Applicants

- The prediction model is applied to five new applicants to automatically accept or reject their applications.
- Proper graphical user interface is implemented for this component.

