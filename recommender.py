import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a0580b4696df1b46e2da59db5ef66cf9'.format(movie_id))   
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  movie_idex = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_idex]
  movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
  recommeded_movies = []
  recommended_movie_poster = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id

    recommeded_movies.append(movies.iloc[i[0]].title)

    recommended_movie_poster.append(fetch_poster(movie_id))

  return recommeded_movies , recommended_movie_poster

st.title("MOVIE RECOMMENDER SYSTEM")

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)


similarity =  pickle.load(open("similarity.pkl", "rb"))  

selected_movie_name = st.selectbox('Select an movie:', movies['title'].values)

if st.button('RECOMMEND'):
    names , posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
       st.header(names[0])
       st.image(posters[0])
    with col1:
       st.header(names[1])
       st.image(posters[1])
    with col1:
       st.header(names[2])
       st.image(posters[2])
    with col1:
       st.header(names[3])
       st.image(posters[3])
    with col1:
       st.header(names[4])
       st.image(posters[4])            