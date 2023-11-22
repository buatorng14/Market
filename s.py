import streamlit as st
import mysql.connector

try:
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="139.5.147.31",
        port="3306",
        user="trong",
        password="c757GL28zN",
        database="trong",
        ssl_disabled=True
    )
    if mydb.is_connected():
        st.write("pass")  # If connected successfully
        mycursor = mydb.cursor()
except mysql.connector.Error as err:
    st.write("Connection Error:", err)
