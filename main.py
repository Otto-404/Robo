#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

eve3 = EV3Brick()

def printValue(text: str):
    print(text)
    eve3.screen.clear()
    eve3.screen.draw_text(1, 1, text)
    

# Inicializa os Motores
Motor_Left = Motor(Port.B)
Motor_Right = Motor(Port.C)

# Inicializa o sensor de Cor.
Sensor_Color = ColorSensor(Port.S3)

# Inicializa o sensor infravermelho
Sensor_Distance = InfraredSensor(Port.S2)

# Inicializa o Objeto Drive Base, que controla os motores de forma paralela automaticamente
robo = DriveBase(Motor_Left, Motor_Right,wheel_diameter=55.5, axle_track=117)

# Calcule o limiar de luz.
Line = 2
Floor = 27
Limit = (Line + Floor) / 2
Distance_Upper = 6
Distance_Lower = 2
Limit_Obstacle = (Distance_Upper - Distance_Lower) / 2
# Define a velocidade do robo a um valor x milimetros por segundo.
Gain = 7


while True:
    Speed = 160 #160
    print(Sensor_Color.reflection())
    # Calcula o desvio do limite.
    Distance = Sensor_Distance.distance()
    Light = Sensor_Color.reflection()
    Curve = Light - Limit
    # Calcula a taxa de rotação
    Turn_Rate = Gain * Curve
    # Define a velocidade base e a taxa de rotação baseada nos cálculos anteriores
    robo.drive(Speed, Turn_Rate)
    # if obstaculo
    while Distance <= Distance_Upper and Distance >= Distance_Lower:
        robo.stop()
        robo.turn(-90)
        robo.straight(250)
        robo.turn(80)
        robo.straight(480)
        robo.turn(90)
        while Light > 7:
            Light = Sensor_Color.reflection()
            printValue(Light)
            print(Sensor_Color.reflection())
            robo.drive(Speed,0)
        robo.straight(30)
        robo.turn(-110)
        wait (100)
        break
    wait(10)
