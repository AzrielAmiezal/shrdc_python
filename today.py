import streamlit as st

st.write("Hello guys how are you today???")
st.write("how do I stop this session???")
st.write("try again")

st.write("YP-BDA01")
st.write("SHRDC")
st.write("Python for Data Analytics")
st.write("Azriel Handsome")

import streamlit as st

# Simple HTML element using st.markdown
st.markdown("<h1 style='color:blue;'>Hello, Streamlit!</h1>", unsafe_allow_html=True)

# You can also use basic HTML tags like <p>, <b>, <i>, etc.
st.markdown("<p>This is a paragraph in <b>bold</b> and <i>italic</i>.</p>", unsafe_allow_html=True)

import streamlit as st

# CSS for animation
animation_style = """
<style>
@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}

.fade-in {
    animation: fadeIn 3s ease-in-out;
    font-size: 24px;
    color: red;
}
</style>
"""

# Apply HTML with animation
st.markdown(animation_style, unsafe_allow_html=True)

st.markdown("<div class='fade-in'>My name is Azriel Amiezal and I hate coding</div>", unsafe_allow_html=True)

import streamlit as st

# CSS for moving animation
animation_style = """
<style>
@keyframes move {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.moving-text {
    display: inline-block;
    font-size: 24px;
    color: blue;
    white-space: nowrap;
    animation: move 10s linear infinite;
}
</style>
"""

# Apply the CSS style
st.markdown(animation_style, unsafe_allow_html=True)

# HTML content with the moving animation
st.markdown("<div class='moving-text'>My name is Azriel Amiezal and I hate coding HAHAHAHAHAHAHA</div>", unsafe_allow_html=True)

import streamlit as st

# CSS for the "hacked" effect
animation_style = """
<style>
@keyframes glitch {
    0% { transform: translateX(0); }
    20% { transform: translateX(-10px); }
    40% { transform: translateX(10px); }
    60% { transform: translateX(-10px); }
    80% { transform: translateX(10px); }
    100% { transform: translateX(0); }
}

@keyframes textColorChange {
    0% { color: red; }
    25% { color: white; }
    50% { color: red; }
    75% { color: black; }
    100% { color: red; }
}

.hacked-text {
    font-size: 40px;
    font-weight: bold;
    color: red;
    animation: glitch 0.1s infinite, textColorChange 1s infinite;
    text-align: center;
    margin-top: 20px;
}
</style>
"""

# Apply the CSS style
st.markdown(animation_style, unsafe_allow_html=True)

# Display the "Your computer has been hacked" text with animation
st.markdown("<div class='hacked-text'>Your computer has been hacked!</div>", unsafe_allow_html=True)


import streamlit as st

# Dictionary mapping Malaysian states to their cities
malaysia_data = {
    'Johor': ['Johor Bahru', 'Muar', 'Batu Pahat'],
    'Kedah': ['Alor Setar', 'Sungai Petani', 'Kulim'],
    'Kelantan': ['Kota Bharu', 'Kuala Krai', 'Pasir Mas'],
    'Malacca': ['Malacca City', 'Ayer Keroh', 'Batu Berendam'],
    'Negeri Sembilan': ['Seremban', 'Port Dickson', 'Bahau'],
    'Pahang': ['Kuantan', 'Bentong', 'Temerloh'],
    'Penang': ['George Town', 'Butterworth', 'Bayan Lepas'],
    'Perak': ['Ipoh', 'Taiping', 'Teluk Intan'],
    'Perlis': ['Kangar', 'Padang Besar', 'Arau'],
    'Sabah': ['Kota Kinabalu', 'Sandakan', 'Tawau'],
    'Sarawak': ['Kuching', 'Miri', 'Sibu'],
    'Selangor': ['Shah Alam', 'Petaling Jaya', 'Subang Jaya'],
    'Terengganu': ['Kuala Terengganu', 'Dungun', 'Kemaman']
}

# Multiselect for states
selected_states = st.multiselect('Select one or more states in Malaysia:', list(malaysia_data.keys()))

# Show corresponding cities for the selected states
if selected_states:
    all_cities = []
    for state in selected_states:
        all_cities.extend(malaysia_data[state])
    
    # Display multiselect for cities based on selected states
    selected_cities = st.multiselect(f'Select cities in the selected states:', all_cities)
    
    # Output the selected states and cities
    st.write(f"You selected the following states: {', '.join(selected_states)}")
    st.write(f"You selected the following cities: {', '.join(selected_cities)}")

import streamlit as st

# CSS for interactive logo
logo_style = """
<style>
@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.logo-container {
    text-align: center;
    margin-top: 50px;
}

.logo {
    font-size: 50px;
    font-weight: bold;
    color: #FF6347;
    transition: transform 0.5s;
}

.logo:hover {
    color: #1E90FF;
    transform: scale(1.2);
    animation: rotate 2s infinite;
}
</style>
"""

# Apply the CSS style
st.markdown(logo_style, unsafe_allow_html=True)

# Display the logo
st.markdown("<div class='logo-container'><div class='logo'>Azriel's Logo</div></div>", unsafe_allow_html=True)

import streamlit as st

# Display the image using Streamlit's built-in function
st.image("D:/SHRDC/Python for Data Analytics/Day 4/pic.png", caption="Java vs Python Logos", use_column_width=True)

import streamlit as st

# CSS for interactive image (hover effect)
logo_style = """
<style>
.image-container img {
    width: 400px;
    transition: transform 0.3s ease-in-out;
}
.image-container img:hover {
    transform: scale(1.1); /* Zoom in effect on hover */
}
</style>
"""

# Apply CSS
st.markdown(logo_style, unsafe_allow_html=True)

# Display image with interactive CSS
st.markdown("""
<div class="image-container">
    <img src="https://vytcdc.com.sg/wp-content/uploads/2021/12/java-python.jpg" alt="Java vs Python">
</div>
""", unsafe_allow_html=True)


import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")

st.line_chart(df, x="Household", y="Income")

st.scatter_chart(df, x="Household", y="Income")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")