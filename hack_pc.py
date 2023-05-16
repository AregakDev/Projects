# WARNING!!!!
# By executing this code, I cannot assume responsibility, and you proceed at your own risk.
# This code is going to shut down your PC!!!


import colorama
import random
import tkinter as tk
import os
from time import sleep

# Define the message and title
message = "Your PC has been hacked!"
title = "Hacked!"

colorama.init()

# Define the colors
green = colorama.Fore.GREEN
print("Hacking PC...")
sleep(1)
# Print the matrix in an infinite loop
for i in range(1000):
    matrix = [[random.choice(['0', '1']) for _ in range(100)] for _ in range(10)]

    for row in matrix:
        print(' '.join([green + str(cell) for cell in row]))

# Define a list of possible warning messages
messages = [
    "WARNING: Your PC is HACKED!",
    "WARNING: Unauthorized access detected!",
    "WARNING: Security breach detected!",
    "WARNING: System compromised!",
    "WARNING: Intruder alert!"
]

# Define the dimensions of the screen
screen_width = 800
screen_height = 600

# Define the dimensions of the message box
message_width = 400
message_height = 200

# Define the countdown time (in seconds)
countdown_time = 10

# Define the function to update the countdown label
def update_countdown_label():
    global countdown_time
    if countdown_time > 0:
        countdown_time -= 1
        countdown_label.config(text=f"Shutting down PC in : {countdown_time} seconds")
        countdown_label.after(1000, update_countdown_label)
    else:
        root.destroy()

# Define the function to show the message box
def show_message_box():
    # Choose a random message
    message = messages[0]

    # Choose a random position for the message box
    x = random.randint(0, screen_width - message_width)
    y = random.randint(0, screen_height - message_height)

    # Create the message box
    message_box = tk.Toplevel()
    message_box.geometry(f"{message_width}x{message_height}+{x}+{y}")
    message_box.title("WARNING!")
    message_box.configure(bg="#000000")

    # Add the message label
    message_label = tk.Label(message_box, text=message, fg="#00FF00", bg="#000000", font=("Courier", 18))
    message_label.pack(pady=20)

    # Add the countdown label
    global countdown_label
    countdown_label = tk.Label(message_box, text=f"Time remaining: {countdown_time} seconds", fg="#00FF00", bg="#000000", font=("Courier", 12))
    countdown_label.pack(pady=10)

    # Start the countdown
    update_countdown_label()

    # Show the message box
    message_box.attributes("-topmost", True)
    message_box.mainloop()

# Create the main window
root = tk.Tk()
root.title("HACKED!")
root.configure(bg="#000000")
root.attributes("-fullscreen", True)

# Add a label to give the impression of a "hacking" console
console_label = tk.Label(root, text="HACKING INTO SYSTEM...", fg="#00FF00", bg="#000000", font=("Courier", 24))
console_label.pack(pady=50)

# Start showing the message boxes
show_message_box()
root.update()
os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
