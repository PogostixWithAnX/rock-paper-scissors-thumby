import thumby
import time
import math
thumby.display.setFPS(60)

#Version 1.0. Created by Pogostix_With_An_X, 2025. Feel free to edit.
#This is my first project so judge me gently ok, I cry easy ;w;
#Note:Could probably be expanded to add Lizard and Spock on A and B. You'd have to shrink the sprites.

#Rock Sprite
# BITMAP: width: 15, height: 21
rockMap = bytearray([0,160,120,254,255,247,251,126,190,120,184,96,224,192,128,
           5,10,21,43,87,43,87,47,95,47,95,47,23,15,7,
           0,0,0,0,4,14,31,4,4,4,0,0,0,0,0])

#Paper Sprite
# BITMAP: width: 16, height: 24
paperMap = bytearray([0,0,0,192,255,191,183,183,247,119,110,238,110,110,252,252,
           128,224,252,239,237,237,173,189,183,183,181,181,245,255,63,1,
           0,0,0,1,1,33,51,251,51,35,3,3,3,3,0,0])

#Scissors Sprite
# BITMAP: width: 21, height: 25
scissorsMap = bytearray([0,0,0,0,0,0,0,0,0,0,0,255,254,240,0,0,0,0,0,0,0,
           4,4,12,12,12,28,28,28,28,28,28,221,109,141,12,12,20,36,68,68,56,
           0,0,0,0,0,0,0,64,64,64,240,231,72,8,9,6,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])

#Secret Sprite
# BITMAP: width: 25, height: 18
secretMap1 = bytearray([14,81,169,5,2,26,66,66,26,2,5,169,81,14,0,0,64,160,160,16,32,16,32,64,128,
           0,0,0,1,250,134,6,14,254,142,7,0,241,1,2,4,8,240,80,145,78,128,64,41,22,
           0,0,0,0,1,3,3,3,1,3,3,3,1,2,2,2,2,1,0,0,0,0,0,0,0])
# BITMAP: width: 25, height: 18
secretMap2 = bytearray([14,81,169,5,2,26,66,66,26,2,5,169,81,14,20,20,34,196,2,4,40,208,0,0,0,
           0,0,0,1,250,134,6,14,254,142,7,0,241,1,2,6,10,241,16,8,5,2,0,0,0,
           0,0,0,0,1,3,3,3,1,3,3,3,1,2,2,2,2,1,0,0,0,0,0,0,0])

#Happy Sprite :)
# BITMAP: width: 5, height: 4
happyMap = bytearray([4,9,8,9,4])

#Sad Sprite :(
# BITMAP: width: 5, height: 4
sadMap = bytearray([8,5,4,5,8])

#Happy Noise
def happyNoise():
    thumby.audio.play(785, 200)
    time.sleep(0.20)
    thumby.audio.play(659, 200)
    time.sleep(0.20)
    thumby.audio.play(988, 200)

#Sad Noise
def sadNoise():
    thumby.audio.play(880, 200)
    time.sleep(0.20)
    thumby.audio.play(698, 200)
    time.sleep(0.20)
    thumby.audio.play(659, 200)

def drawNoise():
    thumby.audio.play(659, 200)
    time.sleep(0.20)
    thumby.audio.play(659,200)
    time.sleep(0.20)
    thumby.audio.play(988, 200)

#Intro Screen
startscreen = True
while(startscreen): #ROCK
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
    thumby.display.drawText("ROCK", 16, 1, 1)
    thumby.display.update()
    time.sleep(0.25)
    
    #PAPER
    thumby.display.drawText("PAPER", 12, 10, 1)
    thumby.display.update()
    time.sleep(0.25)
    
    #SCISSORS
    thumby.display.drawText("SCISSORS", 1, 20, 1)
    thumby.display.update()
    time.sleep(0.25)
    
    #Press A
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    thumby.display.drawText("Press A", 13, 33, 1)
    thumby.display.update()
    time.sleep(0.5)
    waiting = True
    while(waiting):
        if thumby.buttonA.justPressed():
            startscreen = False
            running = True
            waiting = False
        elif thumby.buttonB.justPressed(): #Press B...?
            waiting = False
            thankyou = True
            frameCount = 0
            thumby.display.setFPS(5)
            while(thankyou):
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.fill(0)
                thumby.display.drawText("Thank u fur playin", 1, 1, 1)
                thumby.display.drawText("my Hoomin's silly", 1, 7, 1)
                thumby.display.drawText("game! - Luna", 1, 14, 1)
                thumby.display.drawText("A: Go Back", 1, 34, 1)
                
                secretSpr = thumby.Sprite(25, 18, secretMap1+secretMap2, 47,22)
                secretSpr.setFrame(frameCount)
                thumby.display.drawSprite(secretSpr)
                frameCount += 1
                thumby.display.update()
                
                if thumby.buttonA.justPressed():
                    break

while(running): #Main game loop
    #Player picks an option
    #drawing sprites to screen
    thumby.display.setFPS(30)
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    rockSpr = thumby.Sprite(15, 21, rockMap, 1, 5)#Rock Sprite position
    thumby.display.drawSprite(rockSpr)
    thumby.display.update()
    time.sleep(0.25)
    
    paperSpr = thumby.Sprite(16, 24, paperMap, 25, 0)#Paper Sprite position
    thumby.display.drawSprite(paperSpr)
    time.sleep(0.25)
    thumby.display.update()
    
    scissorsSpr = thumby.Sprite(21, 25, scissorsMap, 47, 1) #Scissors sprite
    thumby.display.drawSprite(scissorsSpr)
    time.sleep(0.25)
    
    thumby.display.drawText("Choose!", 15, 33, 1)
    thumby.display.update()
    
    print("Press Left for Rock, Up for Paper, Right for Scissors.")
    waiting = True
    while(waiting):
        if thumby.buttonL.justPressed():#Player picks Rock
            playerchoice = 1
            print("You choose... ROCK!")
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("You Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("ROCK", 1, 9, 1)
            rock2Spr= thumby.Sprite(15, 16, rockMap, 47, 19)
            thumby.display.drawSprite(rock2Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 1, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
            
        elif thumby.buttonU.justPressed():#Player picks Paper
            playerchoice = 2
            print("You choose... PAPER!")
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("You Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("PAPER", 1, 9, 1)
            paper2Spr= thumby.Sprite(16, 19, paperMap, 47, 19)
            thumby.display.drawSprite(paper2Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 1, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
            
        elif thumby.buttonR.justPressed():#Player picks Scissors
            playerchoice = 3
            print("You choose... SCISSORS!")
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("You Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("SCISSORS", 1, 9, 1)
            scissors2Spr= thumby.Sprite(21, 20, scissorsMap, 47, 19)
            thumby.display.drawSprite(scissors2Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 1, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
                    
        elif thumby.buttonD.justPressed(): #Wait there's a fourth option?
            playerchoice = 4
            print("You chose... LUNA!")
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("You Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("LUNA!", 1, 9, 1)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 1, 34, 1)
            thumby.display.update()
            frameCount = 0
            thumby.display.setFPS(5)
            stillWaiting = True
            while(stillWaiting):
                secretSpr = thumby.Sprite(25, 18, secretMap1+secretMap2, 47,22)
                secretSpr.setFrame(frameCount)
                thumby.display.drawSprite(secretSpr)
                frameCount += 1
                thumby.display.update()
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
            

    #Setting up random number generator for CPU choices
    import random
    list1 = [1,2,3]
    cpuchoice = random.choice(list1)
    
    if cpuchoice == 1:#CPU picks Rock
        print("CPU chooses... ROCK!")
        waiting = True
        while(waiting):
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("CPU Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("ROCK", 1, 9, 1)
            rock3Spr= thumby.Sprite(15, 16, rockMap, 1, 19)
            thumby.display.drawSprite(rock3Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 46, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
        
        
    elif cpuchoice == 2:#CPU picks Paper
        print("CPU chooses... PAPER!")
        waiting = True
        while(waiting):
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("CPU Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("PAPER", 1, 9, 1)
            paper3Spr= thumby.Sprite(16, 19, paperMap, 1, 19)
            thumby.display.drawSprite(paper3Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 46, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False
        
    elif cpuchoice == 3:#CPU picks Scissors
        print("CPU chooses... SCISSORS!")
        waiting = True
        while(waiting):
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("CPU Chose...", 1, 1, 1)
            thumby.display.update()
            time.sleep(0.25)
            thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("SCISSORS", 1, 9, 1)
            scissors2Spr= thumby.Sprite(21, 20, scissorsMap, 1, 19)
            thumby.display.drawSprite(scissors2Spr)
            time.sleep(0.25)
            thumby.display.update()
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("A: Next", 46, 34, 1)
            thumby.display.update()
            stillWaiting = True
            while(stillWaiting): #this is probably stupid but it works ok
                if thumby.buttonA.justPressed():
                    waiting = False
                    stillWaiting = False

    #Comparing choices to determine winner
    winner = "You Win! :D"
    loser = "You Lose :("
    draw = "Draw!"
    if int(playerchoice) == 1: #Player chooses Rock
        if int(cpuchoice) == 1:#VS Rock (Draw)
                print(draw)
                thumby.display.fill(0)
                waiting = True
                while(waiting):
                    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                    thumby.display.drawText("Draw!", 20, 10, 1)
                    thumby.display.update()
                    time.sleep(0.5)
                    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                    thumby.display.drawText("A: Next", 1, 34, 1)
                    thumby.display.update()
                    stillWaiting = True
                    while(stillWaiting): #this is probably stupid but it works ok
                        if thumby.buttonA.justPressed():
                            waiting = False
                            stillWaiting = False
                        
        elif int(cpuchoice) == 2:#VS Paper (Lose)
            print(loser)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                sadNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Lose", 13, 5, 1)
                sadSpr = thumby.Sprite(5, 4, sadMap, 32, 15)
                thumby.display.drawSprite(sadSpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
        elif int(cpuchoice) == 3:#VS Scissors (Win)
            print(winner)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                happyNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Win!", 13, 5, 1)
                happySpr = thumby.Sprite(5, 4, happyMap, 32, 15)
                thumby.display.drawSprite(happySpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
            
    elif int(playerchoice) == 2: #Player chooses Paper
        if int(cpuchoice) == 1:#VS Rock (Win)
            print(winner)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                happyNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Win!", 13, 5, 1)
                happySpr = thumby.Sprite(5, 4, happyMap, 32, 15)
                thumby.display.drawSprite(happySpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
        elif int(cpuchoice) == 2:#VS Paper (Draw)
            print(draw)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Draw!", 20, 10, 1)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
        elif int(cpuchoice) == 3:#VS Scissors (Lose)
            print(loser)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                sadNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Lose", 13, 5, 1)
                sadSpr = thumby.Sprite(5, 4, sadMap, 32, 15)
                thumby.display.drawSprite(sadSpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
    elif int(playerchoice) == 3: #Player chooses Scissors
        if int(cpuchoice) == 1:#VS Rock (Lose)
            print(loser)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                sadNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Lose", 13, 5, 1)
                sadSpr = thumby.Sprite(5, 4, sadMap, 32, 15)
                thumby.display.drawSprite(sadSpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
        elif int(cpuchoice) == 2:#VS Paper (Win)
            print(winner)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                happyNoise()
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("You Win!", 13, 5, 1)
                happySpr = thumby.Sprite(5, 4, happyMap, 32, 15)
                thumby.display.drawSprite(happySpr)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
        elif int(cpuchoice) == 3:#VS Scissors (Draw)
            print(draw)
            waiting = True
            thumby.display.fill(0)
            while(waiting):
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("Draw!", 20, 10, 1)
                thumby.display.update()
                time.sleep(0.5)
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                thumby.display.drawText("A: Next", 1, 34, 1)
                thumby.display.update()
                stillWaiting = True
                while(stillWaiting): #this is probably stupid but it works ok
                    if thumby.buttonA.justPressed():
                        waiting = False
                        stillWaiting = False
                        
    elif int(playerchoice) == 4:#Player made the secret best choice
        print("Luna always wins. It's the Rules.")
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5,1)
        thumby.display.drawText("Luna always wins.", 1, 1, 1)
        thumby.display.drawText("It's the Rules.", 1, 7, 1)
        happyNoise()
        thumby.display.drawText("A: Next", 1, 34, 1)
        frameCount = 0
        thumby.display.setFPS(5)
        stillWaiting = True
        while(stillWaiting):
            secretSpr = thumby.Sprite(25, 18, secretMap1+secretMap2, 47,22)
            secretSpr.setFrame(frameCount)
            thumby.display.drawSprite(secretSpr)
            frameCount += 1
            thumby.display.update()
            if thumby.buttonA.justPressed():
                waiting = False
                stillWaiting = False
                
    #Play again or nah?
    print("Play Again? A:Y B:N")
    waiting = True
    while(waiting):
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("Play Again?", 1, 1, 1)
        thumby.display.drawText("A:Y B:N", 1, 10, 1)
        thumby.display.update()
        time.sleep(0.5)
        if thumby.buttonA.justPressed():
            waiting = False
        elif thumby.buttonB.justPressed():
            thumby.reset()
    
