import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

width = 20
height = 20
margin = 5

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)
grid[1][5] = 1

pygame.init()
window_size = [255, 255]
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test Grid")
done = False
clock = pygame.time.Clock()
screen.fill(black)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][column] = 1

    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = red
            pygame.draw.rect(screen, color, [(margin + width) * column + margin,
                             (margin + height) * row + margin, width, height])
    clock.tick(50)
    pygame.display.flip()
pygame.quit()
