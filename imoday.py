import streamlit as st
import requests
from datetime import date

api = "29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"
url = "https://api.nasa.gov/planetary/apod?api_key=29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"
today = date.today()

response = requests.get(url)
data = response.json()

st.header(f"Image of the day from NASA on {today}")
st.title(data["title"])
st.image(data["url"])
st.write(data["explanation"])

st.markdown("A project by: Shan Khalam")

