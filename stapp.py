import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np

# Load the model
@st.cache_data
def load_model():
    model = tf.keras.models.load_model('weights.best.hdf5')
    return model

model = load_model()

# Streamlit App Title
st.write("# Bike Sharing Demand Prediction")

# CSV File Uploader
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

def make_prediction(data, model):
    prediction = model.predict(data)
    return prediction

if uploaded_file is not None:
    try:
        # Read and preprocess the data
        input_df = pd.read_csv(uploaded_file)
        preprocessed_data = preprocess_data(input_df)

        # Make predictions
        if st.sidebar.button('Predict Demand'):
            prediction = make_prediction(preprocessed_data, model)
            st.subheader("Bike Sharing Demand Prediction")
            st.write(f"Predicted Bike Demand: {prediction[0][0]:.2f} bikes")

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.sidebar.write("Please upload a CSV file to make predictions.")
