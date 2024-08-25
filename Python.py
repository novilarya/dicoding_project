import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_monthly_rent(day_df):
    monthly_rent_df = day_df.resample(rule='M', on='dteday').agg({
      "cnt": "sum"
    })

    monthly_rent_df.index = monthly_rent_df.index.strftime('%B')

    monthly_rent_df = monthly_rent_df.reset_index()

    monthly_rent_df.rename(columns={
        "cnt": "rent_count"
    }, inplace=True)

    return monthly_rent_df

def create_monthly_casual_rent(day_df):
    monthly_casual_rent_df = day_df.resample(rule='M', on='dteday').agg({
        "casual": "sum"
    })

    monthly_casual_rent_df.index = monthly_casual_rent_df.index.strftime('%B')

    monthly_casual_rent_df = monthly_casual_rent_df.reset_index()

    monthly_casual_rent_df.rename(columns={
        "casual": "casual_rent_count"
    }, inplace=True)

    return monthly_casual_rent_df

def create_monthly_registered_rent(day_df):
    monthly_registered_rent_df = day_df.resample(rule='M', on='dteday').agg({
        "registered": "sum"
    })

    monthly_registered_rent_df.index = monthly_registered_rent_df.index.strftime('%B')

    monthly_registered_rent_df = monthly_registered_rent_df.reset_index()

    monthly_registered_rent_df.rename(columns={
        "registered": "registered_rent_count"
    }, inplace=True)

    return monthly_registered_rent_df

dayy_df = pd.read_csv("day_update.csv")

dayy_df['dteday'] = pd.to_datetime(dayy_df['dteday'])
# monthly_rent_df = 
# monthly_casual_rent_df = 
# monthy_registered_rent_df = 

st.header('Bike Sharing Dashboard :sparkles:')

st.subheader('Monthly Rent Count')
fig, ax = plt.subplots()
sns.barplot(
    x='dteday',
    y='rent_count',
    data=create_monthly_rent(dayy_df),
    color='#72BCD4')
plt.xlabel('Month')
plt.ylabel('Rent Count')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Monthly Casual Rent Count')
fig, ax = plt.subplots()
sns.barplot(
    x='dteday',
    y='casual_rent_count',
    data=create_monthly_casual_rent(dayy_df),
    color='#72BCD4')
plt.xlabel('Month')
plt.ylabel('Rent Count')
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader('Monthly Registered Rent Count')
fig, ax = plt.subplots()
sns.barplot(
    x='dteday',
    y='registered_rent_count',
    data=create_monthly_registered_rent(dayy_df),
    color='#DD5746')
plt.xlabel('Month')
plt.ylabel('Rent Count')
plt.xticks(rotation=45)
st.pyplot(fig)
