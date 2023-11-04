import time

from main.main import TrafficLightGUI
# Create a TrafficLightGUI object
traffic_light_gui = TrafficLightGUI()

traffic_light_gui.update_traffic_light("red")
time.sleep(5)
traffic_light_gui.update_traffic_light("yellow")
time.sleep(5)
traffic_light_gui.update_traffic_light("green")
time.sleep(5)