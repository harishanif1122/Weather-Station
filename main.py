import requests
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = '4ca064a834b614799052bdedbfb393cc'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return weather_data
    else:
        return None

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        weather_str = (f"Current weather in {city}:\n"
                       f"Temperature: {weather['temperature']}°C\n"
                       f"Humidity: {weather['humidity']}%\n"
                       f"Wind Speed: {weather['wind_speed']} m/s\n"
                       f"Description: {weather['description']}")
        messagebox.showinfo("Weather Update", weather_str)
    else:
        messagebox.showerror("Error", "Failed to fetch weather data. Please check the city name.")

def close_app():
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("Weather Update")
root.attributes('-topmost', True)  # Open the application as a whole, not minimized

# Label
city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

# Entry
city_entry = tk.Entry(root, width=30)  # Increase the width of the entry field
city_entry.pack()

# Button to get weather
get_weather_btn = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_btn.pack()

# Button to close application
close_btn = tk.Button(root, text="Close", command=close_app)
close_btn.pack()

root.mainloop()
