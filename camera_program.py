import picamera
import pygame
import pygame.camera
from pygame.locals import *
from gpiozero import Button
from signal import pause

# Initialize Pygame
pygame.init()
pygame.camera.init()

# Set screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Set up camera
camera = picamera.PiCamera()
camera.resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Set up Pygame camera
cam = pygame.camera.Camera("/dev/video0", (SCREEN_WIDTH, SCREEN_HEIGHT))
cam.start()

# Set up Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 30)

# GPIO Buttons
capture_button = Button(17)
settings_button = Button(18)

# Camera settings
shutter_speeds = ['1/1000', '1/500', '1/250', '1/125', '1/60', '1/30', '1/15', '1/8', '1/4', '1/2', '1', '2', '4']
current_shutter_speed_index = 4
apertures = [1.8, 2.2, 2.5, 2.8, 3.2, 3.5, 4, 4.5, 5.0, 5.6, 6.3, 7.1, 8, 9, 10, 11]
current_aperture_index = 3
iso_values = [100, 200, 400, 800, 1600]
current_iso_index = 0
exposure_compensation = 0
image_resolutions = [(640, 480), (1024, 768), (1280, 720), (1920, 1080)]
current_resolution_index = 2
image_effects = ['none', 'negative', 'solarize', 'sketch', 'denoise', 'emboss', 'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation', 'colorswap', 'washedout', 'posterise', 'colorpoint', 'colorbalance', 'cartoon']
current_effect_index = 0

def update_overlay():
    overlay = camera.add_overlay(pygame.camera.list_cameras()[0], size=(SCREEN_WIDTH, SCREEN_HEIGHT), layer=3)
    overlay.alpha = 128
    overlay.fullscreen = True

def capture_image():
    camera.capture('image.jpg')

def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_settings_menu():
    screen.fill(BLACK)
    draw_text("Settings Menu", 20, 20)
    pygame.display.update()

def main():
    running = True
    settings_open = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif capture_button.is_pressed:
                capture_image()
            elif settings_button.is_pressed:
                settings_open = not settings_open
                if settings_open:
                    display_settings_menu()
                else:
                    update_overlay()

        if settings_open:
            # Handle settings menu interactions
            pass
        else:
            # Display camera preview with overlay
            image = cam.get_image()
            screen.blit(image, (0, 0))

            # Display camera settings overlay
            draw_text(f"Shutter Speed: {shutter_speeds[current_shutter_speed_index]}", 10, SCREEN_HEIGHT - 90)
            draw_text(f"Aperture: {apertures[current_aperture_index]}", 10, SCREEN_HEIGHT - 60)
            draw_text(f"ISO: {iso_values[current_iso_index]}", 10, SCREEN_HEIGHT - 30)

            pygame.display.update()

    pygame.quit()
    cam.stop()
    camera.close()

if __name__ == "__main__":
    update_overlay()
    main()
    pause()
