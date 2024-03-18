import pygame
import random

pygame.init()

#colours 
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0 )

#screen parameters
WIDTH = 600
HEIGHT = 300

#variables
score = 0
cubeX = 50
cubeY = 300
pos_y = 0
pos_x = 0
jump = 1
obstacles = [450, 600, 750]
enemies_speed = 2
game_on = True

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Cube Runner")
fps = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer = pygame.time.Clock()

run = True

#while loop
while run:
    timer.tick(fps)
    screen.fill(black)

    #text of instructions if player dies
    if game_on:
        text = font.render("Jump with 'UP Key' and Move with 'Left/Right key'", True, white, black)
        screen.blit(text, (120, 70))
        text2 = font.render("Game progressively gets harder", True, white, black)
        screen.blit(text2, (185, 100))
    if not game_on:
        text3 = font.render("Press Space Bar to re-start the game", True, white, black)
        screen.blit(text3, (165, 70))

    #score
    score_text = font.render(f"Score: {score}", True, white, black)
    screen.blit(score_text, (500, 20)) 

    #print infinite ground
    ground = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])

    #print cube
    cube = pygame.draw.rect(screen, green, [cubeX, cubeY, 20, 20])

    #print enemies
    enemy0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    enemy1 = pygame.draw.rect(screen, red, [obstacles[1], 200, 20, 20])
    enemy2 = pygame.draw.rect(screen, red, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and not game_on:
            if event.key == pygame.K_SPACE and pos_y == 0:
                obstacles = [450, 600, 750]
                cubeX = 50
                score = 0
                game_on = True

        if event.type == pygame.KEYDOWN and game_on:
            #jumping
            if event.key == pygame.K_UP and pos_y == 0:
                pos_y = 16
                if score >= 5:
                    pos_y = 13
                    if score >= 10 and score < 15:
                        pos_y = 10
                        if score >= 15:
                            pos_y = 13
                        if score >= 20:
                            pos_y = 10
            #moving
            if event.key == pygame.K_RIGHT:
                pos_x = 2
                if score >= 15:
                    pos_x = 1
            if event.key == pygame.K_LEFT:
                pos_x = -2
                if score >= 15:
                    pos_x = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pos_x = 0
            if event.key == pygame.K_LEFT:
                pos_x = 0

    #randomly spawn enemies
    for i in range(len(obstacles)):
        if game_on:
            obstacles[i] -= enemies_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(600, 700)
                score += 1
            if cube.colliderect(enemy0) or cube.colliderect(enemy1) or cube.colliderect(enemy2):
                game_on = False

    #moving
    if 0 <= cubeX <= 580:
        cubeX += pos_x
    if cubeX < 0:
        cubeX = 0
    if cubeX > 580:
        cubeX = 580

    #jumping
    if pos_y > 0 or cubeY < 200:
        cubeY -= pos_y
        pos_y -= jump
    if cubeY > 200:
        cubeY = 200
    if cubeY == 200 and pos_y < 0:
        pos_y = 0

    pygame.display.flip()
pygame.quit()