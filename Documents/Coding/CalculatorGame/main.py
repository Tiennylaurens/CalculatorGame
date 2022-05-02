import pygame, Game, os

WHITE = (255, 255, 255)

FPS = 60

CALCULATOR_IMAGE_ORANGE = pygame.image.load(os.path.join("Assets", "CalculatorOrange.png"))
CALCULATOR_IMAGE = pygame.image.load(os.path.join("Assets", "Calculator.png"))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator Corruption")

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(CALCULATOR_IMAGE_ORANGE, (300,100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()