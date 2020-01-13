import tkinter as tk
import requests
from tkinter import font

# CANVAS VALUES
HEIGHT = 500
WIDTH = 600

# WEATHER API KEY
# 3768a06152a1f8bb833a5024516defb8

# API CALL: (ITS JSON)
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test_function():
    print("Button clicked")

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        final_str = "City: %s \nConditions: %s \nTemperature: (°F): %s" % (name, desc, temp)
    except:
        final_str = "We're sorry, we couldn't find that location. Please try again."
    return final_str

def get_weather(city):
    weather_key = "3768a06152a1f8bb833a5024516defb8"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    label["text"] = format_response(weather)

# THE MAIN ROOT
root = tk.Tk()

# CANVAS
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
# TOP FRAME
frame = tk.Frame(root, bg="#B9EA2E", bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

# ENTRY. LIKE INPUT.
entry = tk.Entry(frame, font="Futura")
entry.place(relwidth=0.65, relheight=1)

# BUTTON
button = tk.Button(frame, text="Get Weather", font="Futura", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# LOWER FRAME
lower_frame = tk.Frame(root, bg="#B9EA2E", bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.3, anchor="n")

# # LABEL
label = tk.Label(lower_frame, font=("Futura"), anchor="nw", justify="left",bd=3)
label.place(relwidth=1, relheight=1)

# LIST OF FONTS AVAILABLE
# print(tk.font.families())
root.mainloop()
