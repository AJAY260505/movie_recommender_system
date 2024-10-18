import streamlit as st
import pickle
import os
import numpy as np
import requests
import streamlit.components.v1 as components

# Function to load and combine all similarity chunks
def load_similarity_chunks(folder_path):
    similarity_chunks = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.pkl'):
            with open(os.path.join(folder_path, filename), 'rb') as file:
                chunk = pickle.load(file)
                similarity_chunks.append(chunk)
    # Combine all chunks into a single array (adjust as needed)
    return np.vstack(similarity_chunks)  # Use appropriate method to combine based on your data structure

# Load similarity data from the chunks folder
similarity = load_similarity_chunks("similarity_chunks")

# Load movies list from local pickle file
try:
    movies = pickle.load(open("movies_list.pkl", 'rb'))
    movies_list = movies['title'].values
except Exception as e:
    st.error(f"Error loading movies list: {e}")
    movies_list = []

# Display header
st.header("Movie Recommender System")

# Image carousel component (custom component)
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

# Function to fetch poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=18602822affde612b4ba33802ff8b417&language=en-US"
    try:
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            st.warning(f"No poster available for movie ID {movie_id}.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None

# Pre-fetching posters for a list of movie IDs (sample data)
imageUrls = [
    fetch_poster(1632), fetch_poster(299536), fetch_poster(17455),
    fetch_poster(2830), fetch_poster(429422), fetch_poster(9722),
    fetch_poster(13972), fetch_poster(240), fetch_poster(155),
    fetch_poster(598), fetch_poster(914), fetch_poster(255709),
    fetch_poster(572154)
]

# Filter out None values from imageUrls
imageUrls = [url for url in imageUrls if url is not None]

# Display the image carousel component
if imageUrls:
    imageCarouselComponent(imageUrls=imageUrls, height=200)

# Dropdown to select a movie
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

# Function to recommend movies
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []
        recommend_poster = []
        # Fetch top 5 recommendations excluding the selected movie
        for i in distance[1:6]:
            movie_id = movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]].title)
            recommend_poster.append(fetch_poster(movie_id))
        return recommend_movie, recommend_poster
    except IndexError:
        st.error(f"Movie '{movie}' not found in dataset.")
        return [], []
    except Exception as e:
        st.error(f"Error in recommendation process: {e}")
        return [], []

# Button to trigger movie recommendations
if st.button("Show Recommend"):
    if similarity is not None and selectvalue:
        movie_name, movie_poster = recommend(selectvalue)
        # Display recommended movies and posters in columns
        if movie_name:
            col1, col2, col3, col4, col5 = st.columns(5)
            cols = [col1, col2, col3, col4, col5]
            for idx, col in enumerate(cols):
                if idx < len(movie_name):
                    with col:
                        st.text(movie_name[idx])
                        st.image(movie_poster[idx] if movie_poster[idx] else "https://via.placeholder.com/150")
        else:
            st.warning("No recommendations available.")
    else:
        st.error("Similarity data or movie selection is missing.")
