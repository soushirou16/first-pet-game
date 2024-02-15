import pygame
import sys
from button import Button
import random

pygame.init()
info = pygame.display.Info()
pygame.display.set_caption("lil pet game")
clock = pygame.time.Clock()

#SCALING BACKGROUNND TO FIT SCREEN
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load('mypetgame/imgs/background.jpg').convert_alpha()
background_rect = background_image.get_rect()
scale_factor_x = SCREEN_WIDTH / background_rect.width
scale_factor_y = SCREEN_HEIGHT / background_rect.height
scaled_width = int(background_rect.width * scale_factor_x)
scaled_height = int(background_rect.height * scale_factor_y)
scaled_background = pygame.transform.scale(background_image, (scaled_width, scaled_height))
scaled_rect = scaled_background.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
textFont = pygame.font.Font('mypetgame/font/Pixeltype.ttf', 50)
deathMsg = textFont.render(f'Kitty was neglected, and passed away!', False, "black")
deathMsgRect = deathMsg.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))

#LOADING SPRITES
catidleRight1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle1.png').convert_alpha(), 4.5)
catidleRight2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle2.png').convert_alpha(), 4.5)
catidleRight3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle3.png').convert_alpha(), 4.5)
catidleRight4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle4.png').convert_alpha(), 4.5)
catidleLeft1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle5.png').convert_alpha(), 4.5)
catidleLeft2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle6.png').convert_alpha(), 4.5)
catidleLeft3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle7.png').convert_alpha(), 4.5)
catidleLeft4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/idle/Idle8.png').convert_alpha(), 4.5)
catWalkRight1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight1.png').convert_alpha(), 4.5)
catWalkRight2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight2.png').convert_alpha(), 4.5)
catWalkRight3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight3.png').convert_alpha(), 4.5)
catWalkRight4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight4.png').convert_alpha(), 4.5)
catWalkRight5 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight5.png').convert_alpha(), 4.5)
catWalkRight6 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkRight6.png').convert_alpha(), 4.5)
catWalkLeft1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft1.png').convert_alpha(), 4.5)
catWalkLeft2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft2.png').convert_alpha(), 4.5)
catWalkLeft3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft3.png').convert_alpha(), 4.5)
catWalkLeft4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft4.png').convert_alpha(), 4.5)
catWalkLeft5 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft5.png').convert_alpha(), 4.5)
catWalkLeft6 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/walk/walkLeft6.png').convert_alpha(), 4.5)
catAttackRight1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackRight1.png').convert_alpha(), 4.5)
catAttackRight2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackRight2.png').convert_alpha(), 4.5)
catAttackRight3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackRight3.png').convert_alpha(), 4.5)
catAttackRight4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackRight4.png').convert_alpha(), 4.5)
catAttackLeft1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackLeft1.png').convert_alpha(), 4.5)
catAttackLeft2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackLeft2.png').convert_alpha(), 4.5)
catAttackLeft3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackLeft3.png').convert_alpha(), 4.5)
catAttackLeft4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/attack/attackLeft4.png').convert_alpha(), 4.5)
catDeadRight1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead1.png').convert_alpha(), 4.5)
catDeadRight2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead2.png').convert_alpha(), 4.5)
catDeadRight3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead3.png').convert_alpha(), 4.5)
catDeadRight4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead4.png').convert_alpha(), 4.5)
catDeadLeft1 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead5.png').convert_alpha(), 4.5)
catDeadLeft2 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead6.png').convert_alpha(), 4.5)
catDeadLeft3 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead7.png').convert_alpha(), 4.5)
catDeadLeft4 = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/cat/dead/dead8.png').convert_alpha(), 4.5)
redBar = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/redbar.png').convert_alpha(), 0.8)
orangeBar = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/orangebar.png').convert_alpha(), 0.8)
yellowBar = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/yellowbar.png').convert_alpha(), 0.8)
greenBar = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/greenbar.png').convert_alpha(), 0.8)
waterDroplet = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/water.png').convert_alpha(), 0.15)
foodBowl = pygame.transform.scale_by(pygame.image.load('mypetgame/imgs/lifebars/foodbowl.png').convert_alpha(), 0.2)
catIdleListBoth = [[catidleRight1, catidleRight2, catidleRight3, catidleRight4], [catidleLeft1, catidleLeft2, catidleLeft3, catidleLeft4]]
catWalkListBoth = [[catWalkRight1, catWalkRight2, catWalkRight3, catWalkRight4, catWalkRight5, catWalkRight6], [catWalkLeft1, catWalkLeft2, catWalkLeft3, catWalkLeft4, catWalkLeft5, catWalkLeft6]]
catAttackListBoth = [[catAttackRight1, catAttackRight2, catAttackRight3, catAttackRight4], [catAttackLeft1, catAttackLeft2, catAttackLeft3, catAttackLeft4]]
catDeadListBoth = [[catDeadRight1, catDeadRight2, catDeadRight3, catDeadRight4], [catDeadLeft1, catDeadLeft2, catDeadLeft3, catDeadLeft4]]
barList = [redBar, orangeBar, yellowBar, greenBar, redBar]

#GET CURRENT STATS
currStat = []
with open("mypetgame/stats.txt", "r") as allStats:
    for line in allStats:
        specStat = line.split()
        for stat in specStat:
            currStat.append(float(stat))
allStats.close()

#INITIALIZE STARTING POSITIONS
catFacingRight = 1
idleCatCounter = 0
walkCatCounter = 0
attackCatCounter = 0
catDeathCounter = 0
catMoving = False
catAttacked = False
catRect = catidleRight1.get_rect(bottomleft = (320, SCREEN_HEIGHT/1.75))

#INITIALIZE BUTTONS
quitButton = Button(10, scaled_height - 40, 70, 30, (118,181,197), 'quit')
feedButton = Button(100, scaled_height - 40, 70, 30, (118,181,197), 'feed')
drinkButton = Button(190, scaled_height - 40, 70, 30, (118,181,197), 'drink')
reviveButton = Button((SCREEN_WIDTH/2)-50, SCREEN_HEIGHT/5, 100, 50, "light blue", 'Revive')

def checkButtons(mousepos):
    global catDeathCounter
    global catAttacked
    global scaled_background

    if(quitButton.is_clicked(mousepos)):
            with open("mypetgame/stats.txt", "w") as file:
                for stat in currStat:
                    file.write(str(stat) + " ")
            file.close
                    
            pygame.quit()
            sys.exit()

    if(catDeathCounter == 0):
        if(catRect.collidepoint(mousepos)):
            catAttacked = True
        
        elif(feedButton.is_clicked(mousepos) or drinkButton.is_clicked(mousepos)):
            if(feedButton.is_clicked(mousepos)):
                i = 0
            else:
                i = 1

            if(currStat[i] < 100):
                currStat[i] += 20
                if(currStat[i] >= 100):
                    currStat[i] = 99.9999
    else:
        if(reviveButton.is_clicked(mousepos)):
            scaled_background = pygame.transform.scale(background_image, (scaled_width, scaled_height))
            currStat[0] = 99.99
            currStat[1] = 99.99
            catDeathCounter = 0

def printButtons():
    quitButton.draw(screen)
    feedButton.draw(screen)
    drinkButton.draw(screen)

def printObjects():
    screen.blit(scaled_background, scaled_rect)
    screen.blit(waterDroplet, (SCREEN_WIDTH - 242, 45))
    screen.blit(foodBowl, (SCREEN_WIDTH - 250, 15))
    screen.blit(barList[int(currStat[0]//25)], (SCREEN_WIDTH - 200, 10))
    screen.blit(barList[int(currStat[1]//25)], (SCREEN_WIDTH - 200, 50))

def attackCat(catFacingRight):
    global catAttacked
    global attackCatCounter
    attackCatCounter = attackCatCounter + 0.2

    if(attackCatCounter < 4):
        cat = catAttackListBoth[catFacingRight][int(attackCatCounter)]
    else:
        cat = catAttackListBoth[catFacingRight][0]
        attackCatCounter = 0
        catAttacked = False

    screen.blit(cat, catRect)
    
def idleCat(catFacingRight):
    global idleCatCounter
    idleCatCounter = idleCatCounter + 0.1
    i = idleCatCounter % 4
    cat = catIdleListBoth[catFacingRight][int(i)]
    screen.blit(cat, catRect)

def moveCat(catFacingRight):
    global walkCatCounter
    global catMoving
    walkCatCounter = walkCatCounter + 0.2

    if(walkCatCounter < 6):
        cat = catWalkListBoth[catFacingRight][int(walkCatCounter)]
    else:
        walkCatCounter = 0
        cat = catIdleListBoth[catFacingRight][0]
        catMoving = False

    if(catFacingRight == 0):
        catRect.x = catRect.x + 4
    else:
        catRect.x = catRect.x - 4

    screen.blit(cat, catRect)

    #peekaboo!

def catDied(catFacingRight):
    global catDeathCounter
    catDeathCounter = catDeathCounter + 0.1
    reviveButton.draw(screen)
    screen.blit(deathMsg, deathMsgRect)
    scaled_background.fill((190, 0, 0, 100), special_flags=pygame.BLEND_ADD)
    
    if(catDeathCounter < 4):
        cat = catDeadListBoth[catFacingRight][int(catDeathCounter)]
    else:
        cat = catDeadListBoth[catFacingRight][3]
    
    screen.blit(cat, catRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("mypetgame/stats.txt", "w") as file:
                for stat in currStat:
                    file.write(str(stat) + " ")
            file.close
                
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            checkButtons(pygame.mouse.get_pos())

    #GAME LOOP
    printObjects()
    printButtons()

    
    if(currStat[0] > 0):
        currStat[0] -= 0.02
    if(currStat[1] > 0):
        currStat[1] -= 0.036

    #ACTION RANDOMMIZER
    randInt = random.randint(1, 240)

    if(currStat[0] < 0 and currStat[1] < 0):
        catDied(catFacingRight)
    else:

        if(randInt == 1):
            if(catFacingRight == 1):
                catFacingRight = 0
            else:
                catFacingRight = 1
        elif(randInt == 2 or randInt == 3):
            catMoving = True
        
        elif(catAttacked):
            attackCat(catFacingRight)
        elif(catMoving and not catAttacked):
            if(catRect.x > SCREEN_WIDTH - 120):
                catFacingRight = 1
            elif(catRect.x < 120):
                catFacingRight = 0
            moveCat(catFacingRight)
        else:
            idleCat(catFacingRight)
    
    clock.tick(60)
    pygame.display.update()