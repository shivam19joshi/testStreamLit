import streamlit as st

def get_investment_recommendation(risk_type):
    if risk_type == 'Low':
        return 'Consider investing in bonds or high-yield savings accounts.'
    elif risk_type == 'Medium':
        return 'Consider a mix of index funds and blue-chip stocks.'
    elif risk_type == 'High':
        return 'Consider investing in individual stocks or cryptocurrencies.'
    else:
        return 'Please select a valid risk type.'

# Streamlit application
def main():
    st.title('Investment Recommendation System')

    # User inputs
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=1, max_value=100)
    contact = st.text_input('Contact')
    risk_type = st.selectbox('Risk Type', ['Low', 'Medium', 'High'])

    if st.button('Get Recommendation'):
        if name and contact and risk_type:
            recommendation = get_investment_recommendation(risk_type)
            st.write(f'Hello {name}, based on your risk tolerance, we recommend the following:')
            st.write(recommendation)
        else:
            st.write('Please fill in all the details.')

if __name__ == '__main__':
    main()
