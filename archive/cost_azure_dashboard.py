import streamlit as st
import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.button('Refresh')

date = st.date_input(
     "Pick last updated file using date picker",
     datetime.date(2022, 4, 15))
#st.write('Selected Date :', d.month, d.day, d.year)

# load dataframe
df = pd.read_csv('AzureUsage/' + str(date.day) + '_' + str(date.month) + '_' + str(date.year) + '.csv')

#Select service ================
services = df['ServiceName'].unique()

selected_service = st.selectbox(
     'Pick a service',
     services)

service_df = df[df['ServiceName'] == selected_service]
service_df["Date"] = pd.to_datetime(service_df["Date"])
sorted_service_df = service_df.sort_values(by="Date", ascending=True)
grouped_by_date_service_df = sorted_service_df.groupby(["Date"]).sum()
grouped_by_date_service_df = grouped_by_date_service_df.reset_index()
processed_service_df = grouped_by_date_service_df['Cost']

st.write(grouped_by_date_service_df)

st.line_chart(processed_service_df.cumsum().to_list())
st.line_chart(processed_service_df.to_list())

year_service_df = sorted_service_df[sorted_service_df['Date'].dt.year == 2022]
month_service_df = year_service_df[year_service_df['Date'].dt.month == 4]

st.write(month_service_df)
#st.line_chart(processed_service_df_4_2022.to_list())


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.plot(grouped_by_date_service_df['Date'], grouped_by_date_service_df['Cost'])

st.pyplot(fig)