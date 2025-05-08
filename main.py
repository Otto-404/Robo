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
    wait(1750)
    robo.drive(SPEED,72)
    wait(500)
    robo.drive(SPEED,0)
    wait(1300)
    robo.drive(SPEED,-67)
    wait(500)
    robo.drive(SPEED,0)
    wait(1200)
    robo.drive(SPEED,-60)
    wait(500)
    robo.drive(SPEED,0)
    wait(1500)
    robo.drive(SPEED,73)
    wait(500)
    robo.drive(SPEED,0)
    wait(1250)
    #Checkpoint 1
    robo.drive(SPEED,45)
    wait(500)
    robo.drive(SPEED,0)
    wait(800)
    robo.drive(SPEED,-50)
    wait(400)
    robo.drive(SPEED,0)
    wait(1600)
    robo.drive(SPEED,-40)
    wait(400)
    robo.drive(SPEED,0)
    wait(1000)
    robo.drive(SPEED,45)
    wait(1500)
    robo.drive(SPEED,0)
    wait(400)
    robo.drive(SPEED,-33)
    wait(1500)
    robo.drive(SPEED,0)
    wait(1900)
    robo.drive(SPEED,-75)
    wait(500)
    #Checkpoint 2
    robo.drive(SPEED,0)
    wait(1200)
    robo.drive(SPEED,70)
    wait(500)
    robo.drive(SPEED,0)
    wait(700)
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
    wait(800)
    robo.drive(SPEED,65)
    wait(500)
    robo.drive(SPEED,0)
    wait(3000)
    robo.stop
    break
 
