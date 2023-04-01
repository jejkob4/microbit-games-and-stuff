from microbit import *
import time
import random
import music

# startovací sekvence
display.scroll('Whack A Mole!')
display.scroll('Press logo to play!')
music.play(music.FUNK)        

# imgs + endgame
buttonA = Image('00700:'
                '09000:'
                '99987:'
                '09000:'
                '00700')

buttonB = Image('00700:'
                '00090:'
                '78999:'
                '00090:'
                '00700')

endgame = ('Game Over!')

# random list
element_list = [button_a, button_b]
       
# definice
def game_over(end):
    display.scroll(end)   

def timer_3():
        display.show('3')
        time.sleep(1)
        display.show('2')
        time.sleep(1)
        display.show('1')
        time.sleep(1)

def success_press():
            display.clear()
            display.show(Image.YES)
            time.sleep(2)
            display.clear()
    
def show_directions(img):
    display.show(img)
    time.sleep(2)

#variably pro loop
count = 0

   
#pořád
while True:
    if pin_logo.is_touched():
        while (count <3): 
            count = count + 1
            
            display.show(Image.SKULL)
            time.sleep(1)
            display.clear()
            time.sleep(1)

            x = (random.choice(element_list))
        
            if x == button_a:
                y = buttonA
                show_directions(y)
            if x == button_b:
                y = buttonB
                show_directions(y)
            
            timer_3()
        
            if x.was_pressed():
                success_press()
        else:
            game_over(endgame) 
