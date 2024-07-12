import os
import pandas as pd 
import joblib

companyDict=joblib.load(r'C:\Users\91860\OneDrive\Desktop\Financial_Analysis\Financial_Analysis\stock_price_predictor\company')
# company_name = st.selectbox("Select Company", list(companyDict.keys()))
# company_name =
# company_ticker = companyDict[company_name]

df = pd.DataFrame()
df['Ticker'] = companyDict.values()
df['Name' ] = companyDict.keys()

df.to_csv('xyz.csv')
