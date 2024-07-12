# # main_app.py
# import streamlit as st
# from portfolio_optimizer import portfolio_opt
# from stock_price_predictor import stock_predictor
# # Define the different apps
# def stock_predictor1():
#     # st.title('Stock Predictor')
#     stock_predictor.main_page()
#     # Add your stock predictor code here

# def portfolio_optimization():
#     # st.title('Portfolio Optimization')
#     portfolio_opt.main_page()
#     # Add your portfolio optimization code here

# def main():
#     st.sidebar.title('Navigation')
#     app_mode = st.sidebar.radio('Choose an app', ['Home', 'Stock Predictor', 'Portfolio Optimization'])
    
#     if app_mode == 'Home':
#         st.title("Ultimate Financial Analytics Suite")
#         st.write("""
#         Welcome to the Ultimate Financial Analytics Suite!

#         Embark on a transformative journey with our advanced financial analytics tools designed to enhance your investment strategy and portfolio management. Whether you’re aiming to predict stock prices with precision or optimize your investment portfolio for maximum returns, we provide the insights and capabilities you need to succeed.

#         Our **Stock Price Predictor** is your go-to solution for forecasting closing prices, offering you a strategic edge in making informed investment decisions. Meanwhile, our **Portfolio Optimization App** is tailored to help you fine-tune your portfolio, catering to various criteria such as maximizing returns, achieving target returns, and managing risk tolerance.

#         Join us in navigating the dynamic world of finance with confidence and clarity. Explore our comprehensive tools and unlock the full potential of your financial aspirations.
#         """)
#         st.write('Use the sidebar to navigate between apps.') 
#     elif app_mode == 'Stock Predictor':
#         stock_predictor1()
#     elif app_mode == 'Portfolio Optimization':
#         portfolio_optimization()

# if __name__ == '__main__':
#     main()
import streamlit as st
from portfolio_optimizer import portfolio_opt
from stock_price_predictor import stock_predictor

# Initialize session state if not already initialized
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def stock_predictor1():
    stock_predictor.main_page()

def portfolio_optimization():
    portfolio_opt.main_page()

def main():

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button('Home'):
            st.session_state.page = 'home'
    
    with col2:
        if st.button('Stock Predictor'):
            st.session_state.page = 'stock-predictor'
    
    with col3:
        if st.button('Portfolio Optimization'):
            st.session_state.page = 'portfolio-optimization'
    
    # Render content based on the current page
    if st.session_state.page == 'home':
        st.title("Ultimate Financial Analytics Suite")
        st.write("""
        Welcome to the Ultimate Financial Analytics Suite!

        Embark on a transformative journey with our advanced financial analytics tools designed to enhance your investment strategy and portfolio management. Whether you’re aiming to predict stock prices with precision or optimize your investment portfolio for maximum returns, we provide the insights and capabilities you need to succeed.

        Our **Stock Price Predictor** is your go-to solution for forecasting closing prices, offering you a strategic edge in making informed investment decisions. Meanwhile, our **Portfolio Optimization App** is tailored to help you fine-tune your portfolio, catering to various criteria such as maximizing returns, achieving target returns, and managing risk tolerance.

        Join us in navigating the dynamic world of finance with confidence and clarity. Explore our comprehensive tools and unlock the full potential of your financial aspirations.
        """)
    
    elif st.session_state.page == 'stock-predictor':
        stock_predictor1()
    
    elif st.session_state.page == 'portfolio-optimization':
        portfolio_optimization()

if __name__ == '__main__':
    main()
