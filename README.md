# Flight Aware

## Description

Flight Aware is a script written in Python that utilizes the OpenSky Network API to fetch live flight data. It defines a tracking area using latitude and longitude boundaries, and retrieves aircraft information within that area. The script filters the data, checks if the aircraft is within a certain proximity to a home location, and sends a notification using AppleScript(osascript) with flight details if the conditions are met. The notification includes the flight callsign, altitude, origin, and velocity. It opens a web browser with a link to track the flight on FlightAware for more information.

## Dependencies

- Python 3.x
- Requests library: `pip install requests`
- pandas library: `pip install pandas`

## Usage

1. Clone the repository or download the source code.
2. Install the required dependencies using pip.
3. Update the tracking area coordinates and home location coordinates in the code if desired.
4. Run the `flight_tracker.py` script using Python.
5. The script will fetch flight data every minute and send notifications for aircraft detected overhead.
6. Notifications will include flight details such as callsign, altitude, origin, and velocity.
7. The notification will automatically open the FlightAware website to track the flight.

## Configuration

- Modify the `lat_min`, `lat_max`, `long_min`, and `long_max` variables to define the tracking area's latitude and longitude boundaries.
- Adjust the `home_lat` and `home_long` variables to set the home location coordinates.
- Customize the notification title and text in the `send_notification` function if desired.
- Modify the sleep duration in the main program loop (`time.sleep()`) to change the frequency of fetching flight data.

## Acknowledgments

This project utilizes the OpenSky Network API for fetching flight data. For more information about the API and its terms of use, please visit the [OpenSky Network](https://opensky-network.org/) website.

