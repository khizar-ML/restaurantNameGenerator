import streamlit as st
from langchain_helper import generateRestaurantName

st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Chinese", "Mexican","Pakistani","Thai","French","Japanese"))



if cuisine:
    response = generateRestaurantName(cuisine)
    st.header(response['RestaurantName'])
    menu_items = response['PopularDishes'].split(", ")
    st.subheader("Sample Menu Items:")
    for item in menu_items:
        st.write(f"- {item}")
    
