from flask import Flask
from flask import send_from_directory
from flask import render_template

app = Flask(__name__)

@app.route('/films/table')
def film_table():
    movies = []
    with open('film_list.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        movie = line.split(', ')
        movie_dict = {'title' : movie[0], 'stars' : movie[1].strip()}
        movies.append(movie_dict)
    return render_template('film_list.html', movies=movies)

@app.route('/films/list')
def film_list():
    return send_from_directory('films', 'list.html')