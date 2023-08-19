import json
import time
from sense_hat import SenseHat

# Load configuration
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

sense = SenseHat()

def temperature_category(temp):
    if temp <= float(config["cold_temperature_upper_limit"]):
        return "cold", [128, 128, 128]  # Grey
    elif float(config["comfortable_temperature_range"].split('-')[0]) <= temp <= float(config["comfortable_temperature_range"].split('-')[1]):
        return "comfortable", [0, 255, 0]  # Green
    else:
        return "hot", [255, 0, 0]  # Red

def humidity_category(hum):
    if hum <= float(config["dry_humidity_upper_limit"]):
        return "dry", [128, 0, 128]  # Purple
    elif float(config["comfortable_humidity_range"].split('-')[0]) <= hum <= float(config["comfortable_humidity_range"].split('-')[1]):
        return "comfortable", [0, 255, 0]  # Green
    else:
        return "wet", [0, 0, 255]  # Blue

def log_data_to_sql_file(current_time, temperature, temp_category, humidity, hum_category):
    with open('data_log.sql', 'a') as file:
        file.write(f"INSERT INTO th_data (timestamp, temperature, temperature_category, humidity, humidity_category) VALUES ('{current_time}', {temperature}, '{temp_category}', {humidity}, '{hum_category}');\n")

def main():
    while True:
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()

        temp_category, temp_color = temperature_category(temperature)
        hum_category, hum_color = humidity_category(humidity)
        
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Log data to SQL file
        log_data_to_sql_file(current_time, temperature, temp_category, humidity, hum_category)
        
        # Display data on SenseHAT
        sense.show_message(f"T{int(temperature)}", text_colour=temp_color)
        time.sleep(5)
        sense.show_message(f"H{int(humidity)}", text_colour=hum_color)
        time.sleep(5)


if __name__ == "__main__":
    main()