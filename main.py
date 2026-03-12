import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

st.title("Stock Price Viewer")

# user input
stock = st.sidebar.text_input("Enter stock symbol", "AAPL")

if stock:
    st.write(f"Showing data for {stock}")
    tickerData = yf.Ticker(stock)
    df = tickerData.history(start="2015-01-01", end="2026-01-01")
    
    if df.empty:
        st.error("Invalid stock symbol or no data available")
        st.stop()
    
    st.line_chart(df.Close)
    st.line_chart(df.Volume)

    download_button = st.sidebar.download_button(label='Сохранить CSV файл', 
                   data=df.to_csv(), 
                   file_name='data.csv')
    
    uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(5))
    else:
        st.stop()