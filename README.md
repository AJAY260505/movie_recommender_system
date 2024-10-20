# Movie Recommender System

This is a web-based movie recommendation system built using **Streamlit**. It recommends movies based on user preferences using movie similarity data and displays movie posters fetched from The Movie Database (TMDb) API.

## Features
- **Movie Recommendation**: Get personalized movie recommendations by selecting a movie from the dropdown.
- **Poster Display**: Movie posters are dynamically fetched and displayed alongside recommendations.
- **Interactive UI**: Easy-to-use interface with dropdowns and buttons for interaction.
- **Custom Image Carousel**: A carousel of movie posters is displayed using a custom component.

## Technologies Used
- **Streamlit**: For building the web interface.
- **Pickle**: For loading pre-processed movie similarity data.
- **The Movie Database (TMDb) API**: To fetch movie posters dynamically.
- **Python 3.x**: Primary programming language used.
- **NumPy**: Used for handling similarity matrices.
- **Custom Components**: Streamlit’s component integration for custom features like image carousels.

## How It Works
1. **Movie Selection**: The app displays a dropdown of movie titles from which users can select one.
2. **Fetching Recommendations**: After selecting a movie, the app uses a similarity matrix (stored in chunks as pickle files) to find and display similar movies.
3. **Poster Display**: Posters for both the selected and recommended movies are fetched from the TMDb API and displayed.
4. **Image Carousel**: A custom component that displays movie posters in a carousel format at the top.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ajay260505/movie_recommender_system.git
   cd movie_recommender_system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the `similarity_chunks` folder containing the similarity data is present in the root directory of the project.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## File Structure
- `app.py`: The main application script.
- `movies_list.pkl`: Pickle file containing the list of movies and their metadata.
- `similarity_chunks/`: Folder containing the pre-computed similarity matrix chunks.
- `frontend/public/`: Contains assets for custom components, such as the image carousel.

## API Setup
This app uses the **TMDb API** to fetch movie posters. You will need an API key from [TMDb](https://www.themoviedb.org/documentation/api).

Replace the placeholder API key in the `fetch_poster` function inside `app.py`:
```python
api_key = "your_tmdb_api_key"
```

## Example Usage
1. Select a movie from the dropdown menu.
2. Click on the "Show Recommend" button to display five similar movies along with their posters.

## Screenshots
*Include screenshots of the app UI here.*

## Future Enhancements
- Add filtering options by genre, year, or ratings.
- Integrate collaborative filtering or hybrid recommendation systems for more accurate suggestions.
- Improve the UI/UX by enhancing the design and user interaction.
- Implement a search bar for quicker movie selection.
