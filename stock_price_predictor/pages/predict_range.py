import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import GRU
from tensorflow.keras.utils import get_custom_objects
import joblib
import os
import datetime
import time
import yfinance as yf
import pickle
import tensorflow as tf
import json
from streamlit_lottie import st_lottie

def main_page():
        
    # st.set_page_config(
    #     page_title="📈Opening Price"
    # )


    st.title('Predict Stock Price of any Company')
    st.write('/n/n/n')
    st.write('You can now get an idea of what is gonna be the range of  opening price of any company in just a single click./n/n')

    st.write('Disclaimer : The Prediction might take upto a minute. Please be patient')
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'stock_price_predictor/scaler.pkl')

    # scaler=joblib.load(r'stock_price_predictor/scaler.pkl')
    scaler = joblib.load(file_path)

    # Custom GRU layer class
    class CustomGRU(GRU):
        def __init__(self, *args, **kwargs):
            kwargs.pop('time_major', None)  # Remove 'time_major' if present
            super(CustomGRU, self).__init__(*args, **kwargs)

    get_custom_objects().update({'GRU': CustomGRU})

    # model_path = r'stock_price_predictor/gru_model.h5'
    cwd = os.getcwd()

    model_path = os.path.join(cwd , 'stock_price_predictor/gru_model.h5')
    gru_model = tf.keras.models.load_model(model_path, custom_objects={'GRU': CustomGRU})

   
    # Load company data
    company_path = os.path.join(cwd , 'stock_price_predictor/company')
    companyDict=joblib.load(company_path )
    company_name = st.selectbox("Select Company", list(companyDict.keys()))
    company_ticker = companyDict[company_name]

    def inverse(a,b):
        m1=b.min()
        m2=b.max()
        return a*(m2-m1)+m1

    # companyDict=joblib.load(r'stock_price_predictor/company')
    # company_name=st.selectbox("Enter Company Name",list(companyDict.keys()))
    # company_ticker=companyDict[company_name]


    def predict():
        #Extracting the data of the company entered by user 
        ticker_symbol=company_ticker.upper()+".NS"
        days_back=15
        interval='15m'
        end_date=datetime.datetime.now().strftime('%Y-%m-%d')
        start_date=(datetime.datetime.now()-datetime.timedelta(days=days_back)).strftime('%Y-%m-%d')
        company_data=yf.download(ticker_symbol,start=start_date,end=end_date,interval=interval)['Close']
        df=scaler.fit_transform(np.array(company_data).reshape(-1,1))
        new_data=pd.DataFrame()
        df=np.array(df)
        l=[]
        for i in range(df.shape[0]):
            l.append(df[i][0])
        new_data['Close']=l
        new_data=pd.DataFrame(new_data,columns=["Close"])
        def create_dataset(X, y, time_steps=1):
            Xs,ys=[],[]
            for i in range(len(X)-time_steps):
                Xs.append(X.iloc[i:(i+time_steps)].values)
                ys.append(y.iloc[i+time_steps])
            return np.array(Xs),np.array(ys)
        X_test,y_test=create_dataset(new_data[['Close']], new_data[['Close']],60)

        #Fine tuning the overall model trained
        gru_model.fit(X_test,y_test,epochs=10,batch_size=8)

        new_x_test=np.array(new_data[len(company_data)-60:]).reshape(1,60,1)
        pred=gru_model.predict(new_x_test)
        next_predicted=inverse(pred,company_data)[0][0]
        return next_predicted

    if(st.button('Predict Range')):
        predicted_arr=[]
        for layer in gru_model.layers:
            layer.trainable=False
        for i in range(5):
            predicted_price=predict()
            predicted_arr.append(predicted_price)
        predicted_price=np.array(predicted_price)
        mean=predicted_price.mean()
        standard_deviation=predicted_price.std()+0.5643
        st.write('The expected Range of Opening Price tommorow is [ '+str(round(mean-standard_deviation,2))+','+str(round(mean+standard_deviation,2))+' ]')

