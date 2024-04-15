from joblib import load

# Load the label encoder
label_encoder = load('MLModels/label_encoder.joblib')

# Load the vectorizer
vectorizer = load('MLModels/vectorizer.joblib')

# Load the trained random forest classifier model
xgb_classifier = load('MLModels/xgb_classifier.joblib')

def team_classifier(input_data):
    # Convert the input data to numerical features using the same vectorizer
    input_vectorized = vectorizer.transform(input_data)

    # Make predictions for the input data
    predictions_proba = xgb_classifier.predict_proba(input_vectorized)[0]

    # Get the top 3 classes based on the predicted probabilities
    top_3_classes_indices = sorted(range(len(predictions_proba)), key=lambda i: predictions_proba[i], reverse=True)[:3]

    # Decode the class indices to class names using the label encoder
    top_3_class_names = label_encoder.inverse_transform(top_3_classes_indices)

    # Generate the top 3 class names as a string separated by new lines
    top_3_class_names_str = '\n'.join(top_3_class_names)

    return top_3_class_names_str
