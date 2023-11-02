import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner!!")

streamlit.header("Breakfast Menu")
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie')

streamlit.header("Build your own Smoothie!!")

fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(fruit_list)
