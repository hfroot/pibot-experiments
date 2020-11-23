# a library to condense some useful move commands
import explorerhat as hat
from time import sleep

def stop():
    hat.motor.one.stop()
    hat.motor.two.stop()

def set_speed(motor, speed):
    if speed > 0:
        motor.forward(speed)
    elif speed < 0:
        motor.backward(-speed)
    else:
        motor.stop()

def move(oneSpeed, twoSpeed, time=0):
    set_speed(hat.motor.one, oneSpeed)
    set_speed(hat.motor.two, twoSpeed)
    if time > 0:
        sleep(time)
        stop()

def forward(speed=100, time=0):
    move(speed, speed, time)

def left(speed=60, time=0.78):
    move(-speed, speed, time)

def right(speed=60, time=0.76):
    move(speed, -speed, time)

def backward(speed=100, time=2):
    move(-speed, -speed, time)
