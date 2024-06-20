Weather App by ZK_CREATIONS


Overview
This repository contains the code for a simple weather application built using Flask. The app allows users to get the current weather information for a specified city by entering the city name in a form. It fetches data from the OpenWeatherMap API and displays it on the webpage.

Features
User-friendly interface to get weather information by entering a city name.
Displays temperature, weather description, wind speed, and date/time of the request.
Utilizes the OpenWeatherMap API to fetch real-time weather data.
Technologies Used
Python
Flask
HTML/CSS
OpenWeatherMap API![Screenshot 2024-06-20 181903](https://github.com/zuberkhan01st/Weather-App-Flask-/assets/132389756/ba73e0bb-7f61-4962-9528-7c874b48c75d)

Prerequisites
Python 3.x
Flask
An OpenWeatherMap API key
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/zuberkhan01st/WeatherApp-Flask-/
cd weather-app
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Setup Environment Variables

Create a .env file in the root directory of the project.
Add your OpenWeatherMap API key to the .env file:
makefile
Copy code
API_KEY=your_openweathermap_api_key
Run the Application

bash
Copy code
python weather1.py
The app will be running on http://127.0.0.1:5000/.
Project Structure
arduino
Copy code
weather-app/
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── weather.html
├── .env
├── requirements.txt
├── weather1.py
└── README.md
Usage
Open your web browser and go to http://127.0.0.1:5000/.
Enter the name of a city in the input field.
Click the "Get Weather" button.
The weather information for the specified city will be displayed on the page.
Example
When you enter "London" and submit, the app will display:

Current temperature in Celsius.
Weather description (e.g., Clear sky).
Wind speed.
Current date and time of the request.
Weather icon representing the current weather condition.
Screenshots
Home Page

Weather Result

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or feedback, please reach out to me at [zuberkhan01st@gmail.com].

Thank you for using the Weather App by ZK_CREATIONS!

