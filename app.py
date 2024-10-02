import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('notebooks/vehicles_us.csv')

# Fill in missing model year with median
df['model_year'] = df.groupby(['model'])['model_year'].transform(lambda x:  x.fillna(x.median()))

#fill in missing cylinder amount with median
df['cylinders'] = df.groupby(['model','model_year'])['cylinders'].transform(lambda x:  x.fillna(x.median()))

st.title('Vehicle Odometer Histogram')

# Create a histogram using Plotly Express
fig = px.histogram(df, x='odometer', title='Distribution of Vehicle Odometer')

# Display the histogram in Streamlit
st.plotly_chart(fig)
st.title('Odometer vs Price')

# Create a histogram using Plotly Express
fig1 = px.scatter(df, x='odometer', y='price')

# Display the histogram in Streamlit
st.plotly_chart(fig1)