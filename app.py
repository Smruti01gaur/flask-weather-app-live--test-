from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "93262a118a118bdede939f539a96e08d"  # Replace with your actual OpenWeatherMap API key


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                }
            else:
                error_message = "City not found!"
        else:
            error_message = "Please enter a city name."
    return render_template("index.html", weather=weather_data, error=error_message)


if __name__ == "__main__":
    app.run(debug=True)
