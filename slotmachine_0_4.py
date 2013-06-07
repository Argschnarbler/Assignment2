# Source File Name: slotmachine_0_1.py
# Author's Name: Jacob Meikle
# Last Modified By: Jacob Meikle
# Date Last Modified: May 24, 2012
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the pygame module
                        
  Version: 0.4 - *Added jack pot label
                 *Added sounds
                 *cleaned up code and removed print functions.
  
  Version: 0.3 - *Added functionality to the remaining buttons.
                  
                        
  Version: 0.2 - *Created a click event for the boudaries of the spin button which sets the 
                  pull the handle function in motion.
                 *Created a function called reelSwitcher that outputs the correct image assets to the reels after spinning.
                 

  Version: 0.1 - *Created Gui with no functionality
                  * Created Back end functions for the slot machine program Reels, pullthehandle, and
                 is_number (a validation function).
                 * Text output provides debugging information to check if the Slot Machine program does
                 what it's supposed to do.
                 * Used research from the internet to set the Reels function to simulate basic slot reels
"""

# import statements
import random
import pygame
import pygame.mixer


def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Watermelon """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Watermelon"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    
    
    return Bet_Line


def pullthehandle(Bet, Player_Money, Jack_Pot, reel1, reel2, reel3,Jack_Win):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    winnings = 0
    Fruit_Reel = Reels()
    #switch reel images
    reel1 = pygame.image.load(reelSwitcher(Fruit_Reel[0]))
    reel2 = pygame.image.load(reelSwitcher(Fruit_Reel[1]))
    reel3 = pygame.image.load(reelSwitcher(Fruit_Reel[2]))
    
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = Bet*15,True
    elif Fruit_Reel.count("Watermelon") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = Bet*25,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("Watermelon") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:      
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        
        if  jackpot_try  == jackpot_win:
            Player_Money += Jack_Pot
            winnings = Jack_Pot
            Jack_Pot = 500
            Jack_Win = True
        elif jackpot_try != jackpot_win:  
            Jack_Win = False
    
    return Player_Money, Jack_Pot, winnings, reel1, reel2, reel3, Jack_Win

def reelSwitcher(symbol):
    """ This function interprets a symbol string and returns the appropriate image path."""
     
    if symbol == "Grapes":
        return "assets/grapes.jpg"
    elif symbol == "Watermelon":
        return "assets/watermelon.jpg"
    elif symbol == "Orange":
        return "assets/orange.jpg"
    elif symbol == "Cherry":
        return "assets/cherry.jpg"
    elif symbol == "Bar":
        return "assets/bar.jpg"
    elif symbol == "Bell":
        return "assets/bell.jpg"
    elif symbol == "Seven":
        return "assets/seven.jpg"
    elif symbol == "Blank":
        return "assets/blank.jpg"



def main():
    """ The Main function that runs the game loop """
    
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Bet = 10
    win = 0
    amloop = 1487
    Jack_Win = False
    spun = False
    tick = 0
    #pygame init
    pygame.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 22)
    red = (240, 15, 15)
    
    #display config
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Super Slot Machine 4000")
    
    #entities
    background = pygame.image.load("assets/bg.jpg")
    background = background.convert()
    
    reel1 = pygame.image.load("assets/blank.jpg")
    reel2 = pygame.image.load("assets/blank.jpg")
    reel3 = pygame.image.load("assets/blank.jpg")
    
    spin = pygame.image.load("assets/spin.jpg")
    reset = pygame.image.load("assets/reset.jpg")
    stop = pygame.image.load("assets/quit.jpg")
    
    bet10 = pygame.image.load("assets/10.jpg")
    bet25 = pygame.image.load("assets/25.jpg")
    bet50 = pygame.image.load("assets/50.jpg")
    bet100 = pygame.image.load("assets/100.jpg")
    
    credit = myfont.render( str(Player_Money), 1, red)
    mybet = myfont.render( str(Bet), 1, red)
    won = myfont.render( str(win), 1, red)
    jackpot_message = myfont.render( "Jackpot: "+ str(Jack_Pot), 1, red)
    
    #sounds
    ambient = pygame.mixer.Sound('assets/ambience_casino.wav')
    button = pygame.mixer.Sound('assets/button.wav')
    spin_sound = pygame.mixer.Sound('assets/spin.wav')
    pay = pygame.mixer.Sound('assets/pay.wav')
    jackpot = pygame.mixer.Sound('assets/jackpot.wav')
    ambient.set_volume(0.5)
    
    #A - Assign values to key variables
    clock = pygame.time.Clock()
    
    # Flag to initiate the game loop
    KeepGoing = True
    
    while KeepGoing == True:
        
        clock.tick(60)
        
        amloop += 1
        #ambience loop
        if amloop == 1488:
            ambient.play()
            amloop = 0
            
        #re-enable spin button after sound is finished
        if spun:
            tick += 1
            if tick >= 75:
                spun = False
                tick = 0
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                
                #spin button
                size = spin.get_size() 
                if (mouse_x >= 465) and (mouse_x <= 465 + size[0]) and (mouse_y >= 400) and (mouse_y <= 400 + size[1] and spun == False): 
                    if Player_Money >= Bet:                  
                        #Pull the handle         
                        Player_Money, Jack_Pot, win, reel1, reel2, reel3, Jack_Win = pullthehandle(Bet,Player_Money,Jack_Pot,reel1,reel2,reel3,Jack_Win)
                        spin_sound.play() 
                        spun = True
                        
                        #update text
                        credit = myfont.render( str(Player_Money), 1, red)
                        mybet = myfont.render( str(Bet), 1, red)
                        won = myfont.render( str(win), 1, red)
                        jackpot_message = myfont.render( "Jackpot: "+ str(Jack_Pot), 1, red)
                        
                        spin = pygame.image.load("assets/spin.jpg")  
                    else:
                        spin = pygame.image.load("assets/spin_down.jpg")  
                        
                    #win sound
                    if win != 0:
                        pay.play()
                        #jackpot ? fingers crossed
                        if Jack_Win:
                            jackpot.play()
                            jackpot_message = myfont.render( "Jackpot Winner!", 1, red)
                        
                        
                #bet10 button
                size = bet10.get_size() 
                if (mouse_x >= 100) and (mouse_x <= 100 + size[0]) and (mouse_y >= 400) and (mouse_y <= 400 + size[1]): 
                    Bet = 10;
                    mybet = myfont.render( str(Bet), 1, red)
                    button.play()
                #bet25 button
                size = bet25.get_size() 
                if (mouse_x >= 180) and (mouse_x <= 180 + size[0]) and (mouse_y >= 400) and (mouse_y <= 400 + size[1]): 
                    Bet = 25;
                    mybet = myfont.render( str(Bet), 1, red)
                    button.play()
                #bet50 button
                size = bet50.get_size() 
                if (mouse_x >= 260) and (mouse_x <= 260 + size[0]) and (mouse_y >= 400) and (mouse_y <= 400 + size[1]): 
                    Bet = 50;
                    mybet = myfont.render( str(Bet), 1, red)
                    button.play()
                #bet100 button
                size = bet100.get_size() 
                if (mouse_x >= 340) and (mouse_x <= 340 + size[0]) and (mouse_y >= 400) and (mouse_y <= 400 + size[1]): 
                    Bet = 100;
                    mybet = myfont.render( str(Bet), 1, red)
                    button.play()
                #reset button
                size = reset.get_size() 
                if (mouse_x >= 110) and (mouse_x <= 110 + size[0]) and (mouse_y >= 10) and (mouse_y <= 10 + size[1]): 
                    #revert everything to initial values
                    Player_Money = 1000
                    Jack_Pot = 500
                    Bet = 10
                    win = 0
                    
                    reel1 = pygame.image.load("assets/blank.jpg")
                    reel2 = pygame.image.load("assets/blank.jpg")
                    reel3 = pygame.image.load("assets/blank.jpg")
                    
                    credit = myfont.render( str(Player_Money), 1, red)
                    mybet = myfont.render( str(Bet), 1, red)
                    won = myfont.render( str(win), 1, red)
                    button.play()
                #quit button
                size = stop.get_size() 
                if (mouse_x >= 475) and (mouse_x <= 475 + size[0]) and (mouse_y >= 10) and (mouse_y <= 10 + size[1]): 
                    pygame.display.quit()
        
        #Refresh
        screen.blit(background, (0, 0))
        
        #top buttons
        screen.blit(reset, (110, 10))
        screen.blit(stop, (475, 10))
        #reels
        screen.blit(reel1, (125, 80))
        screen.blit(reel2, (275, 80))
        screen.blit(reel3, (425, 80))
        #bet buttons
        screen.blit(bet10, (100, 400))
        screen.blit(bet25, (180, 400))
        screen.blit(bet50, (260, 400))
        screen.blit(bet100,(340, 400))
        #spin button
        screen.blit(spin,(465, 400))
        #text
        screen.blit(credit,(115, 315))
        screen.blit(mybet,(295, 315))
        screen.blit(won,(390, 315))
        screen.blit(jackpot_message,(260,10))
        pygame.display.flip()
        

if __name__ == "__main__": main()