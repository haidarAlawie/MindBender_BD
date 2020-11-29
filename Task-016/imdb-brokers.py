import imdb 
from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
moviesDB = imdb.IMDb()


top = moviesDB.get_top250_movies()
results = []
for movie in top:
	title = movie['title']
	year = movie['year']
	rating = movie['rating']
	results.append([title,year,rating])
	# print(f'{title} - {year} - {rating}')
for i in results:
	producer.send('imdb-replicated', json.dumps(i).encode('utf-8'))
	print(i)




