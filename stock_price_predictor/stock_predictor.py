import streamlit as st
from streamlit_lottie import st_lottie
import requests
from .pages import predict_closing, predict_range


def main_page():
    # st.set_page_config(
    #     page_title="💸Homepage",
    #     initial_sidebar_state="expanded",
    #     layout="wide"
    # )

    st.sidebar.title("Stock Prediction")
    option = st.sidebar.selectbox("Go to", ["Home", "Closing Price Prediction", "Predict Range"])

    if( option == "Home"):

        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        col1,col2=st.columns(2)

        with col1:
            st.title('Welcome to Stock Price Predictor!')
            st.write("Presenting Stock Price Predictor - The Golden Path to Stock Prognostication.We are here to assist you every step of the way, providing invaluable insights and empowering you to make informed decisions. Additionally, our expertise extends to predicting closing prices, equipping you with a strategic advantage in optimizing your investment strategies. Let us be your trusted companion on this thrilling journey, as we empower you to unlock the full potential of your financial aspirations.")
        with col2:
            stocks=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_kuhijlvx.json")
            st_lottie(stocks)
    elif option == "Closing Price Prediction":
        predict_closing.main_page()
    elif option == "Predict Range" : 
        predict_range.main_page()