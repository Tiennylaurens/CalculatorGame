
import pygame, os, time, sys
from Button import Buttons
from Game import CalcGame
from tracker import Status

pygame.init()
#define first variables
width, height = 900, 500
middle = width / 2
transition_width = 500
transition_height = 500
transition_vel = 10
transition_start_left = -500
transition_start_right = 900
calc_scale = 0.8
lettergrote = 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator Corruption")

white = (255, 255, 255)
black = (0,0,0)
groen = (189, 236, 182)

FPS = 45
clock = pygame.time.Clock()

#raw images
calculator_image_orange = pygame.image.load(os.path.join("Assets", "CalculatorOrange.png")).convert_alpha()
calculator_image = pygame.image.load(os.path.join("Assets", "Calculator.png")).convert_alpha()
start_image = pygame.image.load(os.path.join("Assets", "start.png")).convert_alpha()
finish_image = pygame.image.load(os.path.join("Assets", "finish.png")).convert_alpha()
arrow_image = pygame.image.load(os.path.join("Assets", "Arrow.png")).convert_alpha()
realcalc_image = pygame.image.load(os.path.join("Assets", "realcalc.png")).convert_alpha()
exit_image = pygame.image.load(os.path.join("Assets", "exit_btn.png")).convert_alpha()
blank_image = pygame.image.load(os.path.join("Assets", "blank.png")).convert_alpha()
correct_image = pygame.image.load(os.path.join("Assets", "correct.png")).convert_alpha()
false_image = pygame.image.load(os.path.join("Assets", "false.png")).convert_alpha()
#scaled and rotated images
calculator_orange = pygame.transform.scale(calculator_image_orange, (300, 300))
left_arrow = pygame.transform.scale(arrow_image, (transition_width, transition_height))
right_arrow = pygame.transform.rotate((pygame.transform.scale(arrow_image, (transition_width, transition_height))), 180)
realcalc = pygame.transform.scale(realcalc_image, (realcalc_image.get_width() * calc_scale, realcalc_image.get_height()* calc_scale))
correct = pygame.transform.scale(correct_image, (75, 75))
false = pygame.transform.scale(false_image, (75, 75))

#define button instances 
start_button = Buttons(384, 400, start_image, 0.2)
exit_button = Buttons(780, 50, exit_image, 0.35)
button_1 = Buttons(455, 305, blank_image, 0.0327)
button_2 = Buttons(378.5, 305, blank_image, 0.0327)
button_3 = Buttons(302, 305, blank_image, 0.0327)
button_6 = Buttons(455, 228, blank_image, 0.0327)
button_5 = Buttons(378.5, 228, blank_image, 0.0327)
button_4 = Buttons(302, 228, blank_image, 0.0327)
button_9 = Buttons(455, 151, blank_image, 0.0327)
button_8 = Buttons(378.5, 151, blank_image, 0.0327)
button_7 = Buttons(302, 151, blank_image, 0.0327)
button_devide = Buttons(531.5, 151, blank_image, 0.0327)
button_mult = Buttons(531.5, 228, blank_image, 0.0327)
button_sub = Buttons(531.5, 305, blank_image, 0.0327)
button_add = Buttons(531.5, 382, blank_image, 0.0327)

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#define game instance
game = CalcGame()
status = Status()
left_rect = pygame.Rect(transition_start_left, 0, transition_width, transition_height)
right_rect = pygame.Rect(transition_start_right, 0, transition_width, transition_height)


#define some variables 
calc_width = realcalc.get_width()
calc_x = middle - (calc_width / 2)

#define function that makes calculation font
def make_calc_font():
    calc_font = pygame.font.SysFont('freesansbold.ttf', lettergrote)
    calc_text = calc_font.render(game.calculation, True, black, groen)
    calcrect = calc_text.get_rect()
    calcrect.center = (450, 95)
    screen.blit(calc_text, calcrect)

#define function that makes text font
def make_text_font(words, lettertype):
    text_font = pygame.font.SysFont('freesansbold.ttf', lettertype)
    text = text_font.render(words, True, white, black)
    textrect = text.get_rect()
    textrect.center = (450, 95)
    screen.blit(text, textrect)

#define funciton that makes end font
def make_end_font():   
    end_font = pygame.font.SysFont('freesansbold.ttf', 60)
    end_text = end_font.render("Congraulations You Won!", True, white, black)
    endrect = end_text.get_rect()
    endrect.center = (450, 100)
    screen.blit(end_text, endrect)

#set difficulty
def set_difficulty():
    if button_1.draw(screen):
        game.set_difficulty(1)
    if button_2.draw(screen):
        game.set_difficulty(2)
    if button_3.draw(screen):
        game.set_difficulty(3)

#set amount of rounds function 
def set_amount_of_rounds():
    if button_1.draw(screen):
        game.set_rounds(1)
    if button_2.draw(screen):
        game.set_rounds(2)
    if button_3.draw(screen):
        game.set_rounds(3)
    if button_4.draw(screen):
        game.set_rounds(4)
    if button_5.draw(screen):
        game.set_rounds(5)
    if button_6.draw(screen):
        game.set_rounds(6)
    if button_7.draw(screen):
        game.set_rounds(7)
    if button_8.draw(screen):
        game.set_rounds(8)
    if button_9.draw(screen):
        game.set_rounds(9)

#define function that handles the game logic
def handle_game_logic():
    if game.faults == 3:
        status.set_finished()
    if not game.player_operator:
        if button_add.draw(screen):
            game.set_player_operator(1)
        if button_sub.draw(screen):
            game.set_player_operator(2)
        if button_mult.draw(screen):
            game.set_player_operator(3)
        if button_devide.draw(screen):
            game.set_player_operator(4)

    if game.player_operator:
        if button_1.draw(screen):
            game.set_player_number(1)
        if button_2.draw(screen):
            game.set_player_number(2)
        if button_3.draw(screen):
            game.set_player_number(3)
        if button_4.draw(screen):
            game.set_player_number(4)
        if button_5.draw(screen):
            game.set_player_number(5)
        if button_6.draw(screen):
            game.set_player_number(6)
        if button_7.draw(screen):
            game.set_player_number(7)
        if button_8.draw(screen):
            game.set_player_number(8)
        if button_9.draw(screen):
            game.set_player_number(9)
        
    if game.player_number and game.player_operator:
        game.set_prev_calc(game.calculation)
        if game.player_number == game.number and game.player_operator == game.operator:
            reset_calc()
            game.up_rounds()
            game.prev_right = True
            game.prev_wrong = None
            if game.player_rounds == game.rounds:
                status.set_finished()
            else: 
                game.set_calculation(game.new_play_window())
        else:
            game.prev_wrong = True
            game.prev_right = None
            game.up_faults()
            reset_calc()
            game.set_calculation(game.play_wrong())

def draw_lives():
    score_font = pygame.font.SysFont('freesansbold.ttf', 30)
    score_text = score_font.render("{}/3 Lives".format(3 - game.faults), True, black, white)
    scorerect = score_text.get_rect()
    scorerect.center = (800, 50)
    screen.blit(score_text, scorerect)

def draw_score():
    score_font = pygame.font.SysFont('freesansbold.ttf', lettergrote)
    score_text = score_font.render("{}/{}".format(game.player_rounds, game.rounds), True, black, white)
    scorerect = score_text.get_rect()
    scorerect.center = (50, 50)
    screen.blit(score_text, scorerect)

#define function that draws status menu
def draw_start_window():
    screen.fill(white)
    if not status.started_game:
        screen.blit(calculator_orange, (300, 45))
    if not status.started_game:
        if start_button.draw(screen):
            status.set_started()
        if exit_button.draw(screen):
            status.run = False
    if status.started_game:
        transition()
    pygame.display.update()

#define function that draws the game window
def draw_round_window():
    #drawing score and calc on screen
    screen.fill(white)
    screen.blit(realcalc, (calc_x, 35))
    #set difficulty
    if not game.difficulty:
        make_text_font("Select difficulty 1=Easy 2=Normal 3=hard", 15)
        set_difficulty()
    #draw rounds
    if game.prev_right:
        screen.blit(correct, (40, 100))
    if game.prev_wrong:
        screen.blit(false, (40,100))
    if game.rounds:
        draw_score()
        draw_lives()
    #set first calculation
    if not game.calculation:
       game.set_calculation(game.new_play_window())
    #making the text font that shows the calculation
    if game.difficulty and not game.rounds:
        #set amount of rounds
        make_text_font("Select amount of rounds", 24)
        set_amount_of_rounds()
    if game.rounds:
        #adding text for calculation
        make_calc_font()
        if game.prev_calc:
            text_font = pygame.font.SysFont('freesansbold.ttf', 24)
            text = text_font.render(game.prev_calc, True, white, black)
            textrect = text.get_rect()
            textrect.center = (100, 250)
            screen.blit(text, textrect)
        #hanlding game logic
        handle_game_logic()
    if status.finished_game:
        #start transition
        if game.player_rounds == game.rounds: 
            if not status.end_score_displayed:
                make_end_font()
                draw_score()
                pygame.display.update()
                time.sleep(2)
                status.set_end_score()
            if status.end_score_displayed:
                transition()
        else: 
            if not status.end_score_displayed:
                make_text_font("You lost", 40)
                pygame.display.update()
                time.sleep(2)
                status.set_end_score()
            if status.end_score_displayed:
                transition()


    pygame.display.update()

#define function that draws a transition for the menu screen 
def transition():
    handle_transition_movement()
    screen.blit(left_arrow, (left_rect.x, left_rect.y))
    screen.blit(right_arrow, (right_rect.x, right_rect.y))
    pygame.display.update

#define function that resets transition
def reset_transition():
    left_rect.x = transition_start_left
    right_rect.x = transition_start_right

#define function that resets status variables
def reset_status():
    status.started_game = False
    status.finished_first_tran = False
    status.finished_game = False
    status.end_score_displayed = False 
    game.clear_rounds()
    game.clear_player()
    game.clear_num_op()

#define function that reset status number and operator variables
def reset_calc():
    game.player_number = None
    game.player_operator = None

#define function that handles the transition movement
def handle_transition_movement():
    if left_rect.x + transition_vel <= middle - transition_width and right_rect.x - transition_vel >= middle:
        left_rect.x += transition_vel
        right_rect.x -= transition_vel
    else:
        if not status.finished_game:
            status.set_finished_first_tran()
            reset_transition()
        if status.finished_game:
            reset_status()
            reset_transition()

#main game looop
def main():
    while status.run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status.run = False
        if not status.finished_first_tran:
            draw_start_window()
        if status.finished_first_tran:
            draw_round_window() 
    pygame.quit()

if __name__ == "__main__":
    main()