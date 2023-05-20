import streamlit as st
import requests

api = "29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"
url = "https://api.nasa.gov/planetary/apod?api_key=29WQxV6QbiFnP5vPH12jgG5Rm4cuIGHXafi2uEDo"

response = requests.get(url)

with open("iod.jpg", "wb") as file:
    file.write(response.content)