import pygame
import word

WIDTH = 800
HEIGHT = 600

def display():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("KeyBoard Jump Game")
    gameloop(window)

def gameloop(window):
    speed = 0.5
    newWord = word.word(speed)
    score = 0
    begin = True
    while True:
        if begin:
            menu(window, True, score)
        begin = False
        background = pygame.image.load("source/teacher-background.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        character = pygame.image.load("source/char.jpg")
        character = pygame.transform.scale(character, (50,50))
        wood = pygame.image.load("source/wood-.png")
        wood = pygame.transform.scale(wood, (90,50))
        window.blit(background, (0,0))
        newWord.y += newWord.wordSpeed
        window.blit(wood,(newWord.x-50,newWord.y+15))
        window.blit(character,(newWord.x-100,newWord.y))
        drawText(window, str(newWord.displayword), 40, newWord.x, newWord.y)
        drawText(window, 'Score:'+str(score), 40, WIDTH/2 , 5)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               # print(pygame.key.name(event.key))
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    newWord.yourWord += pygame.key.name(event.key)
                    if newWord.displayword.startswith(newWord.yourWord):
                        if newWord.displayword == newWord.yourWord:
                            score += len(newWord.displayword)
                            speed += 0.1
                            newWord = word.word(speed)
                    else:
                        menu(window, False, score)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if newWord.y < HEIGHT-5:
            pygame.display.update()
        else:
            menu(window, False, score)

def drawText(display, text, size, x, y):
    font_name = pygame.font.match_font("source/comic.ttf")
    font = pygame.font.Font(font_name, size)
    textDraw = font.render(text, True, (0,0,0))
    rect = textDraw.get_rect()
    rect.midtop = (x, y)
    display.blit(textDraw, rect)

def menu(display, begin, score):
    if begin:
        bg = pygame.image.load("source/keyback.jpg")
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        display.blit(bg, (0,0))
        drawText(display, "Press a key to begin!", 54, WIDTH / 2, 500)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    waiting = False
    else:
        bg = pygame.image.load("source/teacher-background.jpg")
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        display.blit(bg, (0,0))
        drawText(display, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        drawText(display,"Score : " + str(score), 70, WIDTH / 2, HEIGHT /2)
        drawText(display, "Press R to play again, ESC to quit", 54, WIDTH / 2, 500)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        gameloop(display)