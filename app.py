import pandas as pd
import pickle as pk
import streamlit as st

# Load the trained model
model = pk.load(open('C:/Users/bipin/predicting house price/House_Prediction_model1.pkl', 'rb'))

# Title of the app
st.header('House Price Prediction')

# Load the cleaned data
data = pd.read_csv('C:/Users/bipin/predicting house price/Cleaned_data1.csv')

# User input: Select location
loc = st.selectbox('Choose the location', data['location'].unique())

# User input: Total area in square feet
sqft = st.number_input('Enter Total Sqft', min_value=0)

# User input: Number of bedrooms
beds = st.number_input('Enter no of Bedrooms', min_value=0)

# User input: Number of bathrooms
bath = st.number_input('Enter no of Bathrooms', min_value=0)

# User input: Number of balconies
balc = st.number_input('Enter no of Balconies', min_value=0)

# Prepare input DataFrame for prediction
input_data = pd.DataFrame([[loc, sqft, bath, balc, beds]], 
                          columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

def format_price(price):
    if price >= 1e7:
        return f"{price / 1e7:.2f} Cr"
    elif price >= 1e5:
        return f"{price / 1e5:.2f} Lakh"
    else:
        return f"{price:.2f}"

# Prediction button
if st.button("Predict Price"):
    output = model.predict(input_data)
    predicted_price = output[0] * 100000
    formatted_price = format_price(predicted_price)
    st.markdown("### Prediction Result")
    st.success(f"Price of the House is ₹{formatted_price}")
# Add sidebar
st.sidebar.title("About")
st.sidebar.text("Created by Kumari Ayushi")
st.sidebar.text("GitHub Repository")
st.sidebar.write("[GitHub Repo Link](https://github.com/Ayushi8757/Predicting-House-Price-)")
