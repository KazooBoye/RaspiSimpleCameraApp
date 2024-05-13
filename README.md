# RaspiSimpleCameraApp
An intuitive, simple camera app for raspberry pi optimized for touch screens.

This Python program allows you to use a Raspberry Pi with a 3.5 inch 480x320 resolution display and the default Pi camera to capture images. It features a fullscreen camera preview with a software light meter and overlays current shutter speed, aperture, and ISO settings. Additionally, it includes a settings menu accessible via GPIO buttons for adjusting camera settings such as shutter speed, aperture, ISO, exposure compensation, image resolution, and image effects.

## Requirements
- Raspberry Pi with a 3.5 inch 480x320 resolution display
- Raspberry Pi Camera Module
- Python 3.x
- `picamera` library
- `pygame` library
- `gpiozero` library

## Installation

1. Connect the Raspberry Pi camera module to your Raspberry Pi.
2. Install the required libraries using pip:

    ```
    pip install picamera pygame gpiozero
    ```

## Usage

1. Run the Python script `camera_program.py` on your Raspberry Pi.
2. The camera preview will start displaying on fullscreen with overlays for camera settings.
3. Use the GPIO buttons connected to the Raspberry Pi to interact with the program:
   - One button for capturing images.
   - One button for opening the settings menu.
4. In the settings menu, you can adjust various camera settings:
   - Shutter speed: Select from a range of shutter speeds.
   - Aperture: Adjust the aperture value.
   - ISO: Change the ISO setting.
   - Exposure compensation: Set exposure compensation.
   - Image resolution: Choose from available image resolutions.
   - Image effects: Apply different effects to captured images.
