import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


player_pos = pygame.Vector2(400, 300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("yellow")

    pygame.draw.circle(screen, "blue", player_pos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -=10*dt
    if keys[pygame.K_UP]:
        player_pos.y-=10*dt
    if keys[pygame.K_RIGHT]:
        player_pos.x+=10*dt
    if keys[pygame.K_DOWN]:
        player_pos.y+=10*dt
    pygame.display.flip()
    dt= clock.tick(60)/1000
pygame.quit()