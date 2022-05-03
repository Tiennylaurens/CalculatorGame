import pygame, os
from Button import Buttons
from Game import CalcGame

class Start:
    def __init__(self):
        self.started = False
        self.two = False
    def set_true(self):
        self.started = True
    def set_two(self):
        self.two = True

width, height = 900, 500
middle = width / 2
transition_width = 500
transition_height = 500
transition_vel = 10
transition_start_left = -500
transition_start_right = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator Corruption")

white = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

#raw images
calculator_image_orange= pygame.image.load(os.path.join("Assets", "CalculatorOrange.png")).convert_alpha()
calculator_image = pygame.image.load(os.path.join("Assets", "Calculator.png")).convert_alpha()
start_image = pygame.image.load(os.path.join("Assets", "start.png")).convert_alpha()
finish_image = pygame.image.load(os.path.join("Assets", "finish.png")).convert_alpha()
arrow_image = pygame.image.load(os.path.join("Assets", "Arrow.png")).convert_alpha()

#scaled and rotated images
calculator_orange = pygame.transform.scale(calculator_image_orange, (300, 300))
left_arrow = pygame.transform.scale(arrow_image, (transition_width, transition_height))
right_arrow = pygame.transform.rotate((pygame.transform.scale(arrow_image, (transition_width, transition_height))), 180)

#define button instances 
start_button = Buttons(384, 400, start_image, 0.2)

#define game instance
game = CalcGame()
start = Start()
left_rect = pygame.Rect(transition_start_left, 0, transition_width, transition_height)
right_rect = pygame.Rect(transition_start_right, 0, transition_width, transition_height)

#define function that draws start menu
def draw_start_window():
    screen.fill(white)
    if not start.started:
        screen.blit(calculator_orange, (300,45))
    if not start.started:
        if start_button.draw(screen):
            start.set_true()
    if start.started:
        transition()
    pygame.display.update()
        
#define function that draws a transition for the menu screen 
def help_transition():
    handle_transition_movement()
    screen.blit(left_arrow, (left_rect.x, left_rect.y))
    screen.blit(right_arrow, (right_rect.x, right_rect.y))

def transition():
    handle_transition_movement()
    screen.blit(left_arrow, (left_rect.x, left_rect.y))
    screen.blit(right_arrow, (right_rect.x, right_rect.y))
    pygame.display.update

#define function that resets transition
def reset_transition():
    left_rect.x = transition_start_left
    right_rect.x = transition_start_right

#define function that handles the transition movement
def handle_transition_movement():
    if left_rect.x + transition_vel <= middle - transition_width and right_rect.x - transition_vel >= middle:
        left_rect.x += transition_vel
        right_rect.x -= transition_vel
    else:
        start.set_two()
        reset_transition()

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not start.two:
            draw_start_window()
        if start.two:
            #draw_start_window()
            run = False
    pygame.quit()

if __name__ == "__main__":
    main()