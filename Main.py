import tkinter as tk
from tkinter import ttk
import picamera
import RPi.GPIO as GPIO
from PIL import Image, ImageTk

# GPIO button pins
PHOTO_BUTTON_PIN = 6
RECORD_BUTTON_PIN = 5

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PHOTO_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RECORD_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create a function to take a photo
def take_photo():
    with picamera.PiCamera() as camera:
        camera.capture("photo.jpg")

# Create a function to start/stop video recording
def toggle_recording():
    global recording
    if not recording:
        camera.start_recording("video.h264")
        recording_button.config(text="Stop Recording", command=stop_recording)
        recording = True
    else:
        camera.stop_recording()
        recording_button.config(text="Start Recording", command=start_recording)
        recording = False

# Create a function to start video recording
def start_recording():
    with picamera.PiCamera() as camera:
        camera.start_recording("video.h264")

# Create a function to stop video recording
def stop_recording():
    camera.stop_recording()

# Create a function to show the settings menu
def show_settings_menu():
    stop_preview()
    clear_window()

    # Create and set default values for settings variables
    shutter_speed_var = tk.IntVar()
    shutter_speed_var.set(camera.shutter_speed)

    iso_var = tk.IntVar()
    iso_var.set(camera.iso)

    white_balance_var = tk.StringVar()
    white_balance_var.set(camera.awb_mode)

    filter_var = tk.StringVar()
    filter_var.set("None")

    # Function to update the settings
    def update_settings():
        camera.shutter_speed = shutter_speed_var.get()
        camera.iso = iso_var.get()
        camera.awb_mode = white_balance_var.get()
        # Apply image filter (add your filter logic here if needed)

    # Function to go back to the main window
    def back_to_main_window():
        clear_window()
        start_preview()
        show_main_window()

    # Function to increase shutter speed
    def increase_shutter_speed():
        current_speed = shutter_speed_var.get()
        new_speed = current_speed + 10
        shutter_speed_var.set(new_speed)

    # Function to decrease shutter speed
    def decrease_shutter_speed():
        current_speed = shutter_speed_var.get()
        new_speed = current_speed - 10
        shutter_speed_var.set(new_speed)

    # Function to increase ISO
    def increase_iso():
        current_iso = iso_var.get()
        new_iso = current_iso + 10
        iso_var.set(new_iso)

    # Function to decrease ISO
    def decrease_iso():
        current_iso = iso_var.get()
        new_iso = current_iso - 10
        iso_var.set(new_iso)

    # Create labels and entry fields for settings
    shutter_speed_label = ttk.Label(root, text="Shutter Speed:")
    shutter_speed_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    shutter_speed_entry = ttk.Entry(root, textvariable=shutter_speed_var)
    shutter_speed_entry.grid(row=0, column=2, padx=5, pady=5)

    iso_label = ttk.Label(root, text="ISO:")
    iso_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    iso_entry = ttk.Entry(root, textvariable=iso_var)
    iso_entry.grid(row=1, column=2, padx=5, pady=5)

    white_balance_label = ttk.Label(root, text="White Balance:")
    white_balance_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    white_balance_combobox = ttk.Combobox(
        root,
        textvariable=white_balance_var,
        values=["auto", "sunlight", "cloudy", "shade", "tungsten", "fluorescent", "incandescent", "flash", "horizon"],
    )
    white_balance_combobox.grid(row=2, column=2, padx=5, pady=5)

    filter_label = ttk.Label(root, text="Image Filter:")
    filter_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    filter_combobox = ttk.Combobox(
        root,
        textvariable=filter_var,
        values=["None", "Emboss", "Sketch", "OilPaint"],
    )
    filter_combobox.grid(row=3, column=2, padx=5, pady=5)

    # Create buttons to update settings, go back, and adjust shutter speed/ISO
    update_button = ttk.Button(root, text="Update Settings", command=update_settings)
    update_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

    back_button = ttk.Button(root, text="Back", command=back_to_main_window)
    back_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    plus_shutter_button = ttk.Button(root, text="+", command=increase_shutter_speed)
    plus_shutter_button.grid(row=0, column=3, padx=5, pady=5)

    minus_shutter_button = ttk.Button(root, text="-", command=decrease_shutter_speed)
    minus_shutter_button.grid(row=0, column=4, padx=5, pady=5)

    plus_iso_button = ttk.Button(root, text="+", command=increase_iso)
    plus_iso_button.grid(row=1, column=3, padx=5, pady=5)

    minus_iso_button = ttk.Button(root, text="-", command=decrease_iso)
    minus_iso_button.grid(row=1, column=4, padx=5, pady=5)

# Create a function to stop the camera preview
def stop_preview():
    camera.stop_preview()

# Create a function to start the camera preview
def start_preview():
    camera.start_preview(fullscreen=False, window=(0,100,1024,576))

# Create a function to clear the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Create a function to show the main window
def show_main_window():
    # Create a label to display the camera preview
    preview_label = ttk.Label(root)
    preview_label.grid(row=0, column=0, padx=10, pady=10, rowspan=5, columnspan=4)

    # Create a label to display current shutter speed
    shutter_speed_label = ttk.Label(root, text="Shutter Speed:")
    shutter_speed_label.grid(row=0, column=5, padx=5, pady=5, sticky="w")

    shutter_speed_value = ttk.Label(root, text=str(camera.shutter_speed))
    shutter_speed_value.grid(row=0, column=6, padx=5, pady=5)

    # Create a label to display current ISO value
    iso_label = ttk.Label(root, text="ISO:")
    iso_label.grid(row=1, column=5, padx=5, pady=5, sticky="w")

    iso_value = ttk.Label(root, text=str(camera.iso))
    iso_value.grid(row=1, column=6, padx=5, pady=5)

    # Create a button to show the settings menu
    menu_button = ttk.Button(root, text="Menu", command=show_settings_menu)
    menu_button.grid(row=0, column=7, padx=10, pady=10, rowspan=2)

# Create the main window
root = tk.Tk()
root.title("Raspberry Pi Camera")
root.attributes("-fullscreen", True)

# Initialize the Pi Camera
camera = picamera.PiCamera()
camera.resolution = (480, 320)  # Adjust resolution as needed

# Show the main window initially
show_main_window()

# Initialize recording status
recording = False

# Start the camera preview
start_preview()

# Start the Tkinter main loop
root.mainloop()

# Clean up and close the camera
camera.close()
GPIO.cleanup()
