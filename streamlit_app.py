import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time,datetime
st.header('st.slider')
st.subheader('Slider')
age=st.slider('How old are you?',0,130,25)
st.write("I'm ",age,'years old')
