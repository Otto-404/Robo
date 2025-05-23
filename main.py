#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Ports
PORT_MOTOR_LEFT = Port.D
PORT_MOTOR_RIGHT = Port.A

# Configurações iniciais
WHEEL_DIAMETER = 55.5
AXEL_TRACK = 147

eve3 = EV3Brick()

def printValue(text: str):
    print(text)
    eve3.screen.clear()
    eve3.screen.draw_text(1, 1, text)

class Robo:
    def __init__(self):
        # Motores individuais
        self.motor_esquerdo = Motor(PORT_MOTOR_LEFT)
        self.motor_direito = Motor(PORT_MOTOR_RIGHT)

        # Zera ângulo inicial
        self.motor_esquerdo.reset_angle(0)
        self.motor_direito.reset_angle(0)

    def mover_motor_esquerdo(self, velocidade, tempo_ms):
        self.motor_esquerdo.run(velocidade)
        wait(tempo_ms)
        self.motor_esquerdo.stop()

    def mover_motor_direito(self, velocidade, tempo_ms):
        self.motor_direito.run(velocidade)
        wait(tempo_ms)
        self.motor_direito.stop()

    def parar_todos(self):
        self.motor_esquerdo.stop()
        self.motor_direito.stop()

robo = Robo()
var = 1
while True:
    # Exemplo de uso:
    if var == 1:
        printValue("Movendo Cabeça")
        robo.mover_motor_direito(380, 500)
        wait(1000)
        var = 2

    printValue("Movendo Pernas")
    robo.mover_motor_esquerdo(408.5, 450)
    wait(500)
    printValue("Movendo Cabeça")
    robo.mover_motor_direito(-600, 550)
    wait(700)
    printValue("Movendo Pernas")
    robo.mover_motor_esquerdo(408.5, 450)
    wait(500)
    printValue("Movendo Cabeça")
    robo.mover_motor_direito(600, 550)
    wait(700)
    printValue("Movendo Pernas")
    robo.mover_motor_esquerdo(408.5, 450)
    wait(500)
    printValue("Movendo Cabeça")
    robo.mover_motor_direito(-600, 550)
    wait(700)
    printValue("Movendo Pernas")
    robo.mover_motor_esquerdo(420, 500)
    wait(500)
    printValue("Movendo Cabeça")
    robo.mover_motor_direito(600, 550)
    wait(700)

    #printValue("Parando motores")
   #robo.parar_todos()
