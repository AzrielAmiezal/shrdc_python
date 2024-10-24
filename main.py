import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Main",
    page_icon="🎨",  # You can add an emoji or icon here
    layout="wide"
)

# CSS for custom fonts, colors, and more styling
page_style = """
    <style>
        /* Style for the main content */
        h1 {
            font-family: 'Arial', sans-serif;
            color: #4CAF50;
            font-size: 48px;
            text-align: center;
        }

        /* Style for the sidebar */
        .sidebar .sidebar-content {
            background-color: #f0f0f5;
            padding: 20px;
        }
        .sidebar .sidebar-content h2 {
            color: #ff6347;
            font-family: 'Courier New', monospace;
        }

        /* Style for body text */
        p {
            font-family: 'Verdana', sans-serif;
            color: #333;
            font-size: 20px;
        }

        /* Customize Streamlit components */
        .stButton>button {
            background-color: #ff6347;
            color: white;
            border-radius: 12px;
            border: none;
            font-size: 20px;
        }

        .stButton>button:hover {
            background-color: #ff4500;
        }
    </style>
"""

# Apply the CSS styles using markdown
st.markdown(page_style, unsafe_allow_html=True)

# Main page content with custom styling
st.markdown('# This is the main page...')

# Sidebar content with custom styling
st.sidebar.write('main page')

# Example button
if st.button('Click Me!'):
    st.write('Button clicked!')
