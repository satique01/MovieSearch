import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch free streaming movie websites
def get_free_movie_sites():
    # A list of legal websites that offer free movies
    free_sites = [
        {
            "name": "YouTube Movies (Free Section)",
            "url": "https://www.youtube.com/feed/storefront?bp=ogUCKAI%3D",
            "description": "YouTube has a collection of movies available for free with ads."
        },
        {
            "name": "Tubi TV",
            "url": "https://tubitv.com/",
            "description": "A free streaming service with a large collection of movies and shows supported by ads."
        },
        {
            "name": "Peacock TV",
            "url": "https://www.peacocktv.com/",
            "description": "Peacock offers a free tier with access to thousands of hours of movies and shows."
        },
        {
            "name": "Pluto TV",
            "url": "https://pluto.tv/",
            "description": "Pluto TV offers live TV channels and on-demand movies for free."
        },
        {
            "name": "Crackle",
            "url": "https://www.crackle.com/",
            "description": "Sony's Crackle provides free movies and TV shows supported by ads."
        }
    ]
    return free_sites

# Function to find Netflix's free trial page (if available)
def find_netflix_free_trial():
    url = "https://www.netflix.com/"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

# Streamlit App Layout
st.title("Find Legal Free Movie Streaming Options")
st.write("This app helps you discover websites that offer **legal** free streaming movies. Explore and enjoy free content from these platforms.")

# Display free movie streaming options
st.subheader("Free Movie Streaming Websites:")
free_sites = get_free_movie_sites()
for site in free_sites:
    st.write(f"### [{site['name']}]({site['url']})")
    st.write(site['description'])

# Check for Netflix free trial page
st.subheader("Netflix Free Trial:")
netflix_trial_url = find_netflix_free_trial()
if netflix_trial_url:
    st.write(f"Netflix free trial might be available [here]({netflix_trial_url}).")
else:
    st.write("Netflix free trial is not available at the moment.")

st.write("**Note**: This app only lists legal options for free movies and does not promote piracy or illegal streaming.")
