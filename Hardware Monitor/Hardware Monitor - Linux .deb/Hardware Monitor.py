import psutil
import pygame
from pygame.locals import (
    QUIT,
    MOUSEBUTTONDOWN
)

# Initialization
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 250
mode = "dark"

def toggle_mode():
    global mode
    mode = "dark" if mode == "light" else "light"

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            mouse_x, mouse_y = mouse_position
            button_x = SCREEN_WIDTH - 150
            button_y = 20
            button_width = 130
            button_height = 30
            if (
                button_x <= mouse_x <= button_x + button_width
                and button_y <= mouse_y <= button_y + button_height
            ):
                toggle_mode()

    screen.fill((0, 0, 0) if mode == "dark" else (255, 255, 255))

    button_text = "Toggle Mode"
    button = font.render(button_text, True, (0, 255, 0) if mode == "light" else (255, 255, 255))
    button_rect = button.get_rect()
    button_rect.topleft = (SCREEN_WIDTH - button_rect.width - 20, 20)
    screen.blit(button, button_rect)

    cpu_usage = psutil.cpu_percent()
    cpu_text = 'CPU Usage: ' + str(cpu_usage) + '%'
    cpu_text_render = font.render(cpu_text, True, (0, 255, 0) if mode == "light" else (255, 255, 255))
    screen.blit(cpu_text_render, (20, SCREEN_HEIGHT // 2 - 40))

    ram_usage = psutil.virtual_memory().percent
    ram_text = 'RAM Usage: ' + str(ram_usage) + '%'
    ram_text_render = font.render(ram_text, True, (0, 255, 0) if mode == "light" else (255, 255, 255))
    screen.blit(ram_text_render, (20, SCREEN_HEIGHT // 2))

    disk_usage = psutil.disk_usage('/').percent
    disk_text = 'Disk Usage: ' + str(disk_usage) + '%'
    disk_text_render = font.render(disk_text, True, (0, 255, 0) if mode == "light" else (255, 255, 255))
    screen.blit(disk_text_render, (20, SCREEN_HEIGHT // 2 + 40))

    battery_usage = psutil.sensors_battery().percent
    battery_text = 'Battery Usage/Percentage: ' + str(battery_usage) + '%'
    battery_text_render = font.render(battery_text, True, (0, 255, 0) if mode == "light" else (255, 255, 255))
    screen.blit(battery_text_render, (20, SCREEN_HEIGHT // 2 + 80))

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()  # Quit Pygame
