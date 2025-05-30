import pandas as pd
import pickle as pk
import streamlit as st

# Load the trained model
model = pk.load(open('C:/Users/bipin/predicting house price/House_Price_Prediction.pkl', 'rb'))

# Title of the app
st.header('House Price Prediction')

# Load the cleaned data
data = pd.read_csv('C:/Users/bipin/predicting house price/Cleaned_data.csv')

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

# Prediction button
if st.button("Predict Price"):
    output = model.predict(input_data)
    
    # Displaying the output
    st.markdown("### Prediction Result")
    st.success(f"Price of the House is ₹{output[0] * 100000:.2f}")
