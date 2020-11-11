from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/films/table')
def film_table():
    movies = []
    with open('film_list.txt', 'r') as f:
        lines = f.readlines()

    stars = request.values.get("stars","-1")
    for line in lines:
        movie = line.split(', ')
        if stars != '-1' and movie[1].strip() != stars:
                continue
        movie_dict = {'title' : movie[0], 'stars' : movie[1].strip()}
        movies.append(movie_dict)
    return render_template('film_list.html', movies=movies)

@app.route('/films/list')
def film_list():
    return send_from_directory('films', 'list.html')

@app.route('/films/submit')
def film_submit():
    return send_from_directory('films', 'submit.html')

@app.route('/films/submit', methods=['POST'])
def film_add():
    title = request.form.get('film')
    stars = request.form.get('stars') 

    with open('film_list.txt', 'a+') as f:
        f.write(f'{title}, {stars}\n')
    
    newfilm = [{'title' : title, 'stars' : stars}]

    return render_template('new_film.html', newfilm=newfilm)