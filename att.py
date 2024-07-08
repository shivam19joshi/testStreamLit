import streamlit as st

# Mock Gen AI model function
def gen_ai_investment_recommendations(name, age, job_type, monthly_income, risk_appetite):
    # Mock recommendations based on risk appetite
    if risk_appetite.lower() == 'high':
        return """
        <h2>Investment Recommendations for {}</h2>
        <ul>
            <li><strong>Stocks:</strong> 60%</li>
            <li><strong>Cryptocurrency:</strong> 20%</li>
            <li><strong>Real Estate:</strong> 10%</li>
            <li><strong>Mutual Funds:</strong> 10%</li>
        </ul>
        """.format(name)
    elif risk_appetite.lower() == 'medium':
        return """
        <h2>Investment Recommendations for {}</h2>
        <ul>
            <li><strong>Stocks:</strong> 40%</li>
            <li><strong>Bonds:</strong> 20%</li>
            <li><strong>Real Estate:</strong> 20%</li>
            <li><strong>Mutual Funds:</strong> 20%</li>
        </ul>
        """.format(name)
    else:
        return """
        <h2>Investment Recommendations for {}</h2>
        <ul>
            <li><strong>Stocks:</strong> 20%</li>
            <li><strong>Bonds:</strong> 40%</li>
            <li><strong>Real Estate:</strong> 20%</li>
            <li><strong>Mutual Funds:</strong> 20%</li>
        </ul>
        """.format(name)

# Streamlit app
def main():
    st.title('Investment Recommendation App')

    # Get user inputs
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    job_type = st.text_input('Job Type')
    monthly_income = st.number_input('Monthly Income', min_value=0, value=1000)
    risk_appetite = st.selectbox('Risk Appetite', ['High', 'Medium', 'Low'])

    if st.button('Get Recommendations'):
        # Generate recommendations
        recommendations = gen_ai_investment_recommendations(name, age, job_type, monthly_income, risk_appetite)
        st.markdown(recommendations, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
