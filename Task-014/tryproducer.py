from kafka import KafkaProducer
import requests
import json
import time
producer = KafkaProducer(bootstrap_servers = 'localhost:9099')
cities=['London', 'Paris', 'Bern', 'Stockholm', 'Madrid', 'Vienna']
while True:
    for i in range(len(cities)):

        api_address = 'http://api.openweathermap.org/data/2.5/weather?q='
        city = cities[i]
        appid= '&appid='
        api_key = '7aea328252d1145f04f11f48470d20d4'
        
        url = api_address + city+ appid + api_key
        response = requests.get(url).json()
        msg = response
        print(type(response))


        producer.send('api', json.dumps(msg).encode('utf-8'))
        time.sleep(2)
        print("Sending msg \"{}\"".format(msg))
        print("Message sent!")

