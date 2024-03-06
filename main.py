import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Mateusz Młynarczyk")
    content = """
    Hello, I'm Troley! I'm an aspiring programmer eager to delve into the world of game development. 
    My passion lies in creating immersive and entertaining games, and I'm excited to embark on this journey as a beginner programmer. 
    I look forward to learning and growing in the field, with the ultimate goal of crafting engaging and innovative gaming experiences in the future.
    """
    st.info(content)

st.write("Below you can find some of the apps i have built in Python.")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])