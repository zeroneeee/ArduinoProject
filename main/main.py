import tkinter as tk

class TrafficLightGUI:
    
    def __init__(self, master):
        self.master = master

        # Create a frame for the traffic light display
        self.traffic_light_frame = tk.Frame(self.master)

        # Create the red, yellow, and green light labels
        self.red_light_label = tk.Label(self.traffic_light_frame, text="Red", bg="black")
        self.yellow_light_label = tk.Label(self.traffic_light_frame, text="Yellow", bg="black")
        self.green_light_label = tk.Label(self.traffic_light_frame, text="Green", bg="black")

        # Place the light labels in the frame
        self.red_light_label.grid(row=0, column=0)
        self.yellow_light_label.grid(row=1, column=0)
        self.green_light_label.grid(row=2, column=0)

        # Pack the frame into the master window
        self.traffic_light_frame.pack()
        
        # Initialize the current light index and light colors
        self.light_colors = ["red", "yellow", "green"]
        self.current_light_index = 0

        # Schedule the update_traffic_light method to run every 5 seconds
        self.master.after(5000, self.update_traffic_light)
        

    def turn_off_lights(self):
        # Turn off all lights
        self.red_light_label.config(bg="black")
        self.yellow_light_label.config(bg="black")
        self.green_light_label.config(bg="black")

    def update_traffic_light(self):
        # Turn off all lights
        self.turn_off_lights()

        # Set the color of the current light
        current_color = self.light_colors[self.current_light_index]
        if current_color == "red":
            self.red_light_label.config(bg="red")
            print("red")
        elif current_color == "yellow":
            self.yellow_light_label.config(bg="yellow")
            print("yellow")
        elif current_color == "green":
            self.green_light_label.config(bg="green")
            print("green")
        

        # Increment the current light index, cycling through the colors
        self.current_light_index = (self.current_light_index + 1) % len(self.light_colors)

        # Schedule the next update in 5 seconds
        self.master.after(5000, self.update_traffic_light)
    
# Create the main window
root = tk.Tk()

# Create a TrafficLightGUI object
traffic_light_gui = TrafficLightGUI(root)

# Start the mainloop
root.mainloop()
