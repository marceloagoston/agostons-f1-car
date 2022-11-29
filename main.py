import pygame
import random
import time as t

from constants.colors import *

pygame.init()

from constants.fuentes import *
from constants.settings import *

# Dibujamos la pantalla
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Ponemos icono a la ventana
pygame.display.set_icon(pygame.image.load("./assets/img/f1_hero_pixel.png"))

# Ponemos nombre a la pestaña
pygame.display.set_caption("Agoston's F1 Car 0.1")

# Configuración Inicial Juego
puntos = 0
kers_actual = MAX_KERS
velocidad_actual = PLAYER_VELOCITY
vidas = PLAYER_STARTING_LIVES

####################################################################
######################  INICIO SETEAR TEXTOS  ######################
####################################################################
# Titulo del juego
title_text = fuente_pixel.render("Agoston's F1 Car", True, VIOLETA)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

# Texto Puntos
puntos_text = fuente_pixel.render(f'Puntos: {puntos}', True, AMARILLO)
puntos_rect = puntos_text.get_rect()
puntos_rect.topright = (WINDOW_WIDTH - 50, 10)

# Texto Vidas
velocidad_text = fuente_pixel.render(f'Velocidad: 0', True, AMARILLO)
velocidad_rect = velocidad_text.get_rect()
velocidad_rect.topright = (WINDOW_WIDTH - 50, 50)

# Texto KERS
kers_text = fuente_pixel_chica.render(f'Kers: 100', True, AMARILLO)
kers_rect = kers_text.get_rect()
kers_rect.topright = (WINDOW_WIDTH - 50, 55)

# Texto Vidas
vidas_text = fuente_pixel_chica.render(f'Vidas: {vidas}', True, AMARILLO)
vidas_rect = vidas_text.get_rect()
vidas_rect.topright = (150, 55)

# Texto Tiempo
tiempo_text = fuente_pixel_chica.render(f'Tiempo: 00:00', True, AMARILLO)
tiempo_rect = tiempo_text.get_rect()
tiempo_rect.center = (WINDOW_WIDTH // 2, 65)

### Gameover
gameover_text = fuente_pixel_grande.render(' Juego Terminado ', True, GREEN, DARKGREEN)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 100)

### Gameover - presiona una tecla para jugar otra vez
presskey_text = fuente_pixel.render(' Presione la tecla "C" para jugar otra vez ', True, GREEN, DARKGREEN)
presskey_rect = presskey_text.get_rect()
presskey_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +32)

### Gameover - presiona Q para salir
quit_text = fuente_pixel.render(' O Presione "Q" para salir del juego ', True, WHITE, DARKRED)
quit_rect = quit_text.get_rect()
quit_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 +64)

### Texto instrucciones
instrucciones_text = fuente_pixel_muy_chica.render(' Shift: Kers (Boost)', True, AMARILLO)
instrucciones_rect = instrucciones_text.get_rect()
instrucciones_rect.topright = (WINDOW_WIDTH -20 , 90)

### Texto instrucciones
instrucciones_salir_text = fuente_pixel_muy_chica.render(' s: Salir', True, AMARILLO)
instrucciones_salir_rect = instrucciones_salir_text.get_rect()
instrucciones_salir_rect.topright = (WINDOW_WIDTH -20 , 130)

### Texto Pausa 
pausa_text = fuente_pixel_muy_chica.render(' p: Pausar', True, AMARILLO)
pausa_rect = pausa_text.get_rect()
pausa_rect.topright = (WINDOW_WIDTH -20 , 110)

### Cartel Grande Juego Pausado
pausa_cartel_text = fuente_pixel.render(' Juego Pausado ', True, AMARILLO, DARKGREEN)
pausa_cartel_rect = pausa_cartel_text.get_rect()
pausa_cartel_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 50)

# Cartel juego pausado - presione P para volver a jugar
presskey_pausa_text = fuente_pixel_chica.render(' Presione "P" nuevamente para seguir jugando ', True, GREEN, DARKGREEN)
presskey_pausa_rect = presskey_pausa_text.get_rect()
presskey_pausa_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

####################################################################
######################   FIN SETEAR TEXTOS    ######################
####################################################################


hero_img = pygame.image.load("./assets/img/f1_hero_pixel.png")
hero_img = pygame.transform.scale(hero_img, (35, 35))

hero_img_arr = pygame.transform.rotate(hero_img, 0)
hero_img_der = pygame.transform.rotate(hero_img, 270)
hero_img_ab = pygame.transform.rotate(hero_img, 180)
hero_img_izq = pygame.transform.rotate(hero_img, 90)

hero_rect = hero_img.get_rect()
hero_rect.centery = WINDOW_HEIGHT - 100
hero_rect.centerx = WINDOW_WIDTH // 2

# Objetos
planta_img = pygame.image.load("./assets/img/planta_pixel.png")
planta_img = pygame.transform.scale(planta_img, (35, 35))
planta_rect = planta_img.get_rect()
planta_rect.x = random.randint(32, WINDOW_WIDTH -32)
#primer parametro no tengo idea, el otro es la altura de la pantalla menos el lo grande que es la planta
planta_rect.y = random.randint(112, WINDOW_HEIGHT - 32)

# Botella rota
# bot_img = pygame.image.load("./assets/img/brbot.png")
bot_img = pygame.image.load("./assets/img/bot_rota_pixel.png")
bot_img = pygame.transform.scale(bot_img, (35, 35))
bot_rect = bot_img.get_rect()
bot_rect.x = random.randint(32, WINDOW_WIDTH - 32)
#primer parametro no tengo idea, el otro es la altura de la pantalla menos el lo grande que es la planta
bot_rect.y = random.randint(112, WINDOW_HEIGHT - 32)

# Imagen Background
bg = pygame.image.load("./assets/img/bg.jpg")

# Música
pygame.mixer.music.load("./assets/sounds/Le Grand Chase.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.2)

# Seteamos sonidos
exito_sound = pygame.mixer.Sound("./assets/sounds/sonido_bien.wav")
exito_sound.set_volume(.2)
golpe_sound = pygame.mixer.Sound("./assets/sounds/sonido_golpe.wav")
golpe_sound.set_volume(.2)

# Controles
silence = False
running = True
pausado = False
aux = 1
aux2 = 0
minutos = 0

text_minutos = '00'
text_segundos = '00'

while running:

	# Comprobar si se presiono el boton de salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:

		    # El jugador presiona la tecla de salir (q)
            if event.key == pygame.K_q:
                pausado = False
                running = False

            # El jugador presiona la tecla de pausar### (p)
            elif event.key == pygame.K_p:
                pausado = True
                pygame.mixer.music.set_volume(0.05)

                display_surface.blit(pausa_cartel_text, pausa_cartel_rect)
                display_surface.blit(presskey_pausa_text, presskey_pausa_rect)
                pygame.display.update()
                
                while pausado:
                    
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                pausado = False
                                pygame.mixer.music.set_volume(.2)
                    
            elif event.key == pygame.K_m:
                silence = not silence
                if silence:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(.2)


	# Get movimientos continuos
    keys = pygame.key.get_pressed()

	# Movimientos Continuos sin pasar el borde de la pantalla y sin llegar al HUD
    if keys[pygame.K_LEFT] and hero_rect.left > 0:
        hero_rect.x -= velocidad_actual
        hero_img = hero_img_izq
    if keys[pygame.K_RIGHT] and hero_rect.right < WINDOW_WIDTH:
        hero_rect.x += velocidad_actual
        hero_img = hero_img_der

    if keys[pygame.K_UP] and hero_rect.top > 80:
        hero_rect.y -= velocidad_actual
        hero_img = hero_img_arr

    if keys[pygame.K_DOWN] and hero_rect.bottom < WINDOW_HEIGHT:
        hero_rect.y += velocidad_actual
        hero_img = hero_img_ab

    if keys[pygame.K_RSHIFT] and hero_rect.bottom < WINDOW_HEIGHT:
        hero_rect.y += velocidad_actual
        hero_img = hero_img_ab

    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and kers_actual > 0:
        velocidad_actual = PLAYER_VELOCITY + 10
        kers_actual -= 1
    else:
        velocidad_actual = PLAYER_VELOCITY

    # Detectamos colisión con planta
    if hero_rect.colliderect(planta_rect):
        exito_sound.play()
        puntos += 1
        
        if kers_actual < 100:
            kers_actual += 7

        planta_rect.x = random.randint(32, WINDOW_WIDTH - 32)
        planta_rect.y = random.randint(112, WINDOW_HEIGHT - 32)

        bot_rect.x = random.randint(32, WINDOW_WIDTH - 32)
        bot_rect.y = random.randint(112, WINDOW_HEIGHT - 32)

    # Detectamos colisión con botella
    if hero_rect.colliderect(bot_rect):
        golpe_sound.play()
        vidas -= 1

        if vidas <= 0:
            pausado = True
            pygame.mixer.music.set_volume(0)
            display_surface.blit(gameover_text, gameover_rect)
            display_surface.blit(presskey_text, presskey_rect)
            display_surface.blit(quit_text, quit_rect)

            pygame.display.update()
            pygame.mixer.music.stop()

            while pausado:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pausado = False
                            running = False

                        elif event.key == pygame.K_c:
                            pausado = False

                            puntos = 0
                            kers_actual = MAX_KERS
                            velocidad_actual = PLAYER_VELOCITY
                            vidas = PLAYER_STARTING_LIVES

                            pygame.mixer.music.play(-1, 0.0)
                            pygame.mixer.music.set_volume(0.2)


        planta_rect.x = random.randint(20, WINDOW_WIDTH)
        planta_rect.y = random.randint(100, WINDOW_HEIGHT)

        bot_rect.x = random.randint(20, WINDOW_WIDTH)
        bot_rect.y = random.randint(100, WINDOW_HEIGHT)

    
    # Cronometro
    segundos = int(pygame.time.get_ticks()/1000)

    if aux == segundos:
        aux+=1
        aux2+=1 
        
        if segundos % 60 == 0:
            minutos += 1
            aux2 = 0

        text_minutos = str(minutos).zfill(2)
        text_segundos = str(aux2).zfill(2)
        # print(f'Tiempo: {text_minutos}:{text_segundos}')


	# Actualizar HUD
    velocidad_text = fuente_pixel.render(f'Velocidad: 0', True, GREEN, DARKGREEN)
    puntos_text = fuente_pixel.render(f'Puntos: {puntos}',  True, AMARILLO)
    kers_text = fuente_pixel_chica.render(f'Kers: {kers_actual}', True, AMARILLO)
    vidas_text = fuente_pixel_chica.render(f'Vidas: {vidas}', True, AMARILLO)
    tiempo_text = fuente_pixel_chica.render(f'Tiempo: {text_minutos}:{text_segundos}', True, AMARILLO)
    

	# Pintar de negro la pantalla
    # display_surface.fill(GREY)
    display_surface.blit(bg, (0, 0))


	# Pintar la cabecera
    display_surface.blit(puntos_text, puntos_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(kers_text, kers_rect)
    display_surface.blit(vidas_text, vidas_rect)
    display_surface.blit(tiempo_text, tiempo_rect)
    display_surface.blit(instrucciones_text, instrucciones_rect)
    display_surface.blit(pausa_text, pausa_rect)
    display_surface.blit(instrucciones_salir_text, instrucciones_salir_rect)

	# Linea blanca que separa el HUD del area de juego
    pygame.draw.line(display_surface, WHITE, (0,80), (WINDOW_WIDTH, 80), 2)

	# Bordes de la pista
	# pygame.draw.line(display_surface, WHITE, (150,64), (150, WINDOW_HEIGHT), 10)
	# pygame.draw.line(display_surface, WHITE, (WINDOW_WIDTH - 150,64), (WINDOW_WIDTH - 150, WINDOW_HEIGHT), 10)

	# Pintar jugador y planta
    display_surface.blit(hero_img, hero_rect)
    display_surface.blit(planta_img, planta_rect)
    display_surface.blit(bot_img, bot_rect)
    # Dibujar el rect del hero
    # pygame.draw.rect(display_surface, GREEN, hero_rect, 1)


	# Actualizar la pantalla
    pygame.display.update()

	# Tick the clock
    clock.tick(FPS)

    # Frenar juego por tiempo
    if segundos == 10:
        pausado = True
        pygame.mixer.music.set_volume(0.05)

        display_surface.blit(pausa_cartel_text, pausa_cartel_rect)
        display_surface.blit(presskey_pausa_text, presskey_pausa_rect)
        pygame.display.update()

        # CONTINUAR
        while pausado:
            print('FIN DEl JUEGO POR TIEMPO')


# Cerrar juego
pygame.quit()