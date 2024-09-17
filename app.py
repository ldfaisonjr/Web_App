import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Odometer Histogram')

# Create a histogram using Plotly Express
fig = px.histogram(df, x='odometer', title='Distribution of Vehicle Odometer')

# Display the histogram in Streamlit
st.plotly_chart(fig)