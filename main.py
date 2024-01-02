import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, place, days, options, and subheader wigits
st.title("Weather Forcast for the Next Days")
place = st.text_input("Place:").title()
days = st.slider("Forcast Days:", min_value=1, max_value=5,
                 help="Number of days forecasted")
options = st.selectbox("Select data to view:", ("Temperature", "Sky Condition"))
st.subheader(f"{options} for the next {days} days in {place}:")

# Grab data
if place:
    filtered_data = get_data(place, days)

    # Present temperature data
    if options == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (K)"})
        st.plotly_chart(figure)

    # Present sky condition data
    if options == "Sky Condition":
        images = {"Clear": "weather_images/clear.png", "Clouds": "weather_images/cloud.png",
                  "Rain": "weather_images/rain.png", "Snow": "weather_images/snow.png"}
        sky = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky]
        print(sky)
        st.image(image_paths, width=115)
