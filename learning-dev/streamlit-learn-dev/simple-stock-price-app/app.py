import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app
         

shown are the stock **closing price** and volume of google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start = '2014-10-20', end ='2020-10-20')

st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)

