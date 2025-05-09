#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,InfraredSensor)
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
from time import sleep, time
#Ports
PORT_MOTOR_LEFT = Port.B
PORT_MOTOR_RIGHT = Port.C
PORT_SENSOR_COLOR = Port.S3

# Var Colors
LINE = 2
FLOOR = 27
LIMIT = (LINE + FLOOR) / 2

# VAR MOTORS
WHEEL_DIAMETER = 55.5
AXEL_TRACK = 147
TURN_CORRECTION = 1
SPEED = 1000
GAIN = 7
DISTANCE_CORRECT = 1
TURN_CORRECT_LEFT = 1
TURN_CORRECT_RIGHT = 1

MAX_TIME_IN_BLANK = 1000

eve3 = EV3Brick()

def printValue(text: str):
    print(text)
    eve3.screen.clear()
    eve3.screen.draw_text(1, 1, text)
    

Sensor_Color = ColorSensor(PORT_SENSOR_COLOR)

class Robo:
    def __init__(self):
        Motor_Left = Motor(Port.B)
        Motor_Right = Motor(Port.C)
        Motor_Left.reset_angle(100)
        self.motor = DriveBase(Motor_Left, Motor_Right,wheel_diameter=WHEEL_DIAMETER, axle_track=AXEL_TRACK)
        self.motor.settings(straight_speed=5000, straight_acceleration=10000)
    
    def drive(self, speed, angle):
        self.motor.drive(-speed, -angle)

    def stop(self):
        self.motor.stop()

    def straight(self, distancia):
        self.motor.straight(-0.4481 * distancia) 
    def turn(self, angulo):
        angulo = -angulo
        angulo_novo = 0
        if (angulo > 0):
            angulo_novo = 1.10092* angulo
        else:
            angulo_novo = 1.052632 * angulo
        self.motor.turn(angulo_novo)


def inLine(light):
    if light < LIMIT:
        return print("Encontrei a linha preta")
    else:
        return print("Estou na linha branca")


robo = Robo()

    
while True:
    #Start
    robo.drive(SPEED,0)
    wait(1900)
    robo.drive(SPEED,75)
    wait(500)
    robo.drive(SPEED,0)
    wait(1500)
    robo.drive(SPEED,-75)
    wait(500)
    robo.drive(SPEED,0)
    wait(1600)
    robo.drive(SPEED,-75)
    wait(500)
    robo.drive(SPEED,0)
    wait(1600)
    robo.drive(SPEED,76)
    wait(500)
    robo.drive(SPEED,0)
    wait(1600)
    #Checkpoint 1
    robo.drive(SPEED,50)
    wait(500)
    robo.drive(SPEED,0)
    wait(700)
    robo.drive(SPEED,-50)
    wait(500)
    robo.drive(SPEED,0)
    wait(1650)
    robo.drive(SPEED,-45)
    wait(450)
    robo.drive(SPEED,0)
    wait(1150)
    #curva S
    robo.drive(SPEED,45)
    wait(600)
    robo.drive(SPEED,0)
    wait(600)
    robo.drive(SPEED,45)
    wait(1100)
    robo.drive(SPEED,0)
    wait(900)
    robo.drive(SPEED,-40)
    wait(1500)
    robo.drive(SPEED,0)
    wait(2100)
    robo.drive(SPEED,-75)
    wait(500)
    #Checkpoint 2
    robo.drive(SPEED,0)
    wait(1200)
    robo.drive(SPEED,70)
    wait(500)
    robo.drive(SPEED,0)
    wait(800)
    robo.drive(SPEED,75)
    wait(500)
    robo.drive(SPEED,0)
    wait(1200)
    robo.drive(SPEED,-70)
    wait(500)
    robo.drive(SPEED,0)
    wait(500)
    robo.drive(SPEED,-65)
    wait(500)
    robo.drive(SPEED,0)
    wait(950)
    robo.drive(SPEED,70)
    wait(500)
    robo.drive(SPEED,0)
    wait(3500)
    robo.stop
    break
 
