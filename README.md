# Wine-Classifier

## This project is a multiclass classification model designed to predict the quality of wine based on physicochemical properties. Using the Wine Quality Dataset (UCI), the model classifies wine samples into quality ratings ranging from 3 to 8, providing a practical demonstration of machine learning in quality control for food and beverage industries.

## Model: Multiclass Classification (Random Forest)

## Dataset: Wine Quality Dataset (UCI)

## Preprocessing:

### Handled class imbalance (e.g., class merging or resampling techniques)
### Normalized features to improve convergence
### Performed EDA to identify key feature distributions

## Evaluation:

### Used a confusion matrix and classification report for insight into per-class performance
### Random Forest Model
Multiclass AUC: 0.9892

              precision    recall  f1-score   support

           0       0.99      0.99      0.99       291
           1       0.92      0.98      0.95       272
           2       0.82      0.78      0.80       287
           3       0.73      0.67      0.70       268
           4       0.86      0.89      0.88       281
           5       0.95      0.97      0.96       312
           6       1.00      1.00      1.00       272

    accuracy                           0.90      1983
   macro avg       0.90      0.90      0.90      1983
weighted avg       0.90      0.90      0.90      1983

## Objective:
### To develop a robust model capable of automatically grading wine quality based on measurable chemical attributes, demonstrating real-world applications of machine learning in classification tasks.
