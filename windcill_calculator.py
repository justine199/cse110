# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to calculate wind chill
def calculate_wind_chill(temperature_f, wind_speed_mph):
    return 35.74 + (0.6215 * temperature_f) - 35.75 * (wind_speed_mph ** 0.16) + 0.4275 * temperature_f * (wind_speed_mph ** 0.16)

# Main program
# Get the temperature from the user
temperature_input = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# Convert to Fahrenheit if necessary
if unit == "C":
    temperature_f = celsius_to_fahrenheit(temperature_input)
else:
    temperature_f = temperature_input

# Display wind chill for wind speeds from 5 to 60 mph
for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temperature_f, wind_speed)
    print(f"At temperature {temperature_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
