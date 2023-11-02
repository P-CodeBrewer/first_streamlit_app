import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


streamlit.header("Build your own Smoothie")

fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_list = fruits_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:" ,list(fruits_list.index),['Avocado','Apple'])

fruits_to_show = fruits_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


