import streamlit as st
import requests
from datetime import date

api = "29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"
url = "https://api.nasa.gov/planetary/apod?api_key=29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"
today = date.today()

response_nasa = requests.get(url)
data_nasa = response_nasa.json()

st.header(f"Image of the day from NASA on {today}")
st.title(data_nasa["title"])
st.image(data_nasa["url"])
st.write(data_nasa["explanation"])

st.markdown("A project by: Shan Khalam")

