from gpiozero import LED, Button, TrafficLights
from time import sleep
from signal import pause
import random
# red = LED(25)
#yellow = LED(12)
# green = LED(16)
button = Button(21)
l1 = TrafficLights(25,12,16)
l2 = TrafficLights(9,6,19)
pRed = LED(4)
pGreen = LED(17)
#l2 = TrafficLights(

#test LEDs
# while True:
#     if button.is_pressed:
#         red.on()
#         yellow.on()
#         green.on()
#     else:
#         red.off()
#         yellow.off()
#         green.off()

# while True:
#     lights.blink()
#     button.wait_for_press()
#     lights.off()
#     button.wait_for_release()

def streetLights():
    while True:
        pGreen.on()
        l1.red.on()
        l2.green.on()
        sleep(6)
        pGreen.blink(0.25,0.25)
        l2.green.off()
        l2.amber.on()
        sleep(2)
        l2.amber.off()
        l2.red.on()
        pGreen.off()
        pRed.on()
        sleep(1)
        l1.amber.on()
        sleep(1)
        l1.amber.off()
        l1.red.off()
        l1.green.on()
        sleep(8)
        l1.green.off()
        l1.yellow.on()
        sleep(2)
        l1.red.on()
        l2.amber.on()
        l1.amber.off()
        sleep(1)
        pRed.off()
        l2.amber.off()
        l2.red.off()

def night():
    while True:
        pRed.blink()
        l1.amber.blink(0.5,0.5)
        l2.amber.blink(0.5,0.5)
        pause()
     
#streetLights()
#night()
