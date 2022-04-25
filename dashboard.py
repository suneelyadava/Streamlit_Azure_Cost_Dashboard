from datetime import datetime, date
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv('AzureUsage/last.csv')
df["Date"] = pd.to_datetime(df["Date"])
#st.write(df["Date"].tail())
last_upload = df["Date"].max()

services = df["ServiceName"].unique()

headerSection = st.header('Dashboard')
mainSection = st.container()
leftNavBar = st.sidebar

with leftNavBar:
    #Last upload
    if str(date.today()) + ' 00:00:00' == str(last_upload):
        st.success(f"Last upload: {last_upload}")
    else:
        st.warning(f"Last upload: {last_upload}")
    #Select service
    selected_service = st.selectbox('Pick a service', services)


service_df = df[df['ServiceName'] == selected_service]
sorted_service_df = service_df.sort_values(by="Date", ascending=True)
cost_service_per_day_df = sorted_service_df.groupby(["Date"]).sum().reset_index()
cost_service_per_day_df.set_index("Date", inplace=True)

with mainSection:
    left_col, right_col = st.columns(2)
    with left_col:
        st.write('Cost')
        st.line_chart(cost_service_per_day_df['Cost'])
    with right_col:
        st.write('Cumulative Sum')
        st.line_chart(cost_service_per_day_df['Cost'].cumsum())