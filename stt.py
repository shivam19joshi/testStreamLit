import streamlit as st

# Title of the app
st.title("Stock Investment Recommendation")

# User input
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
risk_type = st.selectbox("Select your risk type", ["Low", "Medium", "High"])

# Recommendation logic
if risk_type == "Low":
    recommendation = "We recommend investing in government bonds and blue-chip stocks."
elif risk_type == "Medium":
    recommendation = "We recommend a mix of index funds and dividend-paying stocks."
elif risk_type == "High":
    recommendation = "We recommend looking into growth stocks and sector-specific ETFs."

# Display user input and recommendation
if st.button("Submit"):
    st.write(f"Hello {name}, age {age}")
    st.write(f"Based on your risk type ({risk_type}), {recommendation}")

# To run this app, save it as app.py and run `streamlit run app.py` in your terminal.
