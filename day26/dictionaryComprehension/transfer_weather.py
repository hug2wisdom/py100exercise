c_weather = {
    "london": 22,
    "america": 33,
    "china": 44,
}

f_weather = {country: degree + 22.0 for (country, degree) in c_weather.items()}
print(f_weather)
