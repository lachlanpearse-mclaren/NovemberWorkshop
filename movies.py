import argparse

parser = argparse.ArgumentParser(description='Collect movie ratings.')
parser.add_argument('--film-name', help='Enter the name of a film.')
parser.add_argument('--stars', help='Give the film a star rating')

args = parser.parse_args()

with open("film_list.txt", 'a+') as f:
    f.write(f'{args.film_name}, {args.stars}\n')