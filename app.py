#### PACKAGES
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt


#### DATA
df = pd.read_csv("supermarket.csv")

#### VISUALIZATIONS
top_stores = pd.DataFrame(data=df.groupby(by='store_area')['store_sales'].sum()).sort_values(by='store_sales', ascending=False).head(10)
low_inventory = pd.DataFrame(data=df.groupby(by='store_id')[['store_id','items_available']].sum()).sort_values(by='items_available', ascending=True).head(5)
avg_customers = round(np.mean(df['daily_customer_count']))
time_now = dt.datetime.now()



# FRONT END 
st.title("Bob's Grocery - Admin Dashboard")
st.text(f'Information updated at:{time_now}')

st.markdown('<h3 style="color:#d92906">Stores with Low Inventory</h3>', unsafe_allow_html=True)
st.table(low_inventory)


st.subheader("Top Performing Sales Areas")
st.bar_chart(data=top_stores)


st.markdown('<h3 style="color:#FFFFFF">Average Daily Number of Customers</h3>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#4dd906;font-size:100px">{avg_customers}</h1>', unsafe_allow_html=True)











