import streamlit
import pandas as pd
import requests
import snowflake.connector

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

streamlit.header("Fruityvice Fruit Advice!")


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

fruityvice_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruityvice_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruityvice_choice )
fruityvice_df = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_df)

streamlit.header("The Fruit load list conatins:")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list;")
my_data_row = my_cur.fetchall()
streamlit.text("Fruit Load List:")
streamlit.dataframe(my_data_row)

list = streamlit.text_input("What fruit would you like to add?")
streamlit.write("Thanks for adding", list)
