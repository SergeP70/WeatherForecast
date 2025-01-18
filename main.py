# Weather Forecast
import streamlit as st
import plotly.express as px
from api import get_data

# Design the Title, input and slider
st.title("Weather Forecast for the next days")
place = st.text_input("Place:", value='London')
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Get the data and return it as a list of dicts
try:
    conditions = get_data(place, days)
except KeyError:
    st.error('Place was not found, enter another place')
else:
    # Create a temperature plot or display the sky icons
    if option == 'Temperature':
        # Make a list of the dates and the corresponding temperatures
        # and return this to the X- and Y-axis
        figure = px.line(x=[condition['date'] for condition in conditions],
                         y=[condition['temperature'] for condition in conditions],
                         labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(figure)
    else:
        # Place the sky icons next to each other
        cols = st.columns(8)
        cols_index = 0

        for condition in conditions:
            kind = condition['kind']
            img_label = condition['date']
            with cols[cols_index]:
                st.image(f'https://openweathermap.org/img/wn/{kind}@2x.png', width=115, caption=img_label)
                cols_index += 1
                if cols_index >= len(cols):
                    cols_index = 0

