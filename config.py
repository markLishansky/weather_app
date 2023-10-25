USE_ROUNDED_COORDS = True
OPENWEATHER_API = "7d97302422b2c1b2a0bb6cb8327a064d"
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)