movies = []
with open('film_list.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    movie = line.split(',')
    movie_dict = {'title' : movie[0], 'stars' : movie[1].strip()}
    movies.append(movie_dict)

print(movies)
    