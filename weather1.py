from flask import Flask, render_template, request
import json
import urllib.request
import urllib.parse
from datetime import datetime
import os
from dotenv import load_dotenv

app = Flask(__name__)

api_key = os.getenv('API_KEY')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
    else:
        city = 'nagpur'
        
    
    
    city_encoded = urllib.parse.quote(city)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric'
    
    with urllib.request.urlopen(url) as response:
        source = response.read()
    
    list_of_data = json.loads(source)
    
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']), 
        "temp": list_of_data['main']['temp'], 
        "pressure": list_of_data['main']['pressure'], 
        "humidity": list_of_data['main']['humidity'], 
        "description": list_of_data['weather'][0]['description'].capitalize(),
        "icon": list_of_data['weather'][0]['icon'],
        "wind_speed": list_of_data['wind']['speed'],
        "datetime": datetime.now().strftime('%B %d, %Y, %I:%M:%S %p')
    }
    
    return render_template('weather.html', data=data, city=city)

if __name__ == '__main__':
    app.run(debug=True)
