import tkinter as tk

class TrafficLightGUI:
    def __init__(self, master):
        self.master = master

        # Create a frame for the traffic light display
        self.traffic_light_frame = tk.Frame(self.master)

        # Create the red, yellow, and green light labels
        self.red_light_label = tk.Label(self.traffic_light_frame, text="Red", bg="red")
        self.yellow_light_label = tk.Label(self.traffic_light_frame, text="Yellow", bg="yellow")
        self.green_light_label = tk.Label(self.traffic_light_frame, text="Green", bg="green")

        # Place the light labels in the frame
        self.red_light_label.grid(row=0, column=0)
        self.yellow_light_label.grid(row=1, column=0)
        self.green_light_label.grid(row=2, column=0)

        # Pack the frame into the master window
        self.traffic_light_frame.pack()

    def update_traffic_light(self, color):
        # Turn on the specified light and turn off the other lights
        if color == "red":
            self.red_light_label.config(bg="red")
            self.yellow_light_label.config(bg="black")
            self.green_light_label.config(bg="black")
        elif color == "yellow":
            self.red_light_label.config(bg="black")
            self.yellow_light_label.config(bg="yellow")
            self.green_light_label.config(bg="black")
        elif color == "green":
            self.red_light_label.config(bg="black")
            self.yellow_light_label.config(bg="black")
            self.green_light_label.config(bg="green")
        else:
            raise ValueError("Invalid traffic light color")

# Create the main window
root = tk.Tk()

# Create a TrafficLightGUI object
traffic_light_gui = TrafficLightGUI(root)

# Update the GUI to display the red light
traffic_light_gui.update_traffic_light("yellow")

# Start the mainloop
root.mainloop()
