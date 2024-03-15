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

# File uploader for a single file
uploaded_file = st.file_uploader("Upload your .npy file", type=['npy'], key="file_uploader")

# Variable to track if the user has uploaded a file
file_uploaded = False

# Check if the user uploaded a file
if uploaded_file:
    file_uploaded = True

    # Load .npy file
    data = np.load(uploaded_file)

    # Reshape data
    data_reshaped = np.reshape(data, (1, 28, 1))

    # Make prediction
    predictions = (model.predict(data_reshaped) > 0.5).astype("int32")

    # Determine class
    # Assuming predictions is a 2D array

    if predictions[0][0] == 0:
        # Automatically scroll to the results section
        st.markdown(
            """<script>
            window.scrollTo(0, document.body.scrollHeight);
            </script>""",
            unsafe_allow_html=True
        )

        # Display results
        st.warning("Yo broo!! You're Healthy")
        st.markdown("Additional content for the Healthy Screen.")

    else:
        # Automatically scroll to the results section
        st.markdown(
            """<script>
            window.scrollTo(0, document.body.scrollHeight);
            </script>""",
            unsafe_allow_html=True
        )

        # Display results
        st.warning("Ahhhhh, nooooo wayyy,, thyroidd")
        
        st.markdown("Additional content for the Thyroid Screen.")

# Content based on URL parameters only when a file has been uploaded
if file_uploaded:
    params = st.experimental_get_query_params()
    if 'healthy' in params and params['healthy'][0] == 'True':
        st.header("Healthy Screen Content")
        st.success("Great news! You're healthy.")
        st.subheader("Tips for maintaining a healthy lifestyle:")
        st.markdown("- done")
        st.markdown("- Eat a balanced diet.")
        st.markdown("- Stay physically active.")
        st.markdown("- Get enough sleep.")
        st.markdown("- Manage stress.")
    elif 'thyroid' in params and params['thyroid'][0] == 'True':
        st.header("Thyroid Screen Content")
        st.error("It seems there might be an issue with your thyroid.")
        st.subheader("What you can do:")
        st.markdown("- Consult with a healthcare professional for further evaluation.")
        st.markdown("- Consider additional medical tests if recommended.")
        st.markdown("- Follow your healthcare provider's advice for management.")
