import streamlit as st

st.title("Weather Forcast for the Next Days")
place = st.text_input("Place:").title()
days = st.slider("Forcast Days:", min_value=1, max_value=5,
                 help="Number of days forecasted")
options = st.selectbox("Select data to view:", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}:")
