import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st

start='2010-01-01'
end='2022-5-31'

st.title('stock price prediction')
user_input=st.text_input('Enter Stock Ticker','AAPL')
df=data.DataReader('AAPL','yahoo',start,end)
df.head()

#describing data
st.subheader('Data from 2010-2022')
st.write(df.describe())

#Graph patterns
st.subheader('closing Price vs Time chart')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)