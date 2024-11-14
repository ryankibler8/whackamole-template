import pygame
import random


def draw_grid(screen):
    grid_line_color = (0, 0, 0)  
    for x in range(0, 640, 32):
        pygame.draw.line(screen, grid_line_color, (x, 0), (x, 512))
    for y in range(0, 512, 32):
        pygame.draw.line(screen, grid_line_color, (0, y), (640, y))


def get_random_position():
    x = random.randrange(0, 20) * 32
    y = random.randrange(0, 16) * 32
    return x, y


def main():
    try:
        pygame.init()
        
        screen = pygame.display.set_mode((640, 512))
        
        clock = pygame.time.Clock()

        mole_image = pygame.image.load("mole.png")
        
        mole_pos = (0, 0)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_image.get_rect(topleft=mole_pos).collidepoint(event.pos):
                        mole_pos = get_random_position()

            screen.fill((255, 165, 0))
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
