#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
from threading import Thread

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
Line = 5
Floor = 20
Limit = (Line + Floor) / 2
Distance_Upper = 30
Distance_Lower = 10
Limit_Obstacle = (Distance_Upper - Distance_Lower) / 2
# Define a velocidade do robo a um valor x milimetros por segundo.
Speed = 200
Gain = 8
signal = 1

# Loop para seguir a linha sem ponto de parada.
preto = False
anteriorPreto=False
while True:
    print(Sensor_Color.reflection())
    # Calcula o desvio do limite.
    Distance = Sensor_Distance.distance()
    Light = Sensor_Color.reflection()
    Curve = Light - Limit * signal
    if (Limit < 0):
        preto = True
    else:
        preto = False
    if (anteriorPreto !=)
    # Calcula a taxa de rotação
    Turn_Rate = Gain * Curve
    # Define a velocidade base e a taxa de rotação baseada nos cálculos anteriores
    robo.drive(Speed, Turn_Rate)
    signal = signal*(-1)
    # if obstaculo
   # while Distance <= Distance_Upper and Distance >= Distance_Lower:
   #     robo.stop()
   #     Turn_Rate = (Gain * 13)
   #     robo.turn(90)
   #     robo.drive(Speed, Turn_Rate)
   #     wait (1000)
   #     break

    wait(10)
