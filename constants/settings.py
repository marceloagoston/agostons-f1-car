import pygame

# Dimensiones de la pantalla
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800

# Seteamos reloj y FPS
FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 1
PLAYER_VELOCITY = 5

RIVAL_STARTING_VELOCITY = 5
BUFFER_DISTANCE = 100
MAX_KERS = 100