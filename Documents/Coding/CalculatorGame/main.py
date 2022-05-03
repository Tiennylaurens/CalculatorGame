import pygame, Game, os
from Button import Buttons

width, height = 900, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator Corruption")

white = (255, 255, 255)

FPS = 60

#raw images
calculator_image_orange= pygame.image.load(os.path.join("Assets", "CalculatorOrange.png"))
calculator_image = pygame.image.load(os.path.join("Assets", "Calculator.png"))
start_image = pygame.image.load(os.path.join("Assets", "start.png")).convert_alpha()
finish_image = pygame.image.load(os.path.join("Assets", "finish.png")).convert_alpha()


#scaled and rotated images
calculator_orange = pygame.transform.scale(calculator_image_orange, (300, 300))

#define button instances 
start_button = Buttons(384, 400, start_image, 0.2)

def draw_window():
    screen.fill(white)
    screen.blit(calculator_orange, (300,45))
    if start_button.draw(screen):
        print("Clicked")
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