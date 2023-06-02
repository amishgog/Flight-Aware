import os
import time
import requests
from json.decoder import JSONDecodeError
import pandas as pd
import random
from pushbullet import Pushbullet



# Tracking area
lat_min, lat_max = 18.465208, 58.465208
long_min, long_max = 47.076825, 87.076825

home_lat = "******"
home_long = "******"

# Set to store tracked airplanes
tracked_airplanes = set()

# Function to fetch flight data
def fetch_flight_data():
    # API request URL
    url_data = 'https://opensky-network.org/api/states/all?' + 'lamin=' + str(lat_min) + '&lomin=' + str(
        long_min) + '&lamax=' + str(lat_max) + '&lomax=' + str(long_max)
    try:
        response = requests.get(url_data).json()

        col_name = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'long', 'lat',
                    'baro_altitude', 'on_ground', 'velocity']
        flight_df = pd.DataFrame(response['states'], columns=col_name)
        longitude = flight_df['long']
        latitude = flight_df['lat']
        call_sign = flight_df['callsign']
        altitude = flight_df['baro_altitude']
        origin = flight_df['origin_country']
        velocity = flight_df['velocity']
        for long, lat, sign, alt, orig, vel in zip(longitude, latitude, call_sign, altitude, origin, velocity):
            if pd.notna(alt) and pd.notna(long) and pd.notna(lat) and pd.notna(orig) and pd.notna(vel):
                if (
                    abs(lat - home_lat) <= 0.06
                    and abs(long - home_long) <= 0.06
                    and orig != "India"
                    and sign not in tracked_airplanes
                ):
                    send_notification(sign, alt, orig, vel)
                    tracked_airplanes.add(sign)
    except JSONDecodeError as e:
        print("Error decoding JSON:", e)


def send_notification(call_sign, altitude, origin, velocity):
    notification_title = "\bTHERE IS AN AIRCRAFT OVERHEAD!!"
    notification_text = f"-Flight : {call_sign} \n-Altitude : {altitude} m \n-Origin : {origin} \n-Velocity : {velocity} m/s"
    tracking_url = f"https://flightaware.com/live/flight/{call_sign}"
    sounds = ['Basso', 'Blow', 'Bottle', 'Frog', 'Funk', 'Glass', 'Hero', 'Morse', 'Ping', 'Pop', 'Purr', 'Sosumi', 'Submarine', 'Tink']
    notification_sound = random.choice(sounds)

    os.system(f"""
        osascript -e 'display notification "{notification_text}" sound name "{notification_sound}" with title "{notification_title}"'
        osascript -e 'open location "{tracking_url}"'
    """)

    time.sleep(10)

# Main program loop
while True:
    fetch_flight_data()
    time.sleep(60)  # Fetch flight data every minute
