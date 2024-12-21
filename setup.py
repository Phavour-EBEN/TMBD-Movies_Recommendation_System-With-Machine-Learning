import pickle
import streamlit as st
import requests

# api_key = 'c8af6e57e891249830196163d8d90460'
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c8af6e57e891249830196163d8d90460&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    # print(poster_path)
    full_path ="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommendation(movie):
    index = movies[movies['title'] == movie ].index[0]
    distances = sorted(list(enumerate(similarities[index])),reverse=True, key=lambda x: x[1])
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        #append the recommended movie and its Poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_posters



st.header("Movies recommendation System")
movies = pickle.load(open('artifacts/new_dataset.pkl', 'rb'))
similarities = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button('show recommendations'):
    # Get the index of the selected movie
    recommended_movie_names, reommended_movie_posters = recommendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(reommended_movie_posters[0])
    
    with col2:
        st.text(recommended_movie_names[1])
        st.image(reommended_movie_posters[1])
    
    with col3:
        st.text(recommended_movie_names[2])
        st.image(reommended_movie_posters[2])
    
    with col4:
        st.text(recommended_movie_names[3])
        st.image(reommended_movie_posters[3])
    
    with col5:
        st.text(recommended_movie_names[4])
        st.image(reommended_movie_posters[4])
    
