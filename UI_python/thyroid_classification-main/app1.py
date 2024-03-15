import streamlit as st
import numpy as np
import tensorflow as tf


def load_model():
    model = tf.keras.models.load_model('./models/model.h5', compile=False)
    return model


# Load the model
model = load_model()

# Title of the app
st.title("Hypothyroid")

# File uploader
uploaded_files = st.file_uploader("Upload your .npy files", accept_multiple_files=True, type=['npy'])

# Process and predict
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Load .npy file
        data = np.load(uploaded_file)

        # Reshape data
        data_reshaped = np.reshape(data, (1, 28, 1))

        # Make prediction
        predictions = (model.predict(data_reshaped) > 0.5).astype("int32")

        # Determine class
        # import streamlit as st

# Assuming predictions is a 2D array

    if predictions[0][0] == 0:
        st.warning("Yo broo!! You're Healthy")
        # Add a button to redirect to another screen when healthy
        if st.button("Go to Healthy Screen"):
            st.sidebar.success("Redirecting to Healthy Screen")
            # You can add code here to redirect or load content for the Healthy Screen
    else:
        st.warning("Ahhhhh, nooooo wayyy,, thyroidd")
        # Add a button to redirect to another screen when thyroid issue
        if st.button("Go to Thyroid Screen"):
            st.sidebar.success("Redirecting to Thyroid Screen")
            # You can add code here to redirect or load content for the Thyroid Screen

