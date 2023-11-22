import streamlit as st
import mysql.connector
# Connect to the MySQL database
mydb = mysql.connector.connect(
        host="139.5.147.31",
        port="3306",
        user="trong",
        password="c757GL28zN",
        database="trong"
)
if mydb.is_connected():
    st.title("pass")  # If connected successfully
    mycursor = mydb.cursor()
else :
    st.title("Connection Error:", err)
