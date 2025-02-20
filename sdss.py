import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("./asset/sdss_100k_galaxy_form_burst.csv", skiprows=1, header=0)

#Getting to know the data

print(df.info())
print(df.head(5))
print(df.shape)
print(df.columns)
print(df.describe())
