import spacy
nlp = spacy.load('en_core_web_md')

m = open("movies.txt","r")
movie_similarity = []
movies = {}

sentance_to_compare =  """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk 
can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery 
and trained as a gladiator."""


def similar_movie(): #function which compares each movie title to the description of the movie above and returns the most similar title next
    
    model_sentance = nlp(sentance_to_compare)

    for line in m:
        similarity = nlp(line).similarity(model_sentance)
        movie_similarity.append(similarity)     # using lists and dictionaries to return the most similar movie title
        format = line.split(":")
        movies[similarity] = format[0]

    print(movies[max(movie_similarity)])
    m.close()