import time
import random
import matplotlib.pyplot as plt
from datetime import datetime

# import RPi.GPIO as GPIO
# import Adafruit_DHT

# GPIO.setmode(GPIO.BCM)
# TRIG = 23
# ECHO = 24
# DHT_SENSOR = Adafruit_DHT.DHT11
# DHT_PIN = 4

# GPIO.setup(TRIG, GPIO.OUT)
# GPIO.setup(ECHO, GPIO.IN)

# random numbers generation
def get_simulated_distance():
    return round(random.uniform(10, 100), 2) # random from 10 to 100cm

def get_simulated_temperature():
    return round(random.uniform(20, 30), 2) # random from 20 to 30°C

def log_file_data(distance, temperature): # log data to a file
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("sensor_data_log.txt", "a") as file:
        file.write(f"{timestamp}, {distance}, {temperature}\n")

def plot_the_data(): # appends data from the file to lists and plots the data
    timestamps, distances, temperatures = [], [], []
    with open("sensor_data_log.txt", "r") as file:
        for line in file:
            timestamp, distance, temperature = line.strip().split(", ")
            timestamps.append(timestamp)
            distances.append(float(distance))
            temperatures.append(float(temperature))
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, distances, label="Distance (cm)", color="blue")
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    plt.xlabel("Time")
    plt.xticks(rotation=45)
    plt.ylabel("Sensor Readings")
    plt.title("Sensor Readings Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig("sensor_data_plot.png")
    plt.show() 
    
try:
    while True:
        # Random Data
        distance = get_simulated_distance()
        temperature = get_simulated_temperature()
        
        # Real Data
        # distance = get_distance()
        # temperature = get_temperature()
        
        if temperature is not None:
            log_file_data(distance, temperature)
            print(f"Distance: {distance} cm, Temperature: {temperature}°C")
        else:
            print("Failed to retrieve data from temperature sensor.")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Terminated by user")

finally:
    # GPIO.cleanup()
    plot_the_data()


