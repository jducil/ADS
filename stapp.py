pip install scikit-learn
import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the model
@st.cache(allow_output_mutation=True)
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

        if st.sidebar.button('Predict Demand'):
            prediction = make_prediction(preprocessed_data, model)
            # Display the prediction
            st.subheader("Bike Sharing Demand Prediction")
            st.write(f"Predicted Bike Demand: {prediction[0][0]:.2f} bikes")
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.sidebar.write("Please upload a CSV file to make predictions.")


        # Make predictions
        if st.sidebar.button('Predict Demand'):
            prediction = make_prediction(X_test, model)
            st.subheader("Bike Sharing Demand Prediction")
            st.write(f"Predicted Bike Demand: {prediction[0][0]:.2f} bikes")

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.sidebar.write("Please upload a CSV file to make predictions.")
