import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
import datetime
import yfinance as yf
import tensorflow as tf
from tensorflow.keras.layers import GRU
from tensorflow.keras.utils import get_custom_objects
from streamlit_lottie import st_lottie
import requests
import os 

def main_page():
    # Set Streamlit page configuration
    # st.set_page_config(page_title="📈Closing Price")

    # Function to load Lottie animations
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Load and display Lottie animations
    col1, col2 = st.columns(2)

    with col1:
        stocks = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_dwivte2j.json")
        st_lottie(stocks)

    with col2:
        stocks = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_fgba6oco.json")
        st_lottie(stocks)

    # Display title and description
    st.title('Predict Stock Price of any Company')
    st.write('You can now know the closing price of any Company on the next day! You are just 1 click away!')
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'stock_price_predictor/scaler.pkl')

    # scaler=joblib.load(r'stock_price_predictor\scaler.pkl')
    scaler = joblib.load(file_path)

    # Custom GRU layer class
    class CustomGRU(GRU):
        def __init__(self, *args, **kwargs):
            kwargs.pop('time_major', None)  # Remove 'time_major' if present
            super(CustomGRU, self).__init__(*args, **kwargs)

    get_custom_objects().update({'GRU': CustomGRU})

    # model_path = r'stock_price_predictor\gru_model.h5'
    cwd = os.getcwd()

    model_path = os.path.join(cwd , 'stock_price_predictor\gru_model.h5')
    gru_model = tf.keras.models.load_model(model_path, custom_objects={'GRU': CustomGRU})

   
    # Load company data
    company_path = os.path.join(cwd , 'stock_price_predictor\company')
    companyDict=joblib.load(company_path )
    company_name = st.selectbox("Select Company", list(companyDict.keys()))
    company_ticker = companyDict[company_name]

     # Inverse transformation function
    def inverse(a, b):
        m1 = b.min()
        m2 = b.max()
        return a * (m2 - m1) + m1


    # Function to predict stock price
    def predict():
        # Extracting the data of the company entered by user
        ticker_symbol = company_ticker.upper() + ".NS"
        days_back = 15
        interval = '15m'
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.datetime.now() - datetime.timedelta(days=days_back)).strftime('%Y-%m-%d')
        company_data = yf.download(ticker_symbol, start=start_date, end=end_date, interval=interval)['Close']
        
        # Transform data
        df = scaler.transform(np.array(company_data).reshape(-1, 1))
        new_data = pd.DataFrame({'Close': df.flatten()})
        
        def create_dataset(X, y, time_steps=1):
            Xs, ys = [], []
            for i in range(len(X) - time_steps):
                Xs.append(X.iloc[i:(i + time_steps)].values)
                ys.append(y.iloc[i + time_steps])
            return np.array(Xs), np.array(ys)

        X_test, y_test = create_dataset(new_data[['Close']], new_data[['Close']], 60)
        
        # Prepare data for prediction
        new_x_test = np.array(new_data[['Close']].iloc[-60:]).reshape(1, 60, 1)
        
        # Predict the next day's closing price
        pred = gru_model.predict(new_x_test)
        next_predicted = inverse(pred, company_data)[0]
        return next_predicted

    # Trigger prediction on button click
    if st.button('Predict Closing Price'):
        predicted_price = predict()
        if isinstance(predicted_price, np.ndarray):
            predicted_price = predicted_price.item()
        st.write('The expected Closing Price tomorrow is ' + str(round(predicted_price, 2)))
