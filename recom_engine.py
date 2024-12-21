import pandas as pd
import numpy as np

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# %%
credits

# %%
movies

# %%
print(movies.info())


# %%
credits.info()

# %%
merged_data = movies.merge(credits, on="title", how="inner")
merged_data

# %%
merged_data.columns

# %%
main_dataset = merged_data[['movie_id','title','overview','keywords','genres','cast','crew']]
main_dataset

# %%
import ast


def conversion(text):
    data = []
    for i in ast.literal_eval(text):
        data.append(i['name'])

    return data


# %%
main_dataset['keywords'] = main_dataset['keywords'].apply(conversion)
main_dataset['genres'] = main_dataset['genres'].apply(conversion)
# main_dataset['keywords'] = main_dataset['keywords'].apply(conversion)

# %%
def convert(text):
    top_cast_names = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter <3:
            top_cast_names.append(i['name'])
        counter=counter+1
    
    
    return top_cast_names

# %%
main_dataset['cast'] = main_dataset['cast'].apply(convert)


# %%
def crew(text):
    director_names = []
    for i in ast.literal_eval(text):
        if i['job']=='Director':
        
            director_names.append(i['name'])
    
    return director_names

# %%
main_dataset['crew'] = main_dataset['crew'].apply(crew)

# %%
main_dataset

# %%
main_dataset = main_dataset.dropna()

# %%
main_dataset['overview'] = main_dataset['overview'].apply(lambda x :x.split())

# %%
# write a for loop to removing spaces from a word/sentences
def remove(data):
    words = []
    for word in data:
        words.append(word.replace(" ", ""))
    return words

# %%
main_dataset['crew'] = main_dataset['crew'].apply(remove)
main_dataset['cast'] = main_dataset['cast'].apply(remove)
main_dataset['overview'] = main_dataset['overview'].apply(remove)
main_dataset['genres'] = main_dataset['genres'].apply(remove)

# %%
main_dataset

# %%
main_dataset['tag'] = main_dataset['overview']+main_dataset['keywords']+main_dataset['genres']+main_dataset['crew']+main_dataset['cast']
new_dataset = main_dataset[['movie_id','title','tag']]
new_dataset

# %%
new_dataset['tag'] = new_dataset['tag'].apply(lambda x: " ".join(x))


# %%
new_dataset

# %%
new_dataset['tag'] = new_dataset['tag'].apply(lambda x: x.lower())

# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

CV = CountVectorizer(max_features=5000,stop_words='english')

# %%
vectors = CV.fit_transform(new_dataset['tag']).toarray()

# %%
# cosine similarity
from sklearn.metrics.pairwise import cosine_similarity

cosine = cosine_similarity(vectors)

# %%
cosine

# %%
new_dataset[new_dataset['title'] == 'John Carter' ].index[0]

# %%
def recommendation(movie):
    index = new_dataset[new_dataset['title'] == movie ].index[0]
    distances = sorted(list(enumerate(cosine[index])),reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:  # Start from 1 to exclude the movie itself
        recommended_movies.append(new_dataset.iloc[i[0]]['title'])
        print(recommended_movies)
    return recommended_movies
    # for i in distances[1:6]:
    #     print(new_dataset.iloc[i[0]]['title'])
    #     return new_dataset.iloc[i[0]]['title']



# %%
# recommendation(movie)


