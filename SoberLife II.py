#  Sober Life--written by Bruce Baskir July 2019

import sys
import pygame
import random
import time
pygame.init()
font = pygame.font.Font(None, 48)

def findpos(funcx,funcy):  #converts location mouse to square on board
    flag = 0
    ypos = 0
    xpos = 0
    if funcx < 0:  flag = 1
    if funcx > 1499:  flag = 1
    if funcy < 0:  flag = 1
    if funcy > 599:  flag = 1
    if flag == 0:
        ypos = int(funcy/200)
        if ypos%2 == 0:
            if funcx > 150 and funcx < 1350:
                xpos = 2 * int((funcx - 150)/300)+1
            else:  flag = 1
        else:
            xpos = 2*int(funcx/300)
    return xpos,ypos,flag

def timeprint(functime,funcx,funcy):
    ampm = 0    #  0 = am   1 = pm
    hours = int(functime/4)+ 8
    if hours > 11:
        ampm = 1
    if hours > 12:
        hours = hours - 12
    minutes = 15 * (functime%4)
    minutes = str(minutes)
    if minutes == "0":
        minutes = "00"
    display = str(hours)+":"+minutes
    if ampm == 0:
        display = display + " am"
    else:
        display = display + " pm"
    text = font.render(display,True,(100,100,100))
    screen.blit(text,(funcx*150+100,funcy*200+80))

def makedeck(funcdiff):  #generates unshuffled deck
    funcdeck = []
    counter = 0
    while counter < funcdiff[0]:
        funcdeck.append(-2)  # exercise = -2
        counter = counter + 1
    while counter < funcdiff[1]:
        funcdeck.append(-3)  # meditation = -3
        counter = counter + 1
    while counter < funcdiff[2]:  #jobstress = 10
        funcdeck.append(11)
        counter = counter + 1
    while counter < funcdiff[3]:  #family = 20
        funcdeck.append(21)
        counter = counter + 1
    while counter < 50:  #health = 30
        funcdeck.append(31)
        counter = counter + 1
    return funcdeck

def shuffledeck(funcdeck):
    deckshuffled = []
    counter = 0
    while counter < 50:     #initializes shuffled deck
        deckshuffled.append(0)
        counter = counter + 1
    counter = 0
    while counter < 50:
        cardplace = random.randint(1,50-counter)
        place = 0
        counter2 = 0
        while counter2 < cardplace:
            while deckshuffled[place]!=0:
                place = place + 1
            counter2 = counter2 + 1
            if counter2 < cardplace - 1:
                place = place + 1
        deckshuffled[place] = funcdeck[counter]
        counter = counter + 1
    return deckshuffled

def shuffleboard():
    funcboard = [-2,-2,-2,-2,-2,-3,-3,11,11,21,21,31,31]
    boardshuffled = []
    counter = 0
    while counter < 13:     #initializes shuffled board
        boardshuffled.append(0)
        counter = counter + 1
    counter = 0
    while counter < 13:
        cardplace = random.randint(1,13-counter)
        place = 0
        counter2 = 0
        while counter2 < cardplace:
            while boardshuffled[place]!=0:
                place = place + 1
            counter2 = counter2 + 1
            if counter2 < cardplace - 1:
                place = place + 1
        boardshuffled[place] = funcboard[counter]
        counter = counter + 1
    return boardshuffled

def cardtype(functype):
    if functype == -3:
        retval = 5
    if functype == -2:
        retval = 4
    if functype > 0:
        retval = int(functype / 10)
    return retval

def stresscalc(funcgridpoint,funcstress):   #calculates stress at gridpoint and adds it
    if funcgridpoint > 0:
        funcstress = funcstress + (funcgridpoint % 10)
    else:
        funcstress = funcstress + funcgridpoint
        if funcstress < 0:
            funcstress = 0
    return funcstress

def stressfaceprint(funcgrid):
    counterx = 0
    while counterx < 9:
        countery = 0
        while countery < 3:
            gridvalue = funcgrid[counterx][countery]
            if gridvalue > 0:
                gridvalue = gridvalue % 10
                counters = 0
                while counters < gridvalue:
                    screen.blit(stressface,(counterx*150+35 + counters*50,countery*200+145))       #prints stressed faces
                    counters = counters + 1
            countery = countery + 1
        counterx = counterx + 1

def update(funcgrid):   #increases stress each turn
    gameflag = 0
    funcx = 0
    while funcx < 9:
        funcy = 0
        while funcy < 3:
            if funcgrid[funcx][funcy] > 0:
                basestress = funcgrid[funcx][funcy]%10
                gridval = int(funcgrid[funcx][funcy]/10)  #type of stress in space
                stresschange = checkaround(funcx,funcy,funcgrid)
                stressnum = stresschange + 2*basestress
                if gridval == 1:
                    stressrating = 40
                elif gridval == 2:
                    stressrating = 25
                else:
                    stressrating = 15
                stressdenom = stressnum + stressrating
                stresschance = random.randint(1,stressdenom)
                if stresschance <= stressnum:
                    if (funcgrid[funcx][funcy])%10 == 5:
                        gameflag = 2   #player loses
                    funcgrid[funcx][funcy] = funcgrid[funcx][funcy] + 100
            funcy = funcy+1
        funcx = funcx + 1
    funcx = 0     #resets grid--values greater than 100 are temporary
    while funcx < 9:
        funcy = 0
        while funcy < 3:
            if funcgrid[funcx][funcy]>100:
                funcgrid[funcx][funcy] = funcgrid[funcx][funcy] - 99
            funcy = funcy + 1
        funcx = funcx + 1
    return funcgrid,gameflag

def checkaround(funcxx,funcyy,funcgrid2):
    xcoord = [-1,-1,1,1,-2,2]
    ycoord = [-1,1,-1,1,0,0]
    addstress = 0
    circlecounter = 0
    while circlecounter < 6:
        xtemp = funcxx + xcoord[circlecounter]
        ytemp = funcyy + ycoord[circlecounter]
        if xtemp >= 0 and xtemp <9 and ytemp >=0 and ytemp < 3:  #checked space on board?
            if funcgrid2[xtemp][ytemp] > 0:   #checked space contains stressor
                thing1 =  (funcgrid2[xtemp][ytemp])%100
                thing2 = funcgrid2[funcxx][funcyy]
                if thing1==thing2:
                    addstress = addstress + 2*int(thing1/10)  #double stress if matches
                else:
                    addstress = addstress + int(thing1/10)
        circlecounter = circlecounter + 1
    return addstress

def instructions():
    screen.fill((100,200,200))
    yesno=pygame.image.load("yesno.png")
    line = []
    line.append("You are trying to make it through the day without getting too stressed.")
    line.append("Click the space on the activity on which you wish to start.")
    line.append("Each turn you move by clicking on a space adjacent to your present space.")
    line.append("Some activities are stressful, others are calming.")
    line.append("Delaying a stressful activity will make it more stressful.")
    line.append("Clusters of stressful activities become more stressful more quickly.")
    line.append("You win by making it through until 8:00pm.")
    line.append("You lose if your stress level becomes too high . . .")
    line.append("   . . . or if any activity attains a stress level greater than five.")
    line.append("      Good luck!!!   (Press any key to continue)")
    endloop = 0
    while True:
        textask = font.render("Welcome to Sober Life.  Do you want instructions?",True,(100,100,100))
        screen.blit(textask,(300,300))
        screen.blit(yesno,(450,500))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos,ypos = pygame.mouse.get_pos()
                if ypos > 500 and ypos < 700:
                    if xpos > 750 and xpos < 1050:   #no instructions
                        return
                    elif xpos > 450 and xpos < 750:
                        screen.fill((100,200,200))
                        linecounter = 0
                        while linecounter < 10:
                            textnow = font.render(line[linecounter],True,(100,100,100))
                            screen.blit(textnow,(10,linecounter*75))
                            linecounter = linecounter + 1
                        pygame.display.flip()
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    return

def difficultysetting():
    screen.fill((100,200,200))
    stressbuttons=pygame.image.load("stressbuttons.png")
    while True:
        settingask = font.render("Click on the sort of day you will have.",True,(100,100,100))
        screen.blit(settingask,(300,300))
        screen.blit(stressbuttons,(0,500))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos,ypos = pygame.mouse.get_pos()
                if ypos > 500 and ypos < 700:  #need to add actual values
                    if xpos < 300:
                        stresscards = [12,24,34,42]
                    elif xpos < 600:
                        stresscards = [12,24,32,40]
                    elif xpos < 900:
                        stresscards = [10,22,32,42]
                    elif xpos < 1200:
                        stresscards = [12,22,30,40]
                    else:
                        stresscards = [10,20,30,40]
                    return stresscards
                            

            
        
    

    
   
screen = pygame.display.set_mode((1500,800))
instructions()
difset = difficultysetting()
screen.fill((100,200,200))
pictures=[]
emptysquare=pygame.image.load("emptysquare.png")
pictures.append(emptysquare)    #  pictures[0] is empty square
jobstress=pygame.image.load("jobstress.png")  # pictures[1] is job
pictures.append(jobstress)
familystress=pygame.image.load("familystress.png")  # pictures[2] is family
pictures.append(familystress)
healthstress=pygame.image.load("healthstress.png")   # pictures[3] is health
pictures.append(healthstress)
exercise=pygame.image.load("exercise.png")   # pictures[4] is exercise
pictures.append(exercise)
meditation=pygame.image.load("meditation.png")  # pictures[5] is meditation
pictures.append(meditation)
banner=pygame.image.load("banner.png")
quitbutton=pygame.image.load("quitbutton.png")
stressbar=pygame.image.load("stressbar.png")
stressbit=pygame.image.load("stressbit.png")
stressface=pygame.image.load("stressface.png")

grid = []     #sets up grid  10 x 3
x = 0
while x < 10:
    grid.append([0]*3)
    x = x+1
x = 0
while x < 10:
    y = 0
    while y < 3:
        if (x+y)%2==1:
            grid[x][y] = 1
        y = y+1
    x = x+1
y = 0   #sets up starting position
while y < 3:
    x = 0
    while x < 9:
        if grid[x][y] == 1:
            screen.blit(pictures[0],(x*150,y*200))
        x = x+1
    y = y+1

theboard = shuffleboard() 

soberdeck = makedeck(difset)
soberdeck = shuffledeck(soberdeck)


counter = 0
y = 0   #sets up starting cards
while y < 3:
    x = 0
    while x < 9:
        if grid[x][y] == 1:
            grid[x][y]= theboard[counter]
            thecard = cardtype(theboard[counter])
            screen.blit(pictures[thecard],(x*150+10,y*200+10))
            counter = counter + 1
        x = x+1
    y = y+1

screen.blit(quitbutton,(1350,700))  #places quit button
screen.blit(stressbar,(1,650))
xcoord = -1   #starting off the board
ycoord = -1
timenow = 0
gameover = 0
stresslevel = 0
stressfaceprint(grid)     
pygame.display.flip()


while gameover==0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xpos,ypos = pygame.mouse.get_pos()
            if xpos > 1350 and ypos > 700:   #quit button exits game
                gameover  = 3   #  gameover = 3 means player has quit
                break
            gridx,gridy,posflag = findpos(xpos,ypos)
            if posflag==0:
                invalidmove = 0
                if xcoord > -1:    #already on board
                    if abs(xcoord - gridx)+ abs(ycoord - gridy) == 2 and gridx != xcoord:  #valid move
                        timenow = timenow + 1
                        cardpick = cardtype(soberdeck[timenow])
                        screen.blit(pictures[cardpick],(xcoord*150 + 10, ycoord*200 + 10))
                        grid [xcoord][ycoord] = soberdeck[timenow]
                    else:
                        invalidmove=1
                if invalidmove==0:
                    screen.blit(banner,(gridx*150,gridy*200))     
                    stresslevel = stresscalc(grid[gridx][gridy],stresslevel)
                    if stresslevel > 10:
                        gameover = 2    #  gameover = 2 means player has lost
                        break
                    grid[gridx][gridy] = 0     #current location of player is considered empty
                    if timenow > 47:    #end of game due to time expired
                        gameover = 1   #  gameover = 1 means player has won
                        break
                    grid,gameover = update(grid)
                    if gameover == 2:
                        break
                    timeprint(timenow,gridx,gridy)
                    xcoord = gridx
                    ycoord = gridy
                    screen.blit(stressbar,(1,650))
                    stresscounter = 0
                    while stresscounter < stresslevel:
                        screen.blit(stressbit,(stresscounter*100+250,650))
                        stresscounter = stresscounter + 1

                    stressfaceprint(grid)     
                    pygame.display.flip()

while True:
    if gameover == 1:
        screen.fill((30,200,30))
        text1 = font.render("You have managed your stress!!!",True,(100,100,100))
        text2 = font.render("Congratulations, you have won!!!",True,(100,100,100))
    if gameover == 2:
        screen.fill((150,0,0))
        text1 = font.render("Your stress levels are too high!!  You have lost",True,(50,200,200))
        text2 = font.render("Don't worry, you can try again tomorrow.",True,(50,200,200))
    if gameover == 3:
        screen.fill((50,50,50))
        text1 = font.render("Sorry you couldn't finish your game.",True,(200,200,200))
        text2 = font.render("Perhaps you can try again later.",True,(200,200,200))
    text3 = font.render("(Press any key to exit.)",True,(250,100,250))
    screen.blit(text1,(300,200))
    screen.blit(text2,(300,400))
    screen.blit(text3,(450,650))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
    
        
    
