from microbit import *
import random
import time
# startovací sekvence

jedna = (Image('00000:'
           '00000:'
           '00900:'
           '00000:'
           '00000'))

dva = (Image('00000:'
           '00090:'
           '00000:'
           '09000:'
           '00000'))

tri = (Image('00000:'
           '00090:'
           '00900:'
           '09000:'
           '00000'))

ctyri = (Image('00000:'
               '09090:'
               '00000:'
               '09090:'
               '00000'))

pet = (Image('00000:'
             '09090:'
             '00900:'
             '09090:'
             '00000'))

sest = (Image('00000:'
           '09090:'
           '09090:'
           '09090:'
           '00000'))


kocka = [jedna, dva, tri, ctyri, pet, sest]


#pořád
while True:
    if button_a.was_pressed() or button_b.was_pressed() or pin_logo.is_touched():
        display.clear()
        display.show(Image.GHOST)
        time.sleep(1)
        display.clear()
        x = random.choice(kocka)
        display.show(x)
        print(x)
