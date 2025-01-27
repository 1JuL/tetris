import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
msg_font = pygame.font.Font(None, 25)
controls_font = pygame.font.Font(None, 16)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
move_control_surface = controls_font.render("Use Arrow Keys to Move Blocks",True,Colors.white)
rotate_control_surface = controls_font.render("Up Arrow to Rotate",True,Colors.white)
pause_control_surface = controls_font.render("P to Pause, U to Unpause",True,Colors.white)
menu_controls_surface = controls_font.render("ESC to Exit Game",True,Colors.white)

game_over_surface = title_font.render("GAME OVER", True, Colors.white)
game_over_msg_surface = msg_font.render("Press 'R' to restart!!", True, Colors.yellow)

score_rect = pygame.Rect(325, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
GAME_TIMER = 300
pygame.time.set_timer(GAME_UPDATE, GAME_TIMER)

next_score_target = 1000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                if event.key == pygame.K_r:
                    game.game_over = False
                    game.reset()
            
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.key == pygame.K_p and game.game_over == False:
                game.pause_game()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
                
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        
    #Difficulty increase    
    if game.score >= next_score_target:
        GAME_TIMER = max(50, GAME_TIMER - 20)
        print(GAME_TIMER)
        pygame.time.set_timer(GAME_UPDATE, GAME_TIMER)
        next_score_target += 1000
        
    #Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    screen.blit(move_control_surface, (320, 420, 50, 50))
    screen.blit(rotate_control_surface, (355, 440, 50, 50))
    screen.blit(pause_control_surface, (340, 460, 50, 50))
    screen.blit(menu_controls_surface, (360, 480, 50, 50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 520, 50, 50))
        screen.blit(game_over_msg_surface, (325, 570, 50, 50))
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0 ,10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0 ,10)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(144)