import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("clean_netflix_data.csv")

# Page title
st.title("🎥 Netflix Explorer App")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

type_filter = st.sidebar.selectbox("Select Type", options=["All", "Movie", "TV Show"])
country_filter = st.sidebar.multiselect("Select Country", options=data['country'].dropna().unique())
genre_filter = st.sidebar.multiselect("Select Genre", options=data['listed_in'].dropna().unique())
director_filter = st.sidebar.multiselect("Select Director", options=data['director'].dropna().unique())
search_title = st.sidebar.text_input("Search Title")

# Apply filters
filtered = data.copy()

if type_filter != "All":
    filtered = filtered[filtered['type'] == type_filter]

if country_filter:
    filtered = filtered[filtered['country'].isin(country_filter)]

if genre_filter:
    filtered = filtered[filtered['listed_in'].isin(genre_filter)]

if director_filter:
    filtered = filtered[filtered['director'].isin(director_filter)]

if search_title:
    filtered = filtered[filtered['title'].str.contains(search_title, case=False, na=False)]

# Display result
st.write(f"### Showing {len(filtered)} results")
st.dataframe(filtered[['title', 'type', 'director', 'country', 'listed_in', 'release_year', 'rating', 'duration']])
