import psutil
import pygetwindow as gw
import time
import pyray
from raylib.colors import (
    BLACK,
    GREEN,
    WHITE
)

# Initialization
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 250

# Set the variable mode to light or dark
mode = "dark"
window_fixed = False

def toggle_mode():
    global mode
    mode = "dark" if mode == "light" else "light"

# Set the button dimensions
button_x = 20
button_y = SCREEN_HEIGHT // 2 - 80
button_width = 200
button_height = 40

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'Hardware Monitor')
pyray.set_target_fps(120)  # Set our game to run at 120 frames-per-second

# Check for mouse click on the button
if pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
    mouse_position = pyray.get_mouse_position()
    mouse_x = mouse_position.x
    mouse_y = mouse_position.y
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        toggle_mode()
            
# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    
    # Draw the mode toggle button
    button_text = "Toggle Mode"
    button_text_width = pyray.measure_text(button_text, 20)
    button_x = SCREEN_WIDTH - button_text_width - 20
    button_y = 20
    button_width = button_text_width + 10
    button_height = 30
    pyray.draw_rectangle(button_x, button_y, button_width, button_height, GREEN if mode == "light" else WHITE)
    pyray.draw_text(button_text, button_x + 5, button_y + 5, 20, BLACK if mode == "light" else GREEN)

    # Check if the button is clicked
    if pyray.check_collision_point_rec(pyray.get_mouse_position(), pyray.Rectangle(button_x, button_y, button_width, button_height)) and pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
        toggle_mode()
    time.sleep(0.3)

    # Draw
    pyray.begin_drawing()
    if mode == "light":
        pyray.clear_background(WHITE)
    else:
        pyray.clear_background(BLACK)
    
    # Draw button
    button_text = "Switch Mode"
    pyray.draw_rectangle(button_x, button_y, button_width, button_height, GREEN if mode == "light" else WHITE)
    pyray.draw_text(button_text, button_x + 5, button_y + 5, 20, BLACK if mode == "light" else GREEN)

    # Get and display CPU usage
    cpu_usage = psutil.cpu_percent()
    cpu_text = 'CPU Usage: ' + str(cpu_usage) + '%'
    cpu_text_width = pyray.measure_text(cpu_text, 20)
    cpu_text_x = 120
    cpu_text_y = SCREEN_HEIGHT // 2 - 40
    pyray.draw_text(cpu_text, cpu_text_x, cpu_text_y, 20, GREEN if mode == "light" else WHITE)
    
    # Get and display CPU clock speed (GHz)
    cpu_clock_speed = psutil.cpu_freq().current / 1000
    cpu_clock_speed = round(cpu_clock_speed, 2)
    cpu_clock_text = 'CPU Clock Speed: ' + str(cpu_clock_speed) + ' GHz'
    cpu_clock_text_width = pyray.measure_text(cpu_clock_text, 20)
    cpu_clock_text_x = 120
    cpu_clock_text_y = SCREEN_HEIGHT // 2 - 60
    pyray.draw_text(cpu_clock_text, cpu_clock_text_x, cpu_clock_text_y, 20, GREEN if mode == "light" else WHITE)

    # Get and display RAM usage
    ram_usage = psutil.virtual_memory().percent
    ram_text = 'RAM Usage: ' + str(ram_usage) + '%'
    ram_text_width = pyray.measure_text(ram_text, 20)
    ram_text_x = 120
    ram_text_y = SCREEN_HEIGHT // 2 - 20
    pyray.draw_text(ram_text, ram_text_x, ram_text_y, 20, GREEN if mode == "light" else WHITE)

    # Get and show disk current speed in MB/s
    disk_usage = psutil.disk_usage('/').percent
    disk_text = 'Disk Usage: ' + str(disk_usage) + '%'
    disk_text_width = pyray.measure_text(disk_text, 20)
    disk_text_x = 120
    disk_text_y = SCREEN_HEIGHT // 2
    pyray.draw_text(disk_text, disk_text_x, disk_text_y, 20, GREEN if mode == "light" else WHITE)
    
    # Get and display Battery usage
    battery_usage = psutil.sensors_battery().percent
    battery_text = 'Battery Usage/Percentage: ' + str(battery_usage) + '%'
    battery_text_width = pyray.measure_text(battery_text, 20)
    battery_text_x = 120
    battery_text_y = SCREEN_HEIGHT // 2 + 20
    pyray.draw_text(battery_text, battery_text_x, battery_text_y, 20, GREEN if mode == "light" else WHITE)
    
    # Get and display Network usage (Download/Upload in MB/s)
    network_usage = psutil.net_io_counters()
    download_speed = network_usage.bytes_recv / (1024 * 1024)
    upload_speed = network_usage.bytes_sent / (1024 * 1024)
    download_speed = round(download_speed, 2)
    upload_speed = round(upload_speed, 2)
    download_text = 'Network Usage (Download): ' + str(download_speed) + ' MB/s'
    upload_text = 'Network Usage (Upload): ' + str(upload_speed) + ' MB/s'
    download_text_width = pyray.measure_text(download_text, 20)
    upload_text_width = pyray.measure_text(upload_text, 20)
    download_text_x = 120
    download_text_y = SCREEN_HEIGHT // 2 + 40
    upload_text_x = 120
    upload_text_y = SCREEN_HEIGHT // 2 + 60
    pyray.draw_text(download_text, download_text_x, download_text_y, 20, GREEN if mode == "light" else WHITE)
    pyray.draw_text(upload_text, upload_text_x, upload_text_y, 20, GREEN if mode == "light" else WHITE)

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context