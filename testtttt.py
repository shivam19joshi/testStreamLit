import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

# Function to suggest diet plan based on BMI and other factors
def suggest_diet_plan(bmi, age, fat_percentage):
    if bmi < 18.5:
        return "Underweight: Increase calorie intake with balanced nutrients, focus on protein-rich foods."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight: Maintain a balanced diet with appropriate calorie intake. Include whole grains, lean protein, and vegetables."
    elif 25 <= bmi < 29.9:
        return "Overweight: Reduce calorie intake, focus on whole foods, reduce sugar and refined carbs. Include more vegetables and lean proteins."
    else:
        return "Obese: Significantly reduce calorie intake, focus on high-fiber, low-fat foods. Consider consulting a dietitian for a personalized plan."

# Streamlit app layout
st.title("Diet Plan Suggestion Based on BMI")

# User inputs
height = st.number_input("Enter your height (cm):", min_value=100, max_value=250, value=170)
weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70)
age = st.number_input("Enter your age:", min_value=10, max_value=100, value=25)
fat_percentage = st.number_input("Enter your body fat percentage:", min_value=1, max_value=50, value=20)

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display the calculated BMI
st.write(f"Your BMI is: {bmi}")

# Suggest a diet plan
diet_plan = suggest_diet_plan(bmi, age, fat_percentage)
st.write(f"Diet Plan: {diet_plan}")
